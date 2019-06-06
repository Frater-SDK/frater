import logging
import time

from kafka import KafkaAdminClient
from kafka.errors import NoBrokersAvailable

logger = logging.getLogger()


def wait_for_servers(servers):
    logger.info(f'waiting for servers: {servers}')
    unavailable = True
    while unavailable:
        unavailable = False
        try:
            client = KafkaAdminClient(bootstrap_servers=servers)
            client.close()
        except NoBrokersAvailable:
            unavailable = True
        logging.info(f'Hosts: {", ".join(servers)}, Available: {not unavailable}')
        if unavailable:
            time.sleep(4)
