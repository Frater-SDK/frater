from .object_type import ObjectType
from ..bounding_box import BoundingBox


class ObjectDetection:
    def __init__(self, object_id: str = '', object_type: ObjectType = ObjectType.NULL, source_image: str = '',
                 bounding_box: BoundingBox = None, confidence: float = 0.0):
        self.object_id = object_id
        self.object_type = object_type
        self.source_image = source_image
        self.bounding_box = bounding_box
        self.confidence = confidence
