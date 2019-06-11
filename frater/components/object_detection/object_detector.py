from typing import List

from PIL import Image

from frater.components.data_store import FrameStore
from frater.core import ObjectDetection
from ...stream import OutputStream, InputStream
from ...task import IOTask


class ObjectDetector(IOTask):
    def __init__(self, input_stream: InputStream, output_stream: OutputStream, frame_store: FrameStore):
        super(ObjectDetector, self).__init__(input_stream, output_stream)

        self.frame_store = frame_store

    def run(self):
        for frame in self.input_stream:
            for detection in self.perform_task(frame):
                self.output_stream(detection)

    def perform_task(self, image: Image) -> List[ObjectDetection]:
        raise NotImplementedError
