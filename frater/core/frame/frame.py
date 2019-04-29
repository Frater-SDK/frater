from typing import Tuple

from PIL.Image import Image

from .modality import Modality


class Frame:
    def __init__(self, image: Image = None, modality: Modality = Modality.RGB,
                 index: int = 0, source_video: str = '', ):
        self._image = image
        self._modality = modality
        self._index = index
        self._source_video = source_video

    @property
    def image(self) -> Image:
        return self._image

    @property
    def modality(self) -> Modality:
        return self._modality

    @property
    def index(self) -> int:
        return self._index

    @property
    def source_video(self) -> str:
        return self._source_video

    @property
    def width(self):
        return self.image.width

    @property
    def height(self):
        return self.image.height

    def crop(self, x: float, y: float, width: float, height: float) -> 'CroppedFrame':
        location = x, y, x + width, y + height
        image = self.image.crop(location)
        return CroppedFrame(image, location, self.modality, self.index, self.source_video)


class CroppedFrame(Frame):
    def __init__(self, image: Image = None, source_location: Tuple[float, float, float, float] = None,
                 modality: Modality = Modality.RGB, index: int = 0, source_video: str = ''):
        super(CroppedFrame, self).__init__(image, modality, index, source_video)

        self._source_location = source_location

    @property
    def source_location(self):
        return self._source_location
