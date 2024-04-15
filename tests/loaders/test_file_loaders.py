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

import pytest
import json
from witness.loaders import JSONFileLoader
from witness.serializers.common import CustomJSONEncoder

xfail = pytest.mark.xfail


def test_prepare(fxtr_batch, fxtr_load_uri):
    loader = JSONFileLoader(uri=fxtr_load_uri)
    print(fxtr_batch.data)
    json_fxtr_batch_data = json.dumps(fxtr_batch.data, cls=CustomJSONEncoder)
    print(json_fxtr_batch_data)
    loader.prepare(batch=fxtr_batch)
    assert loader.output == json_fxtr_batch_data
