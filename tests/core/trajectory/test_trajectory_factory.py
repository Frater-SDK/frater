from unittest import TestCase

from frater.core.trajectory.trajectory_factory import *
from ...mocks import MOCKS


class TestTrajectoryFactory(TestCase):
    def test_json_to_trajectory(self):
        trajectory = MOCKS.frater.trajectory
        trajectory_json = MOCKS.json.trajectory

        assert json_to_trajectory(trajectory_json) == trajectory

    def test_trajectory_to_json(self):
        trajectory = MOCKS.frater.trajectory
        trajectory_json = MOCKS.json.trajectory

        assert trajectory_to_json(trajectory) == trajectory_json
