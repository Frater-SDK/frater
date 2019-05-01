from typing import List

from frater.core.temporal_range import TemporalRange
from ..bounding_box import BoundingBox


class Trajectory:
    def __init__(self, bounding_boxes: List[BoundingBox] = None, temporal_range: TemporalRange = None, scale=1.0):
        if bounding_boxes is None:
            bounding_boxes = list()
        if temporal_range is None:
            temporal_range = TemporalRange()

        self._bounding_boxes = bounding_boxes
        self._temporal_range = temporal_range
        self._scale = scale

    def __eq__(self, other: 'Trajectory') -> bool:
        return (self.bounding_boxes == other.bounding_boxes
                and self.temporal_range == other.temporal_range
                and self.scale == other.scale)

    @property
    def bounding_boxes(self) -> List[BoundingBox]:
        return self._bounding_boxes

    @property
    def temporal_range(self) -> TemporalRange:
        return self._temporal_range

    @property
    def scale(self) -> float:
        return self._scale

    @property
    def start_frame(self) -> int:
        return self.temporal_range.start_frame

    @property
    def end_frame(self) -> int:
        return self.temporal_range.end_frame
