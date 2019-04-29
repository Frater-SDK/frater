from unittest import TestCase

from frater.core.factory.activity import *
from .mocks import MOCKS


class TestActivityFactory(TestCase):
    def test_json_to_activity(self):
        activity = MOCKS.frater.activity
        activity_json = MOCKS.json.activity

        assert json_to_activity(activity_json) == activity

    def test_activity_to_json(self):
        activity = MOCKS.frater.activity
        activity_json = MOCKS.json.activity

        assert activity_to_json(activity) == activity_json

    def test_protobuf_to_activity(self):
        activity = MOCKS.frater.activity
        activity_proto = MOCKS.proto.activity

        assert protobuf_to_activity(activity_proto) == activity

    def test_activity_to_protobuf(self):
        activity = MOCKS.frater.activity
        activity_proto = MOCKS.proto.activity
        assert activity_to_protobuf(activity) == activity_proto
