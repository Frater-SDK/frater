from dataclasses import dataclass
from typing import List

from ..config import Config


@dataclass
class StreamConfig(Config):
    data_type: str = ''


class Stream:
    """
    Base Stream class. Only inherited by InputStream and Output Stream
    """

    def __init__(self, config: StreamConfig = None):
        self.config = config

    @property
    def data_type(self):
        return self.config.data_type

    def close(self):
        pass


class InputStream(Stream):
    def __init__(self, data_type=None):
        super(InputStream, self).__init__(data_type)

    def __iter__(self):
        raise NotImplemented


class OutputStream(Stream):
    def send(self, data):
        raise NotImplemented

    def __call__(self, *args, **kwargs):
        return self.send(*args, **kwargs)


class MultiOutputStream(OutputStream):
    """
    MultiOutputStream allows for multiple output sources
    """

    def __init__(self, output_streams: List[OutputStream] = None, data_type: type = None):
        super(MultiOutputStream, self).__init__(data_type)
        if output_streams is None:
            output_streams: List[OutputStream] = list()
        self.output_streams = output_streams

    def send(self, data):
        for output_stream in self.output_streams:
            output_stream.send(data)

    def add_output_stream(self, output_stream: OutputStream):
        self.output_streams.append(output_stream)
