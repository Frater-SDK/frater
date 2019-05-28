from .object_type import ObjectType
from ..bounding_box import BoundingBox


class ObjectDetection:
    def __init__(self, object_id: str = '', object_type: ObjectType = ObjectType.NULL, source_image: str = '',
                 bounding_box: BoundingBox = None, confidence: float = 0.0):
        self._object_id = object_id
        self._object_type = object_type
        self._source_image = source_image
        self._bounding_box = bounding_box
        self._confidence = confidence

    @property
    def object_id(self) -> str:
        return self._object_id

    @property
    def object_type(self) -> ObjectType:
        return self._object_type

    @property
    def source_image(self) -> str:
        return self._source_image

    @property
    def bounding_box(self) -> BoundingBox:
        return self._bounding_box

    @property
    def confidence(self) -> float:
        return self._confidence
