
#  Copyright (c) 2022. Eugene Popov
#  All rights reserved.

import pytest
from core.batch import Batch
from tests.mock import batch

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
