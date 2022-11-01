#  Copyright (c) 2022.  Eugene Popov.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

import logging
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

log = logging.getLogger(__name__)


class AbstractBatch(metaclass=ABCMeta):

    @abstractmethod
    def fill(self, extractor):
        raise NotImplemented

    @abstractmethod
    def push(self, loader):
        raise NotImplemented

    @abstractmethod
    def dump(self, uri):
        raise NotImplemented

    @abstractmethod
    def restore(self, uri):
        raise NotImplemented


class AbstractExtractor(metaclass=ABCMeta):

    def __init__(self, uri=None):

        self.uri = uri
        self.output = None
        self.extraction_timestamp: datetime or None = None

    @abstractmethod
    def _set_extraction_timestamp(self):
        raise NotImplementedError

    @abstractmethod
    def extract(self):
        """
        An abstract method for data extraction.
        """
        raise NotImplementedError

    @abstractmethod
    def unify(self):
        """
        An abstract method for deserialization from data source.
        """
        raise NotImplementedError


class AbstractLoader(metaclass=ABCMeta):

    def __init__(self, uri=None):

        self.uri = uri
        self.batch = None
        self.output = None

    @abstractmethod
    def prepare(self, batch):
        """
        An abstract method of preparing data from a Batch object for loading.
        """
        self._set_batch(batch)

    @abstractmethod
    def attach_meta(self, meta_elements: [list[str]] or None = None):
        """
        An abstract method for attaching meta from Batch-object
        to data prepared for loading.
        """
        raise NotImplementedError

    @abstractmethod
    def load(self):
        """
        An abstract method for loading data to destination store.
        """
        raise NotImplementedError

    def _set_batch(self, batch):
        setattr(self, 'batch', batch)


class MetaIterator:

    def __init__(self, meta_class):
        self._class_attrs = [a for a in dir(meta_class)if not a.startswith('__') and not callable(getattr(meta_class, a))]
        self._class_size = len(self._class_attrs)
        self._current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index < self._class_size:
            element = self._class_attrs[self._current_index]
            self._current_index += 1
            return element
        raise StopIteration


@dataclass
class MetaData:

    record_source: Optional[str] = None
    extraction_timestamp: Optional[datetime] = None
    tags: Optional[list] = field(default_factory=list)
    dump_uri: Optional[str] = ''
    records_extracted: int = 0
    is_restored: bool = False

    def __iter__(self):
        return MetaIterator(self)
