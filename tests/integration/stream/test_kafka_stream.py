import os
import time
from multiprocessing import Process

import pytest
from pytest_docker_compose import NetworkInfo

from frater.stream import KafkaInputStream, KafkaOutputStream
from frater.stream.kafka import KafkaInputStreamConfig, KafkaOutputStreamConfig

pytest_plugins = ["docker_compose"]


@pytest.fixture(scope='function')
def wait_for_kafka(function_scoped_container_getter):
    service: NetworkInfo = function_scoped_container_getter.get('kafka').network_info[0]
    hostname = os.environ['DOCKER_HOST_IP'] if 'DOCKER_HOST_IP' in os.environ else service.hostname
    servers = [f'{hostname}:{service.host_port}']
    return servers


def send_data(data, topic_name, servers):
    output_config = KafkaOutputStreamConfig(topic=topic_name, servers=servers)
    output_stream = KafkaOutputStream(output_config)
    for output_data in data:
        output_stream(output_data)


def receive_data(data, topic_name, servers):
    input_config = KafkaInputStreamConfig(topics=[topic_name], servers=servers)
    input_stream = KafkaInputStream(input_config)
    for i, item in enumerate(input_stream):
        assert item == data[i]
        if i >= len(data) - 1:
            break


# @pytest.mark.skip('Issues with docker-compose')
@pytest.mark.kafka
@pytest.mark.slow
@pytest.mark.docker_compose
def test_kafka_streams(wait_for_kafka):
    count = 10
    data = [{'test': 12345, 'experiment': 'hello_world', 'index': i} for i in range(count)]
    servers = wait_for_kafka
    topic_name = 'kafka_test'
    send = Process(target=send_data, args=(data, topic_name, servers))
    receive = Process(target=receive_data, args=(data, topic_name, servers))

    receive.start()
    time.sleep(0.1)
    send.start()

    receive.join()
