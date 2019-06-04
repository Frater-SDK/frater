from .stream import InputStream, OutputStream
from ..io import json_to_frater, frater_to_json


class JSONInputStream(InputStream):
    def __init__(self, json_items, stream_type):
        super(JSONInputStream, self).__init__(stream_type)
        self._json_items = json_items

    def __next__(self):
        return next(self._json_items)

    def __iter__(self):
        for item in self._json_items:
            yield json_to_frater(item, self.stream_type)


class JSONOutputStream(OutputStream):
    def __init__(self, stream_type):
        super(JSONOutputStream, self).__init__(stream_type)
        self.outputs = list()

    def send(self, data):
        self.outputs.append(frater_to_json(data, self.stream_type))
