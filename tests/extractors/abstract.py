
#  Copyright (c) 2022. Eugene Popov
#  All rights reserved.

import pytest
from extractors.file import ExcelFileExtractor
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
