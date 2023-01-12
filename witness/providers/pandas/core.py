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

import pandas as pd
import logging
from typing import Optional
from witness.core.abstract import AbstractLoader

log = logging.getLogger(__name__)


class PandasLoader(AbstractLoader):

    def __init__(self, uri):
        super().__init__(uri)

    def prepare(self, batch):
        super().prepare(batch)
        df = pd.DataFrame(batch.data, dtype='str')
        self.output = df
        return self

    def attach_meta(self, meta_elements: Optional[list[str]] = None):
        try:
            meta = self.batch.meta
        except AttributeError:
            log.exception('No batch object was passed to loader.'
                          'Pass a batch object to "prepare" method first.')
            raise AttributeError('No batch object was passed to loader')
        if meta_elements is None:
            for element in meta:
                self.output[element] = str(getattr(meta, element))
        else:
            for element in meta_elements:
                self.output[element] = str(getattr(meta, element))

        return self

    def load(self):
        raise NotImplementedError
