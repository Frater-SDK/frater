from typing import List

from frater.core import ObjectDetection, Frame
from frater.data_store import FrameStore
from frater.stream.stream_state import StreamState
from ...stream import OutputStream, InputStream
from ...task import IOTask


class ObjectDetector(IOTask):
    def __init__(self, input_stream: InputStream, output_stream: OutputStream, frame_store: FrameStore):
        super(ObjectDetector, self).__init__(input_stream, output_stream)

        self.frame_store = frame_store

    def run(self):
        for data in self.input_stream:
            if data == StreamState.EOS:
                self._active = False
                self.output_stream(data)
            else:
                self._active = True
                frame = self.frame_store.load_image_for_frame(data)
                for detection in self.perform_task(frame):
                    self.output_stream(detection)

    def perform_task(self, frame: Frame) -> List[ObjectDetection]:
        raise NotImplementedError
