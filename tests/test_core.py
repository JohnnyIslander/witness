
import pytest
from core.batch import Batch

xfail = pytest.mark.xfail
parametrize = pytest.mark.parametrize

mock_src = {
            'data': [],
            'meta': {}
        }

mock_batch = Batch(mock_src)


@parametrize('args', [
    (mock_src, )
])
def test_create_batch(args):
    new_batch = Batch(*args)
    return new_batch


@xfail(reason='attribute slots are fixed')
def test_set_new_attr():
    mock_batch.some_attribute = 'test'


def test_batch_meta_is_dict():
    new_batch = Batch(mock_src)
    isinstance(new_batch.meta, dict)


def test_batch_data_is_list():
    new_batch = Batch(mock_src)
    isinstance(new_batch.data, list)


if __name__ == '__main__':
    pytest.main()
