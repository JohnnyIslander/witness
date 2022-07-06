
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

from tests import files_dir
import datetime

# region Mock
dump_uri = f'{files_dir}/std_dump'

calibration_meta = {
    'extraction_timestamp': datetime.datetime(2022, 1, 1, 12, 0, 0, 0),
    'record_source': r'calibration_data',
    'tags': ['debug', 'snapshot']
}

calibration_data = [
    {'string': 'string_value_1', 'integer': 31, 'timestamp': datetime.datetime(2022, 6, 15, 11, 0, 0, 0)},
    {'string': 'string_value_2', 'integer': 14561, 'timestamp': datetime.datetime(2001, 4, 13, 12, 0, 0, 0)},
    {'string': 'string_value_3', 'integer': 7634, 'timestamp': datetime.datetime(2031, 2, 5, 15, 43, 0, 0)}
]

# endregion Mock


def test_info(fxtr_batch):
    print(fxtr_batch.info())


def test_dump(fxtr_batch):
    fxtr_batch.dump(dump_uri)


def test_restore_no_uri(fxtr_batch):
    fxtr_batch.restore()


def test_attached_meta_after_restore(fxtr_batch):
    fxtr_batch.restore(dump_uri)
    assert fxtr_batch.meta['extraction_timestamp'] == calibration_meta['extraction_timestamp']
    assert fxtr_batch.meta['record_source'] == calibration_meta['record_source']


def test_persist(fxtr_batch):
    fxtr_batch.dump(dump_uri)
    fxtr_batch.restore()
    assert fxtr_batch.meta['record_source'] == calibration_meta['record_source']
    assert fxtr_batch.meta['extraction_timestamp'] == calibration_meta['extraction_timestamp']
