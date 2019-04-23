from .activity import Activity
from .bounding_box import BoundingBox
from .object import Object
from .trajectory import Trajectory

JSON_DEFAULTS = dict()
JSON_DEFAULTS.update({
    BoundingBox: {
        'x': 0.0,
        'y': 0.0,
        'w': 0.0,
        'h': 0.0,
        'confidence': 0.0,
        'frame_index': 0.0
    }})
JSON_DEFAULTS.update({
    'temporal_range': {
        'start_frame': 0,
        'end_frame': 0
    }
})
JSON_DEFAULTS.update({
    Trajectory: {
        'bounding_boxes': [],
        'temporal_range': JSON_DEFAULTS['temporal_range'],
        'scale': 1.0
    }})
JSON_DEFAULTS.update({
    Object: {
        '_id': '',
        'object_type': 0,
        'trajectory': JSON_DEFAULTS[Trajectory]
    }})
JSON_DEFAULTS.update({
    Activity: {
        '_id': '',
        'activity_type': 0,
        'objects': [],
        'trajectory': JSON_DEFAULTS[Trajectory],
        'temporal_range': JSON_DEFAULTS['temporal_range'],
        'source_video': '',
        'experiment': '',
        'confidence': 0.0
    }})