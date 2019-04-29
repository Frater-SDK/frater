from unittest import TestCase

from frater.core.factory.trajectory import *
from .mocks import MOCKS


class TestTrajectoryFactory(TestCase):
    def test_json_to_trajectory(self):
        trajectory = MOCKS.frater.trajectory
        trajectory_json = MOCKS.json.trajectory

        assert json_to_trajectory(trajectory_json) == trajectory

    def test_trajectory_to_json(self):
        trajectory = MOCKS.frater.trajectory
        trajectory_json = MOCKS.json.trajectory

        assert trajectory_to_json(trajectory) == trajectory_json

    def test_protobuf_to_trajectory(self):
        trajectory = MOCKS.frater.trajectory
        trajectory_proto = MOCKS.proto.trajectory
        assert protobuf_to_trajectory(trajectory_proto) == trajectory

    def test_trajectory_to_protobuf(self):
        trajectory = MOCKS.frater.trajectory
        trajectory_proto = MOCKS.proto.trajectory

        assert trajectory_to_protobuf(trajectory) == trajectory_proto
