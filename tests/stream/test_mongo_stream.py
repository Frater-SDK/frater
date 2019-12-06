import os
from uuid import uuid4

import pytest
from pytest_docker_compose import NetworkInfo

from frater.stream.mongo import MongoOutputStream, MongoStreamConfig, MongoInputStream


@pytest.fixture(scope='function')
def wait_for_mongo(function_scoped_container_getter):
    service: NetworkInfo = function_scoped_container_getter.get('mongo').network_info[0]
    hostname = os.environ['DOCKER_HOST_IP'] if 'DOCKER_HOST_IP' in os.environ else service.hostname
    return hostname, int(service.host_port)


@pytest.mark.skip('Issues with docker-compose')
@pytest.mark.mongo
@pytest.mark.slow
@pytest.mark.docker_compose
def test_mongo_stream(wait_for_mongo):
    host, port = wait_for_mongo
    collection = str(uuid4())
    test_id = str(uuid4())

    config = MongoStreamConfig(host, port, collection=collection, filter={'test_id': test_id})

    data = {'test_id': test_id, 'example_data': 12345}
    output_stream = MongoOutputStream(config)
    input_stream = MongoInputStream(config)

    print(data)
    output_stream(data)
    input_data = next(input_stream)
    print(data)
    print(input_data)
    assert data == input_data

    # cleanup
    output_stream.db.drop_collection(collection)
