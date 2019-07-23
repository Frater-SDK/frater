from dataclasses import dataclass, field

from PIL.Image import Image

from frater.core import BoundingBox
from .modality import Modality


@dataclass
class Frame:
    image: Image = field(default_factory=Image)
    modality: Modality = field(default=Modality.RGB)
    index: int = 0
    source_video: str = ''
    experiment: str = ''
    timestamp: str = ''

    @property
    def width(self):
        return self.image.width

    @property
    def height(self):
        return self.image.height

    def crop(self, bounding_box: BoundingBox) -> 'CroppedFrame':
        location = bounding_box.get_corners()
        if self.image:
            image = self.image.crop(location)
        else:
            image = None
        return CroppedFrame(image, self.modality, self.index, self.source_video,
                            self.experiment, self.timestamp, bounding_box)


@dataclass
class CroppedFrame(Frame):
    source_location: BoundingBox = field(default_factory=BoundingBox)
