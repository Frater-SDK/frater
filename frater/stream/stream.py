from typing import List


class Stream:
    """
    Base Stream class. Only inherited by InputStream and Output Stream
    """

    def __init__(self, stream_type: type = None):
        self._stream_type = stream_type

    @property
    def stream_type(self):
        return self._stream_type

    def close(self):
        pass


class InputStream(Stream):
    def __next__(self):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError


class OutputStream(Stream):
    def send(self, data):
        raise NotImplementedError

    def __call__(self, *args, **kwargs):
        return self.send(*args, **kwargs)


class MultiOutputStream(OutputStream):
    """
    MultiOutputStream allows for multiple output sources
    """

    def __init__(self, output_streams: List[OutputStream] = None, stream_type: type = None):
        super(MultiOutputStream, self).__init__(stream_type)
        if output_streams is None:
            output_streams: List[OutputStream] = list()
        self.output_streams = output_streams

    def send(self, data):
        for output_stream in self.output_streams:
            output_stream.send(data)

    def add_output_stream(self, output_stream: OutputStream):
        self.output_streams.append(output_stream)
