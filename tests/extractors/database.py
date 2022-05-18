
#  Copyright (c) 2022. Eugene Popov
#  All rights reserved.

import pytest
from extractors.database import ODBCExtractor

xfail = pytest.mark.xfail
parametrize = pytest.mark.parametrize

# region Mock

mock_query_path = r'Z:\scripts\extract\containers\processing\railway\etran_cnt_departure.sql'

connection_keywords = [
            'DRIVER={SQL Server}',
            'SERVER=CARGO-EXPRESS.vmtp.ru',
            'DATABASE=catrw']

mock_connection_string = ';'.join(connection_keywords)
with open(mock_query_path, 'r') as q:
    mock_query = q.read()

mock_extractor = ODBCExtractor(connection_string=mock_connection_string, query=mock_query)

# endregion Mock


def test_new_extractor_output_is_none():
    extractor = ODBCExtractor(connection_string=mock_connection_string, query=mock_query)
    assert extractor.output is None


@xfail
def test_pass_none_query():
    extractor = ODBCExtractor(connection_string=mock_connection_string, query=None)
    extractor.extract()


def test_extractor_unified_output():
    extractor = mock_extractor
    extractor.extract()
    output = extractor.output

    description = output['description']
    col_names = [col[0] for col in description]

    unified_output = extractor.unify().output
    meta = unified_output['meta']
    data = unified_output['data']
    assert isinstance(meta, dict)
    assert isinstance(data, list)

    record_col_names = [name for name in data[0].keys()]
    assert record_col_names == col_names


if __name__ == '__main__':

    pytest.main()


