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
from . import files_dir
import datetime
import pendulum
from witness.core.batch import Batch
from witness.extractors.http import HttpGetExtractor, JsonHttpGetExtractor
from witness.serializers.http import JsonSerializer
from witness.providers.pandas.loaders import PandasFeatherLoader, PandasExcelLoader
from witness.providers.pandas.extractors import PandasExcelExtractor, PandasFeatherExtractor

xfail = pytest.mark.xfail
parametrize = pytest.mark.parametrize

collect_ignore = ["setup.py", "test_database_extractors.py"]

# region mock

batch_meta = {
    "extraction_timestamp": datetime.datetime(2022, 1, 1, 12, 0, 0, 0),
    "record_source": r"calibration_data",
    "data_interval_end": pendulum.datetime(2022, 2, 2, 13, 5, 0, 0),
}

batch_data = [
    {
        "string": "string_value_1",
        "integer": 31,
        "timestamp": datetime.datetime(2022, 6, 15, 11, 0, 0, 0),
    },
    {
        "string": "string_value_2",
        "integer": 14561,
        "timestamp": datetime.datetime(2001, 4, 13, 12, 0, 0, 0),
    },
    {
        "string": "string_value_3",
        "integer": 7634,
        "timestamp": datetime.datetime(2031, 2, 5, 15, 43, 0, 0),
    },
]

batch_blueprints = [{"data": batch_data, "meta": batch_meta}]

batches = [Batch(data=batch_data, meta=batch_meta)]

dump_uris = [
    f"{files_dir}/test/test_subdir/dump",
    f"{files_dir}/test/test_subdir/test_subdir/dump",
]

file_load_uris = [f"{files_dir}/loads/output_file"]
http_get_uris = [
    {
        "uri": "http://foo-api.com/data",
        "body": '{"success": true}',
        "status": 200,
        "content_type": "text/json",
    },
    {
        "uri": "http://foo-api.com/data",
        "body": '{"success": true}',
        "status": 200,
        "content_type": "text/xml",
    },
]

record_sources = [
    "http://foo-api.com/data",
    "/home/user/file.txt",
    r"C:\User\Documents\config.ini",
    "1C_PowerBI_EX.dbo.VMTP_DC_VesselVoyage",
    "single_file",
    "single_file_with_extension.txt",
    "http://smwhr-web08.hq.moronic.com/api/power-bi/processing",
    r"\\smwhr-fs01\work\Общие файлы\ПЭО\1. Прогнозирование\Планы и факты\2023\План 2023 Бюджет.xlsx",
]

# region extractors
http_extractors = [HttpGetExtractor, JsonHttpGetExtractor]
file_extractors = [
    PandasExcelExtractor(f"{files_dir}/excel_dump.xlsx"),
    PandasFeatherExtractor(f"{files_dir}/feather_dump")
]
# endregion extractors

web_serializers = [JsonSerializer]

# region loaders
file_loaders = [
    PandasFeatherLoader(f"{files_dir}/feather_dump"),
    PandasExcelLoader(f"{files_dir}/excel_dump.xlsx"),
]
# endregion loaders

# endregion mock


@pytest.fixture(params=batch_blueprints, scope="module")
def fxtr_batch(request):
    batch = Batch(request.param["data"], request.param["meta"])
    yield batch


@pytest.fixture(params=file_loaders)
def fxtr_loader(request):
    yield request.param


@pytest.fixture(params=http_get_uris)
def fxtr_get_uri(request):
    yield request.param


@pytest.fixture(params=http_extractors)
def fxtr_http_extractor(request):
    yield request.param


@pytest.fixture(params=file_extractors)
def fxtr_file_extractor(request):
    yield request.param


@pytest.fixture(params=web_serializers)
def fxtr_web_serializer(request):
    yield request.param


@pytest.fixture(params=file_load_uris)
def fxtr_load_uri(request):
    yield request.param


@pytest.fixture(params=record_sources)
def fxtr_record_source(request):
    yield request.param


@pytest.fixture(params=dump_uris)
def fxtr_dump_uris(request):
    yield request.param
