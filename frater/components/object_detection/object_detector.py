from typing import List

from frater.components.data_store import FrameStore
from frater.core import ObjectDetection, Frame
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

    @FrameStore.instance.load_image_for_frame()
    def perform_task(self, frame: Frame) -> List[ObjectDetection]:
        raise NotImplementedError
