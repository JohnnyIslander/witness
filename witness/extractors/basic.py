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

from datetime import datetime
from witness.core.abstract import AbstractExtractor


class FileExtractor(AbstractExtractor):

    def __init__(self):
        super().__init__()

    def _set_extraction_timestamp(self):
        setattr(self, 'extraction_timestamp', datetime.now())

    def _set_record_source(self):
        pass

    def extract(self):
        self._set_extraction_timestamp()
        self._set_record_source()

    def unify(self):
        pass


class DatabaseExtractor(AbstractExtractor):

    def __init__(self):
        super().__init__()

    def _set_extraction_timestamp(self):
        setattr(self, 'extraction_timestamp', datetime.now())

    def _set_record_source(self):
        pass

    def extract(self):
        self._set_extraction_timestamp()
        self._set_record_source()

    def unify(self):
        pass