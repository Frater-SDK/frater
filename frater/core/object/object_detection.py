from .object_type import ObjectType
from ..bounding_box import BoundingBox


class ObjectDetection:
    def __init__(self, object_detection_id: str = '', object_type: ObjectType = ObjectType.NULL,
                 bounding_box: BoundingBox = None, source_image: str = '', source_video: str = '',
                 frame_index: int = 0, experiment: str = '', confidence: float = 0.0):
        self.object_detection_id = object_detection_id
        self.object_type = object_type

        if bounding_box is None:
            bounding_box = BoundingBox()
        self.bounding_box = bounding_box
        self.source_image = source_image
        self.source_video = source_video
        self.frame_index = frame_index
        self.experiment = experiment
        self.confidence = confidence
