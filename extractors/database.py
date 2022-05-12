
from extractors.abstract import DatabaseExtractor


def is_select(q: str) -> bool:
    return True if 'select' in str.lower(q) else False


class ODBCExtractor(DatabaseExtractor):

    def __init__(self, connection_string: str, query: str):

        super().__init__()
        self.connection_string: str = connection_string
        self.query: str = query if isinstance(query, str) and is_select(query) else None

    def _set_extraction_timestamp(self):
        from datetime import datetime
        setattr(self, 'extraction_timestamp', datetime.now())

    def extract(self):
        from pyodbc import connect

        connector = connect(self.connection_string)
        cursor = connector.cursor()
        records = cursor.execute(self.query).fetchall()
        description = cursor.description

        self._set_extraction_timestamp()
        self.output = {'description': description, 'records': records}

        return self

    def unify(self):

        description = self.output['description']
        records = self.output['records']

        data = []
        col_names = [col[0] for col in description]

        for record in records:
            raw = {}
            for i, value in enumerate(record):
                raw[col_names[i]] = value
            data.append(raw)

        meta = {}
        dtypes = [col[1] for col in description]
        source_dtypes = {}
        for i, value in enumerate(dtypes):
            source_dtypes[col_names[i]] = value

        meta['extraction_timestamp'] = self.extraction_timestamp
        meta['source_dtypes'] = source_dtypes

        setattr(self, 'output', {'meta': meta, 'data': data})

        return self
