from typing import List

from ..bounding_box import BoundingBox, combine_bounding_boxes, linear_interpolate_bounding_boxes
from ..temporal_range import TemporalRange


class Trajectory:
    def __init__(self, bounding_boxes: List[BoundingBox] = None, temporal_range: TemporalRange = None, scale=1.0):
        if bounding_boxes is None:
            bounding_boxes = list()
        if temporal_range is None:
            temporal_range = TemporalRange()

        self.bounding_boxes = bounding_boxes
        self.temporal_range = temporal_range
        self.scale = scale

    def __eq__(self, other: 'Trajectory') -> bool:
        return (self.bounding_boxes == other.bounding_boxes
                and self.temporal_range == other.temporal_range
                and self.scale == other.scale)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.bounding_boxes[item - self.start_frame]
        elif isinstance(item, slice):
            temporal_range = TemporalRange(item.start, item.stop - 1)
            bounding_boxes = self.bounding_boxes[item.start - self.start_frame:item.stop - self.start_frame]
            return Trajectory(bounding_boxes, temporal_range, self.scale)

    def __add__(self, other: 'Trajectory') -> 'Trajectory':
        temporal_range = self.temporal_range.union(other.temporal_range)
        bounding_boxes = list()
        for frame_index in range(temporal_range.start_frame, temporal_range.end_frame + 1):
            current_boxes = list()
            if frame_index in self.temporal_range:
                current_boxes.append(self.bounding_boxes[frame_index - self.start_frame])
            if frame_index in other.temporal_range:
                current_boxes.append(other.bounding_boxes[frame_index - other.start_frame])

            bounding_boxes.append(combine_bounding_boxes(current_boxes))

        return Trajectory(bounding_boxes, temporal_range, self.scale)

    @property
    def start_frame(self) -> int:
        return self.temporal_range.start_frame

    @property
    def end_frame(self) -> int:
        return self.temporal_range.end_frame

    def volume(self):
        return sum(bounding_box.area() for bounding_box in self.bounding_boxes)

    def intersect(self, other: 'Trajectory') -> 'Trajectory':
        temporal_range = self.temporal_range.intersect(other.temporal_range)
        bounding_boxes = list()
        for i in temporal_range:
            bounding_box = self[i]
            other_bounding_box = other[i]
            bounding_boxes.append(bounding_box.intersect(other_bounding_box))

        return Trajectory(bounding_boxes, temporal_range, self.scale)

    def union(self, other: 'Trajectory') -> 'Trajectory':
        return self + other

    def add_bounding_box(self, bounding_box: BoundingBox):
        if len(self.bounding_boxes) > 0:
            end_bounding_box = self.bounding_boxes[-1]
            if end_bounding_box.frame_index >= bounding_box.frame_index:
                raise IndexError('Bounding box frame index less than the last')
            elif end_bounding_box.frame_index + 1 != bounding_box.frame_index:
                self.bounding_boxes.extend(linear_interpolate_bounding_boxes(bounding_box, end_bounding_box))
        self.bounding_boxes.append(bounding_box)
