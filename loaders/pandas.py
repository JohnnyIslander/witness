
from core.abstract import AbstractLoader
from loaders.basic import FileLoader
import pandas as pd


class PandasLoader(AbstractLoader):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def prepare(self, batch):
        df = pd.DataFrame(batch.data, dtype='str')
        df['extraction_timestamp'] = batch.meta['extraction_timestamp']
        df['record_source'] = batch.meta['record_source']
        self.output = df
        return self

    def load(self):
        pass


class PandasSQLLoader(PandasLoader):
    """
    Loader that uses Pandas DataFrame.to_sql method for loading data.

    :param engine: sqlalchemy engine;
    :param table: name of the destination table;
    :param schema: name of the destination schema, None if not defined.
    """
    def __init__(self, engine, table: str, schema: str or None = None, **kwargs):
        super().__init__(**kwargs)
        self.engine = engine
        self.table = table
        self.schema = schema

    def load(self):
        self.output.to_sql(name=self.table,
                           con=self.engine,
                           schema=self.schema,
                           if_exists='append',
                           method='multi')
        return self


class PandasExcelLoader(PandasLoader, FileLoader):

    def __init__(self, sheet_name='Sheet1', **kwargs):
        self.sheet_name = sheet_name
        super().__init__(**kwargs)

    def load(self):
        self.output.to_excel(
            excel_writer=self.uri,
            sheet_name=self.sheet_name
        )


class PandasFeatherLoader(PandasLoader, FileLoader):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def load(self):
        self.output.to_feather(self.uri)
