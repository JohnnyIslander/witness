
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

from witness.core.abstract import AbstractExtractor
from datetime import datetime
import pandas as pd


class PandasExtractor(AbstractExtractor):
    """
    Basic pandas extractor class.
    Provides a single 'unify' method for all child pandas extractors.
    """
    def __init__(self, uri, **kwargs):
        super().__init__(uri)

    def _set_extraction_timestamp(self):
        setattr(self, 'extraction_timestamp', datetime.now())

    def extract(self):
        self._set_extraction_timestamp()

    def unify(self):

        data = self.output.to_dict(orient='records')
        meta = {'extraction_timestamp': self.extraction_timestamp,
                'record_source': self.uri}

        setattr(self, 'output', {'meta': meta, 'data': data})

        return self


class PandasFeatherExtractor(PandasExtractor):

    def __init__(self, uri, **kwargs):
        self.uri: str = uri
        super().__init__(uri, **kwargs)

    def extract(self):
        df = pd.read_feather(self.uri)
        setattr(self, 'output', df)
        super().extract()

        return self
