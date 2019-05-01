from unittest import TestCase

from frater.core.bounding_box.bounding_box_factory import *
from ..mocks import MOCKS


class TestBoundingBoxFactory(TestCase):
    def test_json_to_bounding_box(self):
        bounding_box = MOCKS.frater.bounding_box
        bounding_box_json = MOCKS.json.bounding_box

        assert json_to_bounding_box(bounding_box_json) == bounding_box

    def test_bounding_box_to_json(self):
        bounding_box = MOCKS.frater.bounding_box
        bounding_box_json = MOCKS.json.bounding_box

        assert bounding_box_to_json(bounding_box) == bounding_box_json

    def test_protobuf_to_bounding_box(self):
        bounding_box = MOCKS.frater.bounding_box
        bounding_box_proto = MOCKS.proto.bounding_box
        assert protobuf_to_bounding_box(bounding_box_proto) == bounding_box

    def test_bounding_box_to_protobuf(self):
        bounding_box = MOCKS.frater.bounding_box
        bounding_box_proto = MOCKS.proto.bounding_box
        assert bounding_box_to_protobuf(bounding_box) == bounding_box_proto
