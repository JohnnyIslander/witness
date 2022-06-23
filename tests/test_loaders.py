
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

from tests.test_batch import calibration_meta, calibration_data

xfail = pytest.mark.xfail
parametrize = pytest.mark.parametrize

# region mock
mock_dir = path.abspath('./mock')
files_dir = f'{mock_dir}/files'
calibration_batch = Batch(calibration_data, calibration_meta)


# endregion mock

def test_prepare(new_loader):
    new_loader.prepare(calibration_batch)


@xfail
def test_attach_meta_no_batch(new_loader):
    new_loader.attach_meta()


def test_attach_meta(new_loader):
    new_loader.prepare(calibration_batch).attach_meta()


def test_load(new_loader):
    new_loader.prepare(calibration_batch).load()


if __name__ == '__main__':

    pytest.main()
