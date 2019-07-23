from ..bounding_box import bounding_box_defaults
from ..trajectory import trajectory_defaults

OBJECT_JSON_DEFAULT = {
    'object_id': '',
    'object_type': 0,
    'trajectory': trajectory_defaults.TRAJECTORY_JSON_DEFAULT,
    'source_video': '',
    'experiment': '',
    'confidence': 0.0
}

OBJECT_DETECTION_JSON_DEFAULT = {
    'object_detection_id': '',
    'object_type': 0,
    'bounding_box': bounding_box_defaults.BOUNDING_BOX_JSON_DEFAULT,
    'source_image': '',
    'source_video': '',
    'frame_index': 0,
    'experiment': '',
    'confidence': 0.0
}
