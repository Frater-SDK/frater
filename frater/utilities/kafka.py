import logging
import time

from kafka import KafkaAdminClient

logger = logging.getLogger()


def wait_for_kafka_servers(servers):
    logger.info(f'waiting for servers: {servers}')
    unavailable = True
    while unavailable:
        unavailable = not kafka_servers_available(servers)
        logging.info(f'Hosts: {", ".join(servers)}, Available: {not unavailable}')
        if unavailable:
            time.sleep(4)


def kafka_servers_available(servers):
    try:
        client = KafkaAdminClient(bootstrap_servers=servers)
        client.close()
    except Exception:
        return False
    return True


def end_of_sequence(headers):
    return bool(headers['EOS'])
