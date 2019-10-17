from dataclasses import dataclass, field
from uuid import uuid4

from .object_summary import get_object_detection_summary
from .object_type import ObjectType
from ..bounding_box import BoundingBox
from ...logging import get_summary


@dataclass
class ObjectDetection:
    object_detection_id: str = field(default_factory=lambda: str(uuid4()))
    object_type: ObjectType = field(default=ObjectType.NULL)
    bounding_box: BoundingBox = field(default_factory=BoundingBox)
    source_image: str = ''
    source_video: str = ''
    experiment: str = ''

    @property
    def confidence(self):
        return self.bounding_box.confidence

    @property
    def frame_index(self):
        return self.bounding_box.frame_index

    def summary(self, multiline=True):
        return get_summary(self, get_object_detection_summary, multiline)
