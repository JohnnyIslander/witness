

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

import httpretty

httpretty.enable(verbose=True, allow_net_connect=False)


@httpretty.activate
def test_extract(fxtr_http_extractor, fxtr_get_uri):

    httpretty.register_uri(
        method=httpretty.GET,
        uri=fxtr_get_uri['uri'],
        body=fxtr_get_uri['body'],
        status=fxtr_get_uri['status'],
        content_type=fxtr_get_uri['content_type']
    )

    extractor = fxtr_http_extractor(uri=fxtr_get_uri['uri'])
    extractor.extract()

@httpretty.activate
def test_serialize_to_batch(fxtr_http_extractor, fxtr_get_uri, fxtr_web_serializer):
    serializer = fxtr_web_serializer()
    httpretty.register_uri(
        method=httpretty.GET,
        uri=fxtr_get_uri['uri'],
        body=fxtr_get_uri['body'],
        status=fxtr_get_uri['status'],
        content_type=fxtr_get_uri['content_type']
    )
    extractor = fxtr_http_extractor(uri=fxtr_get_uri['uri'], serializer=serializer)
    serialized_output = extractor.extract().unify().output
    print(f'Raw output: {extractor.output}')
    assert serialized_output['data'] == {'success': True}


@httpretty.activate
def test_unify(fxtr_http_extractor, fxtr_get_uri):

    httpretty.register_uri(
        method=httpretty.GET,
        uri=fxtr_get_uri['uri'],
        body=fxtr_get_uri['body'],
        status=fxtr_get_uri['status'],
        content_type=fxtr_get_uri['content_type']
    )
    extractor = fxtr_http_extractor(uri=fxtr_get_uri['uri'])
    extractor.extract().unify()
