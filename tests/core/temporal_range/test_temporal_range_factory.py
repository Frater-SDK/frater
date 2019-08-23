from unittest import TestCase

from frater.core.temporal_range.temporal_range_factory import *
from ...mocks import MOCKS


class TestTemporalRangeFactory(TestCase):
    def test_json_to_temporal_range(self):
        temporal_range_json = MOCKS.json.temporal_range
        temporal_range = MOCKS.frater.temporal_range
        assert json_to_temporal_range(temporal_range_json) == temporal_range

    def test_temporal_range_to_json(self):
        temporal_range_json = MOCKS.json.temporal_range
        temporal_range = MOCKS.frater.temporal_range
        assert temporal_range_to_json(temporal_range) == temporal_range_json
