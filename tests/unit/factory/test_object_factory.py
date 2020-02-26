import unittest

import pytest

from frater.factory import ObjectFactory


class MockType:
    pass


class MockSubType(MockType):
    pass


class OtherType:
    pass


class TestObjectFactory(unittest.TestCase):
    def test_init(self):
        factory = ObjectFactory(MockType)
        assert factory._base_type == MockType

    def test_get(self):
        factory = ObjectFactory(MockType)

        factory.factory_map['subtype'] = MockSubType

        assert factory.get('subtype')

    def test_register_class(self):
        factory = ObjectFactory(MockType)

        factory.register_class('subtype', MockSubType)

        assert 'subtype' in factory.factory_map
        assert factory.factory_map['subtype'] is MockSubType

    def test_register_class_with_non_subclass(self):
        factory = ObjectFactory(MockType)
        with pytest.raises(TypeError):
            factory.register_class('other', OtherType)

    def test_register(self):
        factory = ObjectFactory(MockType)
        factory.register('subtype')(MockSubType)

        assert 'subtype' in factory.factory_map
        assert factory.factory_map['subtype'] is MockSubType

    def test_register_with_non_subclass(self):
        factory = ObjectFactory(MockType)

        func = factory.register('other')
        with pytest.raises(TypeError):
            func(OtherType)

    def test_unregister(self):
        factory = ObjectFactory(MockType)
        factory.factory_map['subtype'] = MockSubType

        factory.unregister('subtype')
        assert 'subtype' not in factory.factory_map

    def test_unregister_with_invalid_name(self):
        factory = ObjectFactory(MockType)

        with pytest.raises(KeyError):
            factory.unregister('other')
