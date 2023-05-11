
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

from tests import files_dir, conftest
from witness import MetaData

# region Mock
dump_uri = f'{files_dir}/std_dump'

calibration_meta = conftest.batch_meta
calibration_data = conftest.batch_data
# endregion Mock


def test_info(fxtr_batch):
    print(fxtr_batch.info())


def test_construct_meta(fxtr_batch):
    constructed_meta = MetaData(**calibration_meta)
    assert fxtr_batch.meta == constructed_meta


def test_manual_add_to_meta(fxtr_batch):
    manual_constructed_meta = MetaData()
    for k,v in calibration_meta.items():
        manual_constructed_meta[k] = v
    assert manual_constructed_meta == fxtr_batch.meta


def test_dump(fxtr_batch):
    fxtr_batch.dump(dump_uri)


def test_restore_no_uri(fxtr_batch):
    fxtr_batch.restore()


def test_attached_meta_after_restore(fxtr_batch):
    fxtr_batch.restore(dump_uri)
    assert fxtr_batch.meta.extraction_timestamp == calibration_meta['extraction_timestamp']
    assert fxtr_batch.meta.record_source == calibration_meta['record_source']


def test_persist(fxtr_batch):
    fxtr_batch.dump(dump_uri)
    fxtr_batch.restore()
    assert fxtr_batch.meta.record_source == calibration_meta['record_source']
    assert fxtr_batch.meta.extraction_timestamp == calibration_meta['extraction_timestamp']
    assert fxtr_batch.meta.dump_uri == dump_uri

