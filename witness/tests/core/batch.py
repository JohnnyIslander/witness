
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
from witness.core.batch import Batch
from witness.tests import batch

xfail = pytest.mark.xfail
parametrize = pytest.mark.parametrize

# region Mock

mock_struct_empty = batch.struct_empty

mock_batch = Batch(batch.struct_full)

# endregion Mock

@parametrize('args', [
    (batch.struct_empty,),
    (batch.struct_full,)
])
def test_create_batch(args):
    new_batch = Batch(*args)
    return new_batch


@xfail(reason='attribute slots are fixed')
def test_set_new_attr():
    mock_batch.some_attribute = 'test'


def test_batch_load():
    mock_batch.load()


if __name__ == '__main__':
    pytest.main()
