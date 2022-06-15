
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

from functools import singledispatchmethod
from witness.core.abstract import AbstractBatch


class Batch(AbstractBatch):
    """
    Central class of entire lib.
    Able to store standardized data structure
    containing data in form of records and metadata dictionary.
    """

    __slots__ = ('data', 'meta')

    def __init__(self, data=None, meta=None):

        self.data: list or None = data
        self.meta: dict or None = meta
        self.is_restored: bool = False

    def info(self):

        if self.meta is None and self.data is None:
            return 'Batch object is not containing any data.'

        record_num = len(self.data) if self.data is not None else None

        info_string = f"""
        Number of records: {record_num}
        Was {'restored from dump' if self.is_restored else 'originally extracted'}
        Source: {self.meta['record_source']}
        Extraction datetime: {self.meta['extraction_timestamp']}
        """

        try:
            info_string = info_string + f"Tags: {self.meta['tags']}\n"
        except KeyError:
            pass

        return info_string

    def fill(self, extractor):
        output = extractor.extract().unify().output
        setattr(self, 'data', output['data'])
        setattr(self, 'meta', output['meta'])
        return self

    def push(self, loader):
        loader.prepare(self).load()
        return self

    def persist(self, uri):
        raise NotImplementedError

    def restore(self, uri):
        raise NotImplementedError

