from functools import reduce
from typing import List, Union, Tuple

import numpy as np

from frater.utilities.interpolation import lerp
from .bounding_box import BoundingBox

__all__ = ['combine_bounding_boxes', 'compute_spatial_iou', 'linear_interpolate_bounding_boxes',
           'scale_bounding_box', 'convert_descriptors_to_bounding_box']


def combine_bounding_boxes(bounding_boxes: List[BoundingBox]) -> Union[BoundingBox, None]:
    if len(bounding_boxes) > 1:
        return reduce(lambda x, y: x + y, bounding_boxes)
    elif len(bounding_boxes) == 1:
        return bounding_boxes[0]
    else:
        raise IndexError('Not enough bounding boxes to combine. List cannot be empty.')


def compute_spatial_iou(bounding_box: BoundingBox, other_bounding_box: BoundingBox) -> float:
    intersection = bounding_box.intersect(other_bounding_box).area()
    union = bounding_box.area() + other_bounding_box.area() - intersection
    if union <= 0:
        return 0.0

    return intersection / union


def convert_descriptors_to_bounding_box(corners: Tuple[float, float, float, float],
                                        confidence: float, frame_index) -> BoundingBox:
    x_0, y_0, x_1, y_1 = corners
    w, h = x_1 - x_0, y_1 - y_0
    return BoundingBox(x_0, y_0, w, h, confidence, frame_index)


def linear_interpolate_bounding_boxes(bounding_box_0: BoundingBox, bounding_box_1: BoundingBox) -> List[BoundingBox]:
    timesteps = bounding_box_1.frame_index - bounding_box_0.frame_index

    corner_0 = np.array(bounding_box_0.get_corners())
    confidence_0 = bounding_box_0.confidence
    corner_1 = np.array(bounding_box_1.get_corners())
    confidence_1 = bounding_box_1.confidence

    corners = [lerp(corner_0, corner_1, t / timesteps).tolist() for t in range(1, timesteps + 1)]
    corners = [tuple(corner) for corner in corners]
    confidences = [lerp(confidence_0, confidence_1, t / timesteps) for t in range(1, timesteps + 1)]

    return [convert_descriptors_to_bounding_box(corner, confidence, frame_index)
            for corner, confidence, frame_index in
            zip(corners, confidences, range(bounding_box_0.frame_index + 1, bounding_box_1.frame_index))]


def scale_bounding_box(bounding_box: BoundingBox, scale: float = 1.0) -> BoundingBox:
    center = bounding_box.center
    width = bounding_box.width * scale
    height = bounding_box.height * scale
    confidence = bounding_box.confidence
    frame_index = bounding_box.frame_index
    return BoundingBox.init_from_center(center, width, height, confidence, frame_index)
