
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

import csv
from witness.core.abstract import AbstractExtractor


class FileExtractor(AbstractExtractor):

    def extract(self):
        self.set_extraction_timestamp()

    def unify(self):
        raise NotImplementedError


class CSVFileExtractor(FileExtractor):

    def __init__(self, uri: str, delimiter=',', quotechar='"'):
        super().__init__()
        self.uri = uri
        self.delimiter = delimiter
        self.quotechar = quotechar

    def extract(self):
        with open(self.uri, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=self.delimiter, quotechar=self.quotechar)
            data = [row for row in reader]
            setattr(self, 'output', data)
        super().extract()
        return self

    def unify(self):
        data = self.output
        meta = {'extraction_timestamp': self.extraction_timestamp,
                'record_source': self.uri}

        setattr(self, 'output', {'meta': meta, 'data': data})

        return self

