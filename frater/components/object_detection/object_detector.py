from typing import List, Set

from frater.core import ObjectDetection, Frame, ObjectType
from frater.data_store import FrameStore
from frater.stream import OutputStream, InputStream
from frater.task import IOTask
from frater.utilities.stream import StreamState


class ObjectDetector(IOTask):
    def __init__(self, input_stream: InputStream, output_stream: OutputStream,
                 frame_store: FrameStore, object_types: Set[ObjectType], batch_size: int = 1):
        super(ObjectDetector, self).__init__(input_stream, output_stream)

        self.frame_store = frame_store
        self.object_types = object_types
        self.batch_size = batch_size
        self.current_batch: List[Frame] = list()

    def run(self):
        for data in self.input_stream:
            if type(data) is StreamState and data == StreamState.EOS:
                if len(self.current_batch) > 0:
                    outputs = self.perform_task(self.current_batch)
                    for output in outputs:
                        if output.object_type in self.object_types:
                            self.output_stream(output)
                    self.reset_batch()

                self._active = False
                self.output_stream(data)
            else:
                self._active = True
                frame = self.frame_store.load_image_for_frame(data)
                if frame:
                    self.add_to_batch(frame)
                if self.batch_is_ready():
                    outputs = self.perform_task(self.current_batch)
                    for output in outputs:
                        if output.object_type in self.object_types:
                            self.output_stream(output)
                    self.reset_batch()

    def perform_task(self, frames: List[Frame]) -> List[ObjectDetection]:
        raise NotImplementedError

    def add_to_batch(self, frame: Frame):
        self.current_batch.append(frame)

    def batch_is_ready(self):
        return len(self.current_batch) == self.batch_size

    def reset_batch(self):
        self.current_batch = list()
