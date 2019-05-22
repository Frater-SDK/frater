from typing import List

from .object import Object

__all__ = ['temporally_segment_object']


def temporally_segment_object(object: Object, window_size: int = 90) -> List[Object]:
    objects = list()
    for i in range(object.start_frame, object.end_frame + 1, window_size):
        start = i
        end = min(i + window_size, object.trajectory.end_frame + 1)
        objects.append(object[start:end])

    return objects
