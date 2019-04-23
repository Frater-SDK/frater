from unittest import TestCase

from frater.core.bounding_box import BoundingBox
from frater.core.factory.trajectory import *
from frater.core.proto import core
from frater.core.trajectory import Trajectory


class TestTrajectoryFactory(TestCase):
    def setUp(self):
        self.test_trajectory_protobuf = core.Trajectory()

    def test_json_to_trajectory_with_empty_trajectory(self):
        test_trajectory = Trajectory()
        test_trajectory_json = {'bounding_boxes': [],
                                'temporal_range': {'start_frame': -1, 'end_frame': -1},
                                'scale': 1.0}
        trajectory = json_to_trajectory(test_trajectory_json)
        assert test_trajectory == trajectory

    def test_json_to_trajectory(self):
        test_trajectory = Trajectory([BoundingBox(10, 10, 50, 50, confidence=0.33)] * 10, (10, 10), 1.4)
        test_trajectory_json = {'bounding_boxes': [{'x': 10, 'y': 10, 'w': 50, 'h': 50,
                                                    'confidence': 0.33, 'frame_index': -1}] * 10,
                                'temporal_range': {'start_frame': 10, 'end_frame': 10},
                                'scale': 1.4}

        assert test_trajectory == json_to_trajectory(test_trajectory_json)

    def test_trajectory_to_json_with_empty_trajectory(self):
        test_trajectory = Trajectory()
        test_trajectory_json = {'bounding_boxes': [],
                                'temporal_range': {'start_frame': -1, 'end_frame': -1},
                                'scale': 1.0}

        assert test_trajectory_json == trajectory_to_json(test_trajectory)

    def test_trajectory_to_json(self):
        test_trajectory = Trajectory([BoundingBox(10, 10, 50, 50, confidence=0.33)] * 10, (10, 10), 1.4)
        test_trajectory_json = {'bounding_boxes': [{'x': 10, 'y': 10, 'w': 50, 'h': 50,
                                                    'frame_index': -1, 'confidence': 0.33}] * 10,
                                'temporal_range': {'start_frame': 10, 'end_frame': 10},
                                'scale': 1.4}
        trajectory_json = trajectory_to_json(test_trajectory)
        assert test_trajectory_json == trajectory_json

    def test_protobuf_to_trajectory_with_empty_trajectory(self):
        test_trajectory = Trajectory()
        test_trajectory_proto = core.Trajectory(temporal_range=core.TemporalRange(start_frame=-1,
                                                                                  end_frame=-1), scale=1.0)
        assert protobuf_to_trajectory(test_trajectory_proto) == test_trajectory

    def test_protobuf_to_trajectory(self):
        test_trajectory = Trajectory([BoundingBox(10, 10, 50, 50, confidence=0.33)] * 10, (10, 10), 1.4)
        test_trajectory_proto = core.Trajectory(bounding_boxes=[core.BoundingBox(x=10, y=10, w=50, h=50,
                                                                                 confidence=0.33, frame=-1)] * 10,
                                                temporal_range=core.TemporalRange(start_frame=10,
                                                                                  end_frame=10), scale=1.4)
        assert test_trajectory_proto == trajectory_to_protobuf(test_trajectory)

    def test_trajectory_to_protobuf_with_empty_trajectory(self):
        test_trajectory = Trajectory()
        test_trajectory_proto = core.Trajectory(temporal_range=core.TemporalRange(start_frame=-1,
                                                                                  end_frame=-1), scale=1.0)
        assert test_trajectory == protobuf_to_trajectory(test_trajectory_proto)

    def test_trajectory_to_protobuf(self):
        test_trajectory = Trajectory([BoundingBox(10, 10, 50, 50, confidence=0.33)] * 10, (10, 10), 1.4)
        test_trajectory_proto = core.Trajectory(bounding_boxes=[core.BoundingBox(x=10, y=10, w=50, h=50,
                                                                                 confidence=0.33, frame=-1)] * 10,
                                                temporal_range=core.TemporalRange(start_frame=10,
                                                                                  end_frame=10), scale=1.4)

        assert test_trajectory == protobuf_to_trajectory(test_trajectory_proto)
