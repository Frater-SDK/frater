from typing import List

from .object import Object
from ..temporal_range import compute_temporal_iou
from ..trajectory import compute_spatiotemporal_iou

__all__ = ['temporally_segment_object', 'objects_have_temporal_overlap', 'objects_have_spatiotemporal_overlap']


def temporally_segment_object(object: Object, window_size: int = 90) -> List[Object]:
    objects = list()
    for i in range(object.start_frame, object.end_frame + 1, window_size):
        start = i
        end = min(i + window_size - 1, object.end_frame)
        objects.append(object[start:end])

    return objects


def objects_have_spatiotemporal_overlap(object: Object, other_object: Object, iou_threshold: float = 0.0) -> bool:
    return compute_spatiotemporal_iou(object.trajectory, other_object.trajectory) > iou_threshold


def objects_have_temporal_overlap(object: Object, other_object: Object, iou_threshold: float = 0.0) -> bool:
    return compute_temporal_iou(object.temporal_range, other_object.temporal_range) > iou_threshold
