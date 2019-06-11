import json
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
        self.host = host
        self.port = port

        @self.server.route('/available')
        def available():
            return self.server.response_class(
                response=json.dumps({'available': self.available()}),
                status=200,
                mimetype='application/json'
            )

        @self.server.route('/start')
        def start():
            return self.server.response_class(
                response=json.dumps({'started': self.start_task()}),
                status=200,
                mimetype='application/json'
            )

        @self.server.route('/stop')
        def stop():
            return self.server.response_class(
                response=json.dumps({'stopped': self.stop()}),
                status=200,
                mimetype='application/json'
            )

        self.task_builder = task_builder
        self.task: Union[Task, None] = None
        self.task_thread: Union[Thread, None] = None

    def available(self):
        return True

    def start_task(self):
        if not self.available():
            return False

        self.task = self.task_builder()
        self.task_thread = Thread(target=self.task.run)
        self.task_thread.start()
        return True

    def stop(self):
        self.task.stop()
        self.task_thread.join()
        return True

    def run(self):
        self.server.run(self.host, self.port)


class KafkaTaskServer(TaskServer):
    def __init__(self, host, port, task_builder: Callable[[], Task], kafka_servers):
        super(KafkaTaskServer, self).__init__(host, port, task_builder)
        self.kafka_servers = kafka_servers

    def available(self):
        return kafka_servers_available(self.kafka_servers)
