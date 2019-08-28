import logging
import os
import sys
import threading
import time
from uuid import uuid4

import pytest
from pytest_docker_compose import NetworkInfo

from frater.stream import KafkaInputStream, KafkaOutputStream
from frater.utilities.kafka import wait_for_kafka_servers

logger = logging.getLogger('test-kafka-stream')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

pytest_plugins = ["docker_compose"]


@pytest.fixture(scope='function')
def wait_for_kafka(function_scoped_container_getter):
    service: NetworkInfo = function_scoped_container_getter.get('kafka').network_info[0]
    hostname = os.environ['DOCKER_HOST_IP'] if 'DOCKER_HOST_IP' in os.environ else service.hostname
    servers = [f'{hostname}:{service.host_port}']
    wait_for_kafka_servers(servers, sleep=3)
    return servers


@pytest.mark.kafka
@pytest.mark.slow
@pytest.mark.docker_compose
def test_kafka_streams(wait_for_kafka):
    topic_name = str(uuid4())

    input_stream = KafkaInputStream(topic_name, servers=wait_for_kafka)
    output_stream = KafkaOutputStream(topic_name, servers=wait_for_kafka)
    inputs = list()

    t = threading.Thread(target=lambda: inputs.append(next(input_stream)))
    t.start()

    time.sleep(0.5)
    data = {'test': 12345, 'experiment': 'hello_world'}
    output_stream(data)
    t.join(timeout=3)
    assert not t.is_alive()

    received_data = inputs[0]
    assert data == received_data


@pytest.mark.kafka
@pytest.mark.slow
@pytest.mark.docker_compose
def test_kafka_streams_sequence(wait_for_kafka):
    topic_name = str(uuid4())

    input_stream = KafkaInputStream(topic_name, servers=wait_for_kafka)
    output_stream = KafkaOutputStream(topic_name, servers=wait_for_kafka)
    inputs = list()

    count = 10

    def get_data():
        for i, d in enumerate(input_stream):
            inputs.append(d)
            if i + 1 >= count:
                break

    t = threading.Thread(target=get_data)
    t.start()
    # give time to start listening for results
    time.sleep(0.5)
    data = [{'test': 12345, 'experiment': 'hello_world', 'index': i} for i in range(count)]
    for output_data in data:
        output_stream(output_data)
    t.join(timeout=3)
    assert not t.is_alive()

    assert data == inputs
