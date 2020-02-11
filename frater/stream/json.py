import json

from .stream import InputStream, OutputStream
from ..io import frater_to_json, json_to_frater


class JSONInputStream(InputStream):
    def __init__(self, filename: str, data_type: type = None):
        super(JSONInputStream, self).__init__(data_type)
        self.filename = filename
        self.input_file = self.open_file()

    def __iter__(self):
        for line in self.input_file:
            yield json_to_frater(json.loads(line.strip()))

    def close(self):
        self.input_file.close()

    def open(self):
        self.input_file = self.open_file()

    def open_file(self):
        return open(self.filename, 'r')


class JSONOutputStream(OutputStream):
    def __init__(self, filename, data_type: type = None):
        super(JSONOutputStream, self).__init__(data_type)
        self.filename = filename
        self.output_file = self.open_file()

    def send(self, data):
        json_output = self.get_json_output(data)
        self.output_file.write(json_output)

    def close(self):
        self.output_file.close()

    def open(self):
        self.output_file = self.open_file()

    def open_file(self):
        return open(self.filename, 'a')

    @staticmethod
    def get_json_output(data):
        return json.dumps(frater_to_json(data)) + '\n'
