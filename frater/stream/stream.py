class Stream:
    def __init__(self, stream_type):
        self._stream_type = stream_type

    @property
    def stream_type(self):
        return self._stream_type


class InputStream(Stream):
    def __next__(self):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError


class OutputStream(Stream):
    def send(self, data):
        if type(data) != self.stream_type:
            raise TypeError('Incorrect data type for stream - '
                            'stream type: {} output type: {} output: {}'.format(self.stream_type, type(data), data))

    def __call__(self, data):
        return self.send(data)
