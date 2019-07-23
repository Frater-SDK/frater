from unittest import TestCase

from frater.core.object.object_factory import *
from ..mocks import MOCKS


class TestObjectFactory(TestCase):
    def test_json_to_object(self):
        obj = MOCKS.frater.object
        object_json = MOCKS.json.object

        assert json_to_object(object_json) == obj

    def test_object_to_json(self):
        obj = MOCKS.frater.object
        object_json = MOCKS.json.object

        assert object_to_json(obj) == object_json
