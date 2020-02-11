from unittest import TestCase
from unittest.mock import Mock

from frater.client import API
from frater.component import ComponentClient, ComponentClientConfig, get_component_client_config


class TestComponentClient(TestCase):
    def setUp(self) -> None:
        config = ComponentClientConfig(host='localhost', port=3000, name='test_client')
        self.client = ComponentClient(config)

        self.mock_api = Mock(spec=API)
        self.client.component_api = self.mock_api

    def tearDown(self) -> None:
        self.mock_api.reset_mock()

    def test_init(self):
        config = ComponentClientConfig(host='localhost', port=3000, name='test_client')
        client = ComponentClient(config)
        assert client.config == config
        assert client.component_api.host == 'localhost'
        assert client.component_api.port == 3000

    def test_start(self):
        self.mock_api.get.return_value = {'started': True, 'message': 'Component successfully started.'}
        response = self.client.start()
        assert response == {'started': True, 'message': 'Component successfully started.'}

        assert self.mock_api.get.call_count == 1

    def test_started(self):
        self.mock_api.get.return_value = {'started': True}
        response = self.client.started()
        assert response == {'started': True}

        assert self.mock_api.get.call_count == 1

    def test_stop(self):
        self.mock_api.get.return_value = {'stopped': True, 'message': 'Component successfully stopped.'}
        response = self.client.stop()
        assert response == {'stopped': True, 'message': 'Component successfully stopped.'}

        assert self.mock_api.get.call_count == 1

    def test_stopped(self):
        self.mock_api.get.return_value = {'stopped': True}
        response = self.client.stopped()
        assert response == {'stopped': True}

        assert self.mock_api.get.call_count == 1

    def test_toggle_pause(self):
        self.mock_api.get.return_value = {'paused': True, 'message': 'Pause toggled'}
        response = self.client.toggle_pause()
        assert response == {'paused': True, 'message': 'Pause toggled'}

        self.mock_api.get.return_value = {'paused': False, 'message': 'Pause toggled'}
        response = self.client.toggle_pause()
        assert response == {'paused': False, 'message': 'Pause toggled'}

        assert self.mock_api.get.call_count == 2

    def test_pause(self):
        self.mock_api.get.return_value = {'paused': True}
        response = self.client.pause()
        assert response == {'paused': True}

        assert self.mock_api.get.call_count == 1

    def test_unpause(self):
        self.mock_api.get.return_value = {'unpaused': True}
        response = self.client.unpause()
        assert response == {'unpaused': True}

        assert self.mock_api.get.call_count == 1

    def test_paused(self):
        self.mock_api.get.return_value = {'paused': True}
        response = self.client.paused()
        assert response == {'paused': True}

        assert self.mock_api.get.call_count == 1

    def test_active(self):
        self.mock_api.get.return_value = {'active': True}
        response = self.client.active()
        assert response == {'active': True}

        assert self.mock_api.get.call_count == 1

    def test_reset(self):
        self.mock_api.get.return_value = {'reset': True}
        response = self.client.reset()
        assert response == {'reset': True}

        assert self.mock_api.get.call_count == 1

    def test_error(self):
        self.mock_api.get.return_value = {'error': False}
        response = self.client.error()
        assert response == {'error': False}

        assert self.mock_api.get.call_count == 1

    def test_update_config(self):
        self.mock_api.patch.return_value = {'some_config': True, 'other_config': False}
        response = self.client.update_config({'other_config': False})
        assert response == {'some_config': True, 'other_config': False}

        assert self.mock_api.patch.call_count == 1

    def test_get_config(self):
        self.mock_api.get.return_value = {'some_config': True}
        response = self.client.get_config()
        assert response == {'some_config': True}

        assert self.mock_api.get.call_count == 1

    def test_get_state(self):
        self.mock_api.get.return_value = {'some_state': 23}
        response = self.client.get_state()
        assert response == {'some_state': 23}

        assert self.mock_api.get.call_count == 1

    def test_get_status(self):
        self.mock_api.get.return_value = {'active': True, 'started': True, 'stopped': False, 'paused': False}
        response = self.client.get_status()
        assert response == {'active': True, 'started': True, 'stopped': False, 'paused': False}

        assert self.mock_api.get.call_count == 1

    def test_get_endpoints(self):
        self.mock_api.get.return_value = [{'endpoint': '/test', 'name': 'get_test', 'methods': ['GET']}]
        response = self.client.get_endpoints()
        assert response == [{'endpoint': '/test', 'name': 'get_test', 'methods': ['GET']}]

        assert self.mock_api.get.call_count == 1


def test_get_component_client_config():
    component_config = Mock()
    component_config.component_id = '1234'
    component_config.name = 'test'
    network_config = Mock()
    network_config.host = 'localhost'
    network_config.port = 3000

    config = ComponentClientConfig(config_id='12345', name='test', component_id='1234', host='localhost', port=3000)

    cfg = get_component_client_config(component_config, network_config)
    assert cfg != config
    cfg.config_id = '12345'
    assert cfg == config
