import unittest

from frater.config import Config


class TestConfig(unittest.TestCase):
    def test_config_init(self):
        cfg = Config(name='hello', config_id='123456')
        assert cfg.name == 'hello'
        assert cfg.config_id == '123456'
        assert cfg.meta == {}

    def test_config_from_dict(self):
        d = {'name': 'hello', 'test': 'my_test', 'config_id': '123456'}
        cfg = Config.from_dict(d)
        assert cfg.name == 'hello'
        assert cfg.config_id == '123456'
        assert cfg.meta == {'test': 'my_test'}
        assert cfg == Config('hello', '123456', {'test': 'my_test'})

    def test_config_to_dict(self):
        d = {'name': 'hello', 'config_id': '123456', 'meta': {'test': 'my_test'}}
        assert d == Config('hello', '123456', {'test': 'my_test'}).to_dict()

    def test_separate_config(self):
        d = {'name': 'hello', 'test': 'my_test', 'config_id': '123456'}
        required, meta = Config.separate_config(d)

        assert required == {'name': 'hello', 'config_id': '123456'}
        assert meta == {'test': 'my_test'}
