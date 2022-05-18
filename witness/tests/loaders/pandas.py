
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
from witness.loaders import PandasSQLLoader
from core.batch import mock_batch
from sqlalchemy import create_engine

import yaml

xfail = pytest.mark.xfail
parametrize = pytest.mark.parametrize

# region Mock

with open(r'..\mock\connections.yaml', 'r') as stream:
    try:
        conf = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

mock_conn_config = conf['connections']['main_dwh']

mock_host = mock_conn_config['host']
mock_port = mock_conn_config['port']
mock_dialect = mock_conn_config['dialect']
mock_db = mock_conn_config['test']['db']
mock_user = mock_conn_config['test']['user']
mock_pwd = mock_conn_config['test']['password']

mock_dsn = f"{mock_dialect}://" \
           f"{mock_user}:{mock_pwd}" \
           f"@{mock_host}:{mock_port}" \
           f"/{mock_db}"
mock_schema = 'raw_etran'
mock_engine = create_engine(mock_dsn,
                            echo=False)

mock_table = 'cnt_dislocation'

mock_loader = PandasSQLLoader(engine=mock_engine, table=mock_table, schema=mock_schema)

# endregion Mock


def test_prepare():
    mock_loader.prepare(mock_batch)


def test_load():

    mock_loader.prepare(mock_batch).load()


if __name__ == '__main__':

    pytest.main()
