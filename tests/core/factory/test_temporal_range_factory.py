from unittest import TestCase
from frater.core.factory.temporal_range import *
from frater.core.proto import core


class TestTemporalRangeFactory(TestCase):
    def test_json_to_temporal_range_with_empty_temporal_range(self):
        temporal_range_json = {}
        temporal_range = None
        assert temporal_range == json_to_temporal_range(temporal_range_json)

    def test_json_to_temporal_range_no_start(self):
        temporal_range_json = {'end_frame': 12}
        temporal_range = None
        assert temporal_range == json_to_temporal_range(temporal_range_json)

    def test_json_to_temporal_range_no_end(self):
        temporal_range_json = {'start_frame': 10}
        temporal_range = None
        assert temporal_range == json_to_temporal_range(temporal_range_json)

    def test_json_to_temporal_range_bad_range(self):
        temporal_range_json = {'start_frame': 10, 'end_frame': 8}
        temporal_range = None
        assert temporal_range == json_to_temporal_range(temporal_range_json)

    def test_json_to_temporal_range(self):
        temporal_range_json = {'start_frame': 10, 'end_frame': 15}
        temporal_range = 10, 15
        assert temporal_range == json_to_temporal_range(temporal_range_json)

    def test_temporal_range_to_json_with_empty_temporal_range(self):
        temporal_range_json = None
        temporal_range = None
        assert temporal_range == json_to_temporal_range(temporal_range_json)

    def test_temporal_range_to_json_bad_tuple(self):
        temporal_range_json = None
        temporal_range = 10,

        # noinspection PyTypeChecker
        assert temporal_range_json == temporal_range_to_json(temporal_range)

    def test_temporal_range_to_json_bad_range(self):
        temporal_range_json = None
        temporal_range = 10, 8

        assert temporal_range_json == temporal_range_to_json(temporal_range)

    def test_temporal_range_to_json(self):
        temporal_range_json = {'start_frame': 10, 'end_frame': 15}
        temporal_range = 10, 15
        assert temporal_range_json == temporal_range_to_json(temporal_range)

    def test_protobuf_to_temporal_range_with_empty_temporal_range(self):
        test_temporal_range_proto = None
        test_temporal_range = None

        assert test_temporal_range == protobuf_to_temporal_range(test_temporal_range_proto)

    def test_protobuf_to_temporal_range_bad_range(self):
        test_temporal_range_proto = core.TemporalRange(start_frame=13, end_frame=12)
        test_temporal_range = None

        assert test_temporal_range == protobuf_to_temporal_range(test_temporal_range_proto)

    def test_protobuf_to_temporal_range(self):
        test_temporal_range_proto = core.TemporalRange(start_frame=10, end_frame=12)
        test_temporal_range = 10, 12

        assert test_temporal_range == protobuf_to_temporal_range(test_temporal_range_proto)

    def test_temporal_range_to_protobuf_with_empty_temporal_range(self):
        test_temporal_range_proto = None
        test_temporal_range = None

        assert test_temporal_range_proto == temporal_range_to_protobuf(test_temporal_range)

    def test_temporal_range_to_protobuf_bad_tuple(self):
        temporal_range_proto = None
        temporal_range = 10,

        # noinspection PyTypeChecker
        assert temporal_range_proto == temporal_range_to_json(temporal_range)

    def test_temporal_range_to_protobuf_bad_range(self):
        temporal_range_proto = None
        temporal_range = 10, 8

        assert temporal_range_proto == temporal_range_to_protobuf(temporal_range)

    def test_temporal_range_to_protobuf(self):
        test_temporal_range_proto = core.TemporalRange(start_frame=10, end_frame=12)
        test_temporal_range = 10, 12

        assert test_temporal_range_proto == temporal_range_to_protobuf(test_temporal_range)
