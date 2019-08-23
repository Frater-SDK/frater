from frater.stream import InputStream, OutputStream


class MockValidationInputStream(InputStream):
    def __init__(self, stream_type):
        super(MockValidationInputStream, self).__init__(stream_type)

    def __next__(self):
        pass

    def __iter__(self):
        pass


class MockValidationOutputStream(OutputStream):
    def __init__(self, stream_type):
        super(MockValidationOutputStream, self).__init__(stream_type)

    def send(self, data):
        pass
