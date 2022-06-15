
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
from os import path
from witness import Batch
from witness.loaders.pandas import PandasFeatherLoader, PandasExcelLoader

from witness.tests.core.batch import calibration_meta, calibration_data

xfail = pytest.mark.xfail
parametrize = pytest.mark.parametrize


# region mock
mock_dir = path.abspath('../../../mock')
files_dir = f'{mock_dir}/files'
calibration_batch = Batch(calibration_data, calibration_meta)

mock_params = [
    (PandasFeatherLoader, f'{files_dir}/feather_dump', calibration_batch),
    (PandasExcelLoader, f'{files_dir}/excel_dump.xlsx', calibration_batch)
]


# endregion mock


@parametrize('loader, uri, batch', mock_params)
def test_prepare(loader, uri, batch):
    new_loader = loader(uri)
    new_loader.prepare(batch)


@parametrize('loader, uri, batch', mock_params)
def test_load(loader, uri, batch):
    new_loader = loader(uri)
    new_loader.prepare(batch).load()


if __name__ == '__main__':

    pytest.main()
