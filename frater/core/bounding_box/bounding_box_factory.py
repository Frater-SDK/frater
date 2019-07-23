from typing import Dict, Tuple

from .bounding_box import BoundingBox
from .bounding_box_defaults import BOUNDING_BOX_JSON_DEFAULT
from ...validation.json import validate_json

__all__ = ['json_to_bounding_box', 'bounding_box_to_json',
           'diva_format_to_bounding_box']


@validate_json(default=BOUNDING_BOX_JSON_DEFAULT, completion=True)
def json_to_bounding_box(bounding_box: Dict) -> BoundingBox:
    x = bounding_box['x']
    y = bounding_box['y']
    w = bounding_box['w']
    h = bounding_box['h']
    confidence = bounding_box['confidence']
    frame_index = bounding_box['frame_index']

    return BoundingBox(x, y, w, h, confidence, frame_index)


def bounding_box_to_json(bounding_box: BoundingBox) -> Dict:
    return {
        'data_type': 'bounding_box',
        'x': bounding_box.x,
        'y': bounding_box.y,
        "w": bounding_box.w,
        "h": bounding_box.h,
        'confidence': bounding_box.confidence,
        'frame_index': bounding_box.frame_index
    }


def diva_format_to_bounding_box(bounding_box: Tuple[str, Dict]) -> BoundingBox:
    frame_index, data = bounding_box
    frame_index = int(frame_index)
    x = data['boundingBox']['x']
    y = data['boundingBox']['y']
    w = data['boundingBox']['w']
    h = data['boundingBox']['h']
    confidence = data['presenceConf']
    return BoundingBox(x, y, w, h, confidence, frame_index)
