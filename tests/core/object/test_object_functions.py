from unittest import TestCase

from frater.core import Trajectory, BoundingBox, TemporalRange
from frater.core.object import *


class TestObjectFunctions(TestCase):
    def test_temporally_segment_object(self):
        bounding_boxes = [BoundingBox(10, 10, 10, 10, frame=i) for i in range(1, 91)]
        temporal_range = TemporalRange(1, 90)
        trajectory = Trajectory(bounding_boxes, temporal_range)
        window_size = 20
        target_segments = list()
        for i in range(1, 91, window_size):
            end = min(i + window_size, 91)
            traj = Trajectory(bounding_boxes[i - 1:end - 1], TemporalRange(i, end - 1))
            target_segments.append(Object(ObjectType.PERSON, trajectory=traj))
        obj = Object(ObjectType.PERSON, trajectory=trajectory)

        assert target_segments == temporally_segment_object(obj, window_size)
