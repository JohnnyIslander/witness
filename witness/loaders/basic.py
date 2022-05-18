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

from witness.core.abstract import AbstractLoader


class DatabaseLoader(AbstractLoader):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def prepare(self, batch):
        raise NotImplementedError

    def load(self):
        raise NotImplementedError


class FileLoader(AbstractLoader):

    def __init__(self, uri, **kwargs):
        self.uri: str = uri
        super().__init__(**kwargs)

    def prepare(self, batch):
        raise NotImplementedError

    def load(self):
        raise NotImplementedError
