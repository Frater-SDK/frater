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

        self.task_builder = task_builder
        self.task: Union[Task, None] = None
        self.task_thread: Union[Thread, None] = None

        self._register_endpoints()

    def available(self):
        return True

    def start(self):
        if not self.available():
            return {'started': False, 'available': False, 'message': 'task unavailable'}

        if self.started():
            return {'started': True, 'available': True, 'message': 'task already started'}

        self.task = self.task_builder()
        self.task_thread = Thread(target=self.task.run)
        self.task_thread.start()
        return {'started': True, 'available': True, 'message': 'task started'}

    def started(self):
        return bool(self.task and self.task_thread)

    def stop(self):
        if self.task and self.task_thread:
            logger.info('stopping task')
            self.task.stop()
            logger.info('joining thread')
            # self.task_thread.join()

            self.task = None
            self.task_thread = None
            message = 'task stopped'
        else:
            message = 'task not started'

        return {'stopped': True, 'message': message}

    def stopped(self):
        return not self.started()

    def run(self):
        self.server.run(self.host, self.port)

    def _register_endpoints(self):
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
                response=json.dumps(self.start()),
                status=200,
                mimetype='application/json'
            )

        @self.server.route('/started')
        def started():
            return self.server.response_class(
                response=json.dumps({'started': self.started()}),
                status=200,
                mimetype='application/json'
            )

        @self.server.route('/stop')
        def stop():
            return self.server.response_class(
                response=json.dumps(self.stop()),
                status=200,
                mimetype='application/json'
            )

        @self.server.route('/stopped')
        def stopped():
            return self.server.response_class(
                response=json.dumps({'stopped': self.stopped()}),
                status=200,
                mimetype='application/json'
            )


class KafkaTaskServer(TaskServer):
    def __init__(self, host, port, task_builder: Callable[[], Task], kafka_servers):
        super(KafkaTaskServer, self).__init__(host, port, task_builder)
        self.kafka_servers = kafka_servers

    def available(self):
        return kafka_servers_available(self.kafka_servers)
