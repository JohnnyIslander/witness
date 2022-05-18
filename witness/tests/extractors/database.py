
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

import pytest
from witness.extractors import ODBCExtractor

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


