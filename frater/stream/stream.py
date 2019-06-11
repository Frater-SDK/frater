class Stream:
    def __init__(self, stream_type: type):
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

    def __call__(self, data):
        return self.send(data)
