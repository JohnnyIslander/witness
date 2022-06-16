
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


from os import path
import pytest
from witness.extractors.pandas import PandasFeatherExtractor, PandasExcelExtractor

xfail = pytest.mark.xfail
parametrize = pytest.mark.parametrize

# region mock
mock_dir = path.abspath('../../mock')
files_dir = f'{mock_dir}/files'
mock_params = [
    (PandasFeatherExtractor, f'{files_dir}/feather_dump'),
    (PandasExcelExtractor, f'{files_dir}/excel_dump.xlsx')
]
# endregion mock


@parametrize('extractor, uri', mock_params)
def test_create(extractor, uri):
    new_extractor = extractor(uri=uri)
    return new_extractor.uri


@parametrize('extractor, uri', mock_params)
def test_extract(extractor, uri):
    new_extractor = extractor(uri=uri)
    new_extractor.extract()


if __name__ == '__main__':

    pytest.main()
