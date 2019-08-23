from unittest import TestCase

from frater.core import Trajectory, BoundingBox
from frater.core.object import *


class TestObjectFunctions(TestCase):
    def test_temporally_segment_object(self):
        bounding_boxes = [BoundingBox(10, 10, 10, 10, frame_index=i) for i in range(1, 91)]
        trajectory = Trajectory(bounding_boxes)
        window_size = 20
        target_segments = list()
        for i in range(1, 91, window_size):
            end = min(i + window_size - 1, 90)
            traj = Trajectory(bounding_boxes[i - 1:end])
            target_segments.append(Object(object_id='', object_type=ObjectType.PERSON, trajectory=traj))
        obj = Object(object_id='', object_type=ObjectType.PERSON, trajectory=trajectory)
        print(target_segments)
        print(temporally_segment_object(obj, window_size))
        assert target_segments == temporally_segment_object(obj, window_size)
