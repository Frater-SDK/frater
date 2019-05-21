from typing import List

from PIL import Image

from frater.components.data_store.image_store import ImageStore
from frater.core import ObjectDetection
from ...stream import OutputStream, InputStream
from ...task import IOTask


class ObjectDetector(IOTask):
    def __init__(self, input_stream: InputStream, output_stream: OutputStream, image_store: ImageStore):
        super(ObjectDetector, self).__init__(input_stream, output_stream)
        self._image_store = image_store

    @property
    def image_store(self):
        return self._image_store

    def run(self):
        for data in self.input_stream:
            image = self.image_store.load_image(data['image_path'])
            detections = self.perform_task(image)
            self.output_stream(detections)

    def perform_task(self, image: Image) -> List[ObjectDetection]:
        raise NotImplementedError
