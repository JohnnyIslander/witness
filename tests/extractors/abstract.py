
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
from witness.extractors.file import ExcelFileExtractor
xfail = pytest.mark.xfail
parametrize = pytest.mark.parametrize

mock_uri = r'.\mock\mock_text.txt'
mock_params = {
    'filename_pattern': '(.)*(text)(.)*'
}


correct_extractor = ExcelFileExtractor(uri=mock_uri, params=mock_params)


@parametrize('args', [
    (mock_uri, mock_params)
])
def test_create_extractor_success(args):
    new_extractor = ExcelFileExtractor(*args)
    return new_extractor


@xfail
@parametrize('args', [
    (1413, ),
    ('rfagre', ),
    ()
])
def test_create_extractor_fail(args):
    new_extractor = ExcelFileExtractor(*args)
    return new_extractor


def test_params_are_iterable():
    for parameter in correct_extractor.params:
        print(parameter)


if __name__ == '__main__':
    pytest.main()
