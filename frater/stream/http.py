from queue import Queue
from threading import Thread

from flask import Flask, request, jsonify

from .stream import InputStream


class HTTPInputStream(InputStream):
    def __init__(self, host: str, port: str, stream_type: type):
        super(HTTPInputStream, self).__init__(stream_type)
        self.server = Flask(__name__)
        self.server.logger.disabled = True

        self.host = host
        self.port = port
        self.queue = Queue()
        self.stopped = False
        self.server_thread = None
        
        self._register_endpoint()
        self.run()

    def _register_endpoint(self):
        @self.server.route('/input', methods=['POST'])
        def get_input():
            if request.is_json:
                self.queue.put(request.json)
                return jsonify({'success': True}), 200
            res = jsonify({'success': False})
            return res, 404

    def __next__(self):
        return

    def __iter__(self):
        while not self.stopped:
            while self.queue.empty():
                continue

            yield self.queue.get()

    def run(self):
        self.server_thread = Thread(target=self.server.run, args=(self.host, self.port))
        self.server_thread.start()
