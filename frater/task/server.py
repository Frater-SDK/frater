import logging
from threading import Thread
from typing import Callable, Union

import flask

from .task import Task
from ..utilities.kafka import kafka_servers_available

logger = logging.getLogger()


class TaskServer:
    def __init__(self, host, port, task_builder: Callable[[], Task]):
        self.server = flask.Flask(__name__)

        self.server.route('/available')(lambda: flask.jsonify({'available': self.available()}))
        self.server.route('/start')(lambda: {'started': flask.jsonify({'started': self.start_task()})})
        self.task_builder = task_builder

        self.server.run(host, port)

        self.task: Union[Task, None] = None
        self.task_thread: Union[Thread, None] = None

    def available(self):
        return True

    def start_task(self):
        if not self.available():
            return False

        self.task = self.task_builder()
        self.task_thread = Thread(target=self.task.run, daemon=True)
        self.task_thread.start()

        return True


class KafkaTaskServer(TaskServer):
    def __init__(self, host, port, task_builder: Callable[[], Task], kafka_servers):
        super(KafkaTaskServer, self).__init__(host, port, task_builder)
        self.kafka_servers = kafka_servers

    def available(self):
        return kafka_servers_available(self.kafka_servers)
