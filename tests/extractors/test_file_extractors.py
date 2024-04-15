#  Copyright (c) 2023.  Eugene Popov.
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
import os.path

from tests import temp_dir, files_dir
from os import path, getcwd


def test_temp_dir():
    assert 'tests' not in temp_dir


def test_extractor_record_source(fxtr_file_extractor):
    extractor = fxtr_file_extractor
    assert extractor.record_source is None
    extractor.extract()
    print(extractor.record_source)
    assert extractor.record_source is not None


def test_extract(fxtr_file_extractor):
    extractor = fxtr_file_extractor
    print(extractor.uri)
    extractor.extract()


def test_extractor_custom_record_source(fxtr_file_extractor):
    extractor = fxtr_file_extractor
    extractor.extract().set_record_source(record_source='custom_record_source')
    print(extractor.record_source)
    assert extractor.record_source == 'custom_record_source'


def test_extractor_shorten_record_source(fxtr_file_extractor):
    extractor = fxtr_file_extractor
    extractor.extract().set_record_source(shorten=True)
    print(extractor.record_source)
    assert extractor.record_source == os.path.split(extractor.uri)[1]
