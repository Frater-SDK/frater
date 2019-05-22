from functools import reduce
from typing import List, Union

from .bounding_box import BoundingBox

__all__ = ['combine_bounding_boxes', 'compute_spatial_iou']


def combine_bounding_boxes(bounding_boxes: List['BoundingBox']) -> Union['BoundingBox', None]:
    if len(bounding_boxes) > 1:
        return reduce(lambda x, y: x + y, bounding_boxes)
    elif len(bounding_boxes) == 1:
        return bounding_boxes[0]
    else:
        return None


def compute_spatial_iou(bounding_box: BoundingBox, other_bounding_box: BoundingBox) -> float:
    intersection = bounding_box.intersect(other_bounding_box).area()
    union = bounding_box.area() + other_bounding_box.area() - intersection
    if union <= 0:
        return 0.0

    return intersection / union
