import logging
import time

from kafka import KafkaClient

logger = logging.getLogger()


def wait_for_kafka_servers(servers, max_retries=10, sleep=1):
    logger.info(f'waiting for servers: {servers}')
    for _ in range(max_retries):
        available = kafka_servers_available(servers)
        logging.info(f'Hosts: {", ".join(servers)}, Available: {available}')
        if available:
            break
        time.sleep(sleep)
    else:
        raise ConnectionError(f'Failed to connect to Kafka Servers {servers}. Attempted max retries.')


def kafka_servers_available(servers):
    try:
        client = KafkaClient(bootstrap_servers=servers)
        client.close()
    except Exception:
        return False
    return True


def end_of_sequence(headers):
    return bool(headers['EOS'])
