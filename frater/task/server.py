import logging
import time
from typing import Callable

import flask

from .task import Task
from ..utilities.kafka import kafka_servers_available

logger = logging.getLogger()


class TaskServer:
    def __init__(self, host, port, task_builder: Callable[[], Task]):
        self.server = flask.Flask(__name__)

        self.server.route('/available')(lambda: {'available': self.available()})
        self.task_builder = task_builder

        self.server.run(host, port)

    def available(self):
        return True

    def start_task(self):
        while not self.available():
            logger.info('Task not available yet')
            time.sleep(4)

        task = self.task_builder()
        task.run()


class KafkaTaskServer(TaskServer):
    def __init__(self, host, port, task_builder: Callable[[], Task], kafka_servers):
        super(KafkaTaskServer, self).__init__(host, port, task_builder)
        self.kafka_servers = kafka_servers

    def available(self):
        return kafka_servers_available(self.kafka_servers)
