#  Copyright (c) 2023.  Eugene Popov.
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

import csv
from typing import Optional
from witness.core.abstract import AbstractLoader, AbstractSerializer
from witness.serializers.common import JsonSerializer


class JSONFileLoader(AbstractLoader):

    def __init__(self, uri, serializer: Optional[AbstractSerializer] = JsonSerializer()):
        super().__init__(uri)
        self.serializer = serializer

    def prepare(self, batch):
        super().prepare(batch)
        output = self.serializer.from_batch(batch.data)
        self.output = output
        return self

    def attach_meta(self, meta_elements: Optional[list] = None):
        super().attach_meta(meta_elements)

    def load(self):
        raise NotImplemented

 
class CSVFileLoader(AbstractLoader):

    def __init__(self,
                 uri: str,
                 fieldnames: Optional[list] = None,
                 delimiter=',',
                 quotechar='"',
                 encoding: str = 'utf-8'):
        super().__init__(uri)
        self.fieldnames: Optional[list] = fieldnames
        self.delimiter: str = delimiter
        self.quotechar: str = quotechar
        self.encoding: str = encoding

    def prepare(self, batch):
        super().prepare(batch)
        self.output = batch.data
        setattr(self, 'fieldnames', batch.data[0].keys())
        return self

    def attach_meta(self, meta_elements: Optional[list[str]] = None):
        super().attach_meta(meta_elements)
        for element in self.meta_to_attach:
            for row in self.output:
                row[element] = self.meta_to_attach[element]
        return self

    def load(self, **writer_kwargs):
        with open(file=self.uri, mode='w', newline='', encoding=self.encoding) as file:
            writer = csv.DictWriter(file,
                                    fieldnames=self.fieldnames,
                                    delimiter=self.delimiter,
                                    quotechar=self.quotechar,
                                    **writer_kwargs)
            writer.writeheader()
            writer.writerows(self.output)

        return self

