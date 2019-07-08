from PIL.Image import Image

from frater.core import BoundingBox
from .modality import Modality


class Frame:
    def __init__(self, image: Image = None, modality: Modality = Modality.RGB,
                 index: int = 0, source_video: str = '', experiment: str = '', timestamp: str = ''):
        self.image = image
        self.modality = modality
        self.index = index
        self.source_video = source_video
        self.experiment = experiment
        self.timestamp = timestamp

    @property
    def width(self):
        if self.image:
            return self.image.width
        return None

    @property
    def height(self):
        if self.image:
            return self.image.height
        return None

    def crop(self, bounding_box: BoundingBox) -> 'CroppedFrame':
        location = bounding_box.get_corners()
        if self.image:
            image = self.image.crop(location)
        else:
            image = None
        return CroppedFrame(image, bounding_box, self.modality, self.index,
                            self.source_video, self.experiment, self.timestamp)


class CroppedFrame(Frame):
    def __init__(self, image: Image = None, source_location: BoundingBox = None,
                 modality: Modality = Modality.RGB, index: int = 0, source_video: str = '',
                 experiment: str = '', timestamp: str = ''):
        super(CroppedFrame, self).__init__(image, modality, index, source_video, experiment, timestamp)

        self.source_location = source_location
