from dataclasses import dataclass, field

from PIL.Image import Image

from .frame_summary import get_frame_summary, get_cropped_frame_summary
from .modality import Modality
from ..bounding_box import BoundingBox
from ...logging import get_summary


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

    def summary(self, multiline=True):
        return get_summary(self, get_frame_summary, multiline)

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

    def summary(self, multiline=True):
        return get_summary(self, get_cropped_frame_summary, multiline)
