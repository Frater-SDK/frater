from typing import List

from frater.core import ObjectDetection, Object
from frater.stream import InputStream, OutputStream
from frater.stream.stream_state import StreamState
from frater.task import IOTask

__all__ = ['ObjectTracker']


class ObjectTracker(IOTask):
    def __init__(self, input_stream: InputStream, output_stream: OutputStream):
        super(ObjectTracker, self).__init__(input_stream, output_stream)

    def perform_task(self, detection: ObjectDetection) -> List[Object]:
        """
        :param detection: ObjectDetection
        :return: List[Object]
        """
        raise NotImplementedError

    def run(self):
        for data in self.input_stream:
            if data == StreamState.EOS:
                self._active = False
                self.output_stream(data)
            else:
                for object in self.perform_task(data):
                    self._active = True
                    self.output_stream(object)
