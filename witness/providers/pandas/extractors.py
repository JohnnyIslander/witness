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
from typing import Optional, Union
from witness.providers.pandas.core import PandasExtractor

log = logging.getLogger(__name__)


class PandasFeatherExtractor(PandasExtractor):
    def extract(self):
        df = pd.read_feather(self.uri)
        setattr(self, "output", df)
        super().extract()

        return self


class PandasExcelExtractor(PandasExtractor):
    def __init__(self, uri, sheet_name=0, header=0, dtype=None):
        self.sheet_name: str or int or None = sheet_name
        self.header: int = header
        self.dtype: str or dict or None = dtype
        super().__init__(uri)

    def extract(self):
        df = pd.read_excel(
            self.uri, sheet_name=self.sheet_name, header=self.header, dtype=self.dtype
        )
        setattr(self, "output", df)
        super().extract()

        return self


class PandasSQLExtractor(PandasExtractor):
    def __init__(self,
                 engine,
                 query: str,
                 index_col: Optional[str] = None,
                 params: Optional[dict] = None,
                 table: Optional[str] = None,
                 schema: Optional[str] = None,
                 columns: Optional[list] = None,
                 dtype: Union[str, dict, None] = None
                 ):
        self.engine = engine
        self.query = query if query else table if table else 'select null'
        self.index_col = index_col
        self.params = params
        self.schema = schema
        self.table = table if self.schema is None else f'{self.schema}.{table}'
        self.columns = columns
        self.dtype = dtype
        uri = f"{engine.url.database}.{schema}.{table}"
        super().__init__(uri)

    def extract(self):
        conn = self.engine.connect()
        df = pd.read_sql(
            sql=self.query,
            con=conn,
            index_col=self.index_col,
            params=self.params,
            columns=self.columns,
            # dtype=self.dtype only in pandas >= 2.0
        )
        setattr(self, "output", df)
        super().extract()

        return self
