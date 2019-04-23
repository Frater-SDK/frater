from typing import Dict, Tuple

from ..bounding_box import BoundingBox
from ..proto import core

__all__ = ['json_to_bounding_box', 'bounding_box_to_json',
           'diva_format_to_bounding_box',
           'protobuf_to_bounding_box', 'bounding_box_to_protobuf']


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
        'x': bounding_box.x,
        'y': bounding_box.y,
        "w": bounding_box.w,
        "h": bounding_box.h,
        "confidence": bounding_box.confidence,
        "frame_index": bounding_box.frame
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


def protobuf_to_bounding_box(bounding_box: core.BoundingBox) -> BoundingBox:
    return BoundingBox(bounding_box.x, bounding_box.y,
                       bounding_box.w, bounding_box.h,
                       bounding_box.confidence, bounding_box.frame)


def bounding_box_to_protobuf(bounding_box: BoundingBox) -> core.BoundingBox:
    return core.BoundingBox(x=bounding_box.x, y=bounding_box.y,
                            w=bounding_box.w, h=bounding_box.h,
                            confidence=bounding_box.confidence,
                            frame=bounding_box.frame
                            )
