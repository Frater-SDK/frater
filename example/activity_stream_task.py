from copy import deepcopy

from frater.core import Activity
from frater.stream import InputStream, OutputStream
from frater.task import Task


class ActivityIdTask(Task):
    def __init__(self, input_stream: InputStream, output_stream: OutputStream):
        super(ActivityIdTask, self).__init__()
        self._input_stream = input_stream
        self._output_stream = output_stream

    @property
    def input_stream(self):
        return self._input_stream

    @property
    def output_stream(self):
        return self._output_stream

    def validate(self):
        pass

    def run(self):
        for activity in self._input_stream:
            output = self.perform_task(activity)
            self.output_stream(output)

    def perform_task(self, activity: Activity) -> Activity:
        output = deepcopy(activity)
        output._activity_id = 'test1234'


class MyInputStream(InputStream):
    def __init__(self, stream_type):
        super().__init__(stream_type)
        self.activities = [Activity()] * 5

    def __next__(self) -> Activity:
        return next(self.activities)

    def __iter__(self):
        for activity in self.activities:
            yield activity


class MyOutputStream(OutputStream):
    pass


def main():
    task = ActivityIdTask(MyInputStream(), MyOutputStream())


if __name__ == '__main__':
    main()
