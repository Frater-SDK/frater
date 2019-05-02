from frater.stream import InputStream, OutputStream
from frater.task import Task


class MockValidationType:
    def __init__(self):
        self.value = 'test'


class OtherMockValidationType:
    def __init__(self):
        self.value = 'other'


class MockValidationTask(Task):
    def __init__(self, input_type, output_type):
        super(MockValidationTask, self).__init__(input_type, output_type)

    def run(self):
        pass

    def perform_task(self, data):
        pass


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
