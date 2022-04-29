import pytest
from core.batch import Batch

mock_batch = {
            'data': [],
            'meta': {}
        }


class TestBatch:

    def test_new_batch_is_not_empty(self):

        new_batch = Batch(mock_batch)
        assert new_batch.data is not None and new_batch.meta is not None

    def test_batch_meta_is_dict(self):
        new_batch = Batch(mock_batch)
        isinstance(new_batch.meta, dict)

    def test_batch_data_is_list(self):
        new_batch = Batch(mock_batch)
        isinstance(new_batch.data, list)


if __name__ == '__main__':
    pytest.main()
