
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

    def _set_record_source(self):
        setattr(self, 'record_source', self.connection_string)

    def extract(self):
        from pyodbc import connect

        connector = connect(self.connection_string)
        cursor = connector.cursor()
        rows = cursor.execute(self.query).fetchall()

        self.output = {'description': cursor.description, 'rows': rows}
        super().extract()

        return self

    def unify(self):

        description = self.output['description']
        rows = self.output['rows']
        col_names = [col[0] for col in description]
        dtypes = [col[1] for col in description]
        source_dtypes = {col_names[i]: dtype for i, dtype in enumerate(dtypes)}

        def build_record(names, row):
            record = {names[i]: value for i, value in enumerate(row)}
            return record

        data = [build_record(col_names, row) for row in rows]
        meta = {'extraction_timestamp': self.extraction_timestamp,
                'record_source': self.record_source,
                'source_dtypes': source_dtypes}

        setattr(self, 'output', {'meta': meta, 'data': data})

        return self
