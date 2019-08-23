import logging
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
    servers = [f'{service.hostname}:{service.host_port}']
    print(servers)
    wait_for_kafka_servers(servers, sleep=3)
    return servers


def test_kafka_streams(wait_for_kafka):
    topic_name = str(uuid4())

    input_stream = KafkaInputStream(topic_name, servers=wait_for_kafka)
    output_stream = KafkaOutputStream(topic_name, servers=wait_for_kafka)
    inputs = list()

    def get_data():
        inputs.append(next(input_stream))

    t = threading.Thread(target=get_data)
    t.start()

    time.sleep(1)
    data = {'test': 12345, 'experiment': 'hello_world'}
    output_stream(data)
    t.join()
    received_data = inputs[0]
    assert data == received_data
