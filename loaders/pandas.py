
from loaders.abstract import DatabaseLoader
from sqlalchemy.types import String
import pandas as pd


class PandasSQLLoader(DatabaseLoader):

    def __init__(self, engine, table: str, schema: str or None = None):
        super().__init__()
        self.engine = engine
        self.table = table
        self.schema = schema

    def prepare(self, batch):
        df = pd.DataFrame(batch.data)
        df['extraction_timestamp'] = batch.meta['extraction_timestamp']
        df['record_source'] = batch.meta['record_source']
        self.output = df
        return self

    def load(self):
        self.output.to_sql(name=self.table,
                           con=self.engine,
                           schema=self.schema,
                           if_exists='append',
                           dtype=String,
                           method='multi')

