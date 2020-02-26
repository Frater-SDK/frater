import json
from dataclasses import dataclass

from .factory import *
from .stream import InputStream, OutputStream, StreamConfig
from ..io import frater_to_json, json_to_frater

__all__ = ['JSONStreamConfig', 'JSONInputStream', 'JSONOutputStream']


@input_stream_configs.register('json')
@output_stream_configs.register('json')
@dataclass
class JSONStreamConfig(StreamConfig):
    filename: str = ''


@input_stream_factory.register('json')
class JSONInputStream(InputStream):
    def __init__(self, config: JSONStreamConfig):
        super(JSONInputStream, self).__init__(config)
        self.input_file = self.open_file()

    def __iter__(self):
        for line in self.input_file:
            yield json_to_frater(json.loads(line.strip()))

    def close(self):
        self.input_file.close()

    def open(self):
        self.input_file = self.open_file()

    def open_file(self):
        return open(self.config.filename, 'r')


@output_stream_factory.register('json')
class JSONOutputStream(OutputStream):
    def __init__(self, config: JSONStreamConfig, data_type: type = None):
        super(JSONOutputStream, self).__init__(config)
        self.output_file = self.open_file()

    def send(self, data):
        json_output = self.get_json_output(data)
        self.output_file.write(json_output)

    def close(self):
        self.output_file.close()

    def open(self):
        self.output_file = self.open_file()

    def open_file(self):
        return open(self.config.filename, 'a')

    @staticmethod
    def get_json_output(data):
        return json.dumps(frater_to_json(data)) + '\n'
