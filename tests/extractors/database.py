
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

# endregion Mock


def test_create_extractor():
    extractor = ODBCExtractor(connection_string=mock_connection_string, query=mock_query)
    return extractor


def test_new_extractor_output_is_none():
    extractor = ODBCExtractor(connection_string=mock_connection_string, query=mock_query)
    assert extractor.output is None


def test_extractor_unified_output():
    extractor = ODBCExtractor(connection_string=mock_connection_string, query=mock_query)
    output = extractor.extract().unify().output
    meta = output['meta']
    data = output['data']

    assert isinstance(meta, dict)
    assert isinstance(data, list)


if __name__ == '__main__':

    pytest.main()


