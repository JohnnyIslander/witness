
import pandas as pd
from loaders.abstract import DatabaseLoader


class PandasSQLLoader(DatabaseLoader):
    """
    Loader that uses Pandas DataFrame.to_sql method for loading data.

    :param engine: sqlalchemy engine;
    :param table: name of the destination table;
    :param schema: name of the destination schema, None if not defined.
    """
    def __init__(self, engine, table: str, schema: str or None = None):
        super().__init__()
        self.engine = engine
        self.table = table
        self.schema = schema

    def prepare(self, batch):
        df = pd.DataFrame(batch.data, dtype='str')
        df['extraction_timestamp'] = batch.meta['extraction_timestamp']
        df['record_source'] = batch.meta['record_source']
        self.output = df
        return self

    def load(self):
        self.output.to_sql(name=self.table,
                           con=self.engine,
                           schema=self.schema,
                           if_exists='append',
                           method='multi')
        return self
