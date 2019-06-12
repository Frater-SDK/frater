from typing import Generator

from frater.components.data_store import FrameStore
from frater.core import ObjectDetection, Object
from frater.stream import InputStream, OutputStream
from frater.task import IOTask

__all__ = ['ObjectTracker']


class ObjectTracker(IOTask):
    def __init__(self, input_stream: InputStream, output_stream: OutputStream, frame_store: FrameStore):
        super(ObjectTracker, self).__init__(input_stream, output_stream)

        self.frame_store = frame_store

    def perform_task(self, detection: ObjectDetection) -> Generator[Object]:
        """
        This method should yield Objects created from ObjectDetections. Depending on how you implement it,
        you may want to keep an ongoing list of object trajectories that each detection could correspond to. You'll also
        need to load the frames from the frame store and then you can crop them with the bounding_box in the detection
        e.g.
        ```
        frame = self.frame_store.get_frame(detection.source_video, detection.bounding_box.index)
        frame = frame.crop(detection.bounding_box)
        ```
        :param detection: ObjectDetection
        :return: Generator[Object]
        """
        raise NotImplementedError

    def run(self):
        for detection in self.input_stream:
            for object in self.perform_task(detection):
                self.output_stream(object)
