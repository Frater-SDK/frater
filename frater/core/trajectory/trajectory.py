from dataclasses import dataclass, field
from typing import List, Union

from .trajectory_summary import get_trajectory_summary
from ..bounding_box import BoundingBox, combine_bounding_boxes, linear_interpolate_bounding_boxes
from ..temporal_range import TemporalRange
from ...logging import get_summary


@dataclass
class Trajectory:
    bounding_boxes: List[BoundingBox] = field(default_factory=list)

    def __init__(self, bounding_boxes: List[BoundingBox] = None, **kwargs):
        super(Trajectory, self).__init__(**kwargs)
        if bounding_boxes is None:
            bounding_boxes = list()

        self.bounding_boxes = list()
        for bounding_box in bounding_boxes:
            self.add_bounding_box(bounding_box)

    @property
    def temporal_range(self):
        start = self.bounding_boxes[0].frame_index if len(self.bounding_boxes) > 0 else 0
        end = self.bounding_boxes[-1].frame_index if len(self.bounding_boxes) > 0 else 0
        return TemporalRange(start, end)

    @property
    def start_frame(self) -> int:
        return self.temporal_range.start_frame

    @property
    def end_frame(self) -> int:
        return self.temporal_range.end_frame

    def summary(self, multiline=True):
        return get_summary(self, get_trajectory_summary, multiline)

    def __len__(self):
        if len(self.bounding_boxes) == 0:
            return 0
        return len(self.temporal_range)

    def __getitem__(self, item: Union[int, slice]) -> Union[BoundingBox, 'Trajectory']:
        if isinstance(item, int):
            return self.bounding_boxes[item - self.start_frame]
        elif isinstance(item, slice):
            start = item.start - self.start_frame if item.start else None
            # inclusive end index
            stop = item.stop - self.start_frame + 1 if item.stop else None
            bounding_boxes = self.bounding_boxes[start:stop]
            return Trajectory(bounding_boxes)

    def __add__(self, other: 'Trajectory') -> 'Trajectory':
        if len(self) == 0:
            return Trajectory(other.bounding_boxes)
        if len(other) == 0:
            return Trajectory(self.bounding_boxes)

        temporal_range = self.temporal_range.union(other.temporal_range)
        bounding_boxes = list()

        for frame_index in range(temporal_range.start_frame, temporal_range.end_frame + 1):
            current_boxes = list()
            if frame_index in self.temporal_range:
                current_boxes.append(self.bounding_boxes[frame_index - self.start_frame])
            if frame_index in other.temporal_range:
                current_boxes.append(other.bounding_boxes[frame_index - other.start_frame])

            if len(current_boxes) > 0:
                bounding_boxes.append(combine_bounding_boxes(current_boxes))

        return Trajectory(bounding_boxes)

    def volume(self):
        return sum(bounding_box.area() for bounding_box in self.bounding_boxes)

    def intersect(self, other: 'Trajectory') -> 'Trajectory':
        temporal_range = self.temporal_range.intersect(other.temporal_range)
        bounding_boxes = list()
        for i in temporal_range:
            bounding_box = self[i]
            other_bounding_box = other[i]
            bounding_boxes.append(bounding_box.intersect(other_bounding_box))

        return Trajectory(bounding_boxes)

    def union(self, other: 'Trajectory') -> 'Trajectory':
        return self + other

    def add_bounding_box(self, bounding_box: BoundingBox):
        if len(self.bounding_boxes) > 0:
            end_bounding_box = self.bounding_boxes[-1]
            if end_bounding_box.frame_index >= bounding_box.frame_index:
                raise IndexError('Bounding box frame index less than the last')
            elif end_bounding_box.frame_index + 1 != bounding_box.frame_index:
                self.bounding_boxes.extend(linear_interpolate_bounding_boxes(end_bounding_box, bounding_box))
        self.bounding_boxes.append(bounding_box)
