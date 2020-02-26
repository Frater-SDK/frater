from typing import Dict

from ...client import ComponentClientConfig, ComponentClient
from ...utilities import Handler

__all__ = ['SystemManager']


class SystemManager:
    def __init__(self):
        self.components: Dict[str, ComponentClient] = dict()

    def check_dependency(self, params):
        # TODO implement dependency checking. For now, dependencies are always ready
        return {'ready': True}

    def get_component(self, params):
        return self.components[params['component_id']].config.to_dict()

    def get_components(self):
        return [component.config.to_dict() for component in self.components.values()]

    def register_component(self, data):
        client_config = ComponentClientConfig.from_dict(data)
        if client_config.component_id in self.components:
            return {'registered': False, 'message': f'Component {client_config.component_id} already registered'}
        else:
            self.components[client_config.component_id] = ComponentClient(client_config)

            return {'registered': True, 'message': f'Component {client_config.component_id} successfully registered'}

    def start(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'started': False, 'message': f'Component {component_id} is not registered in this system.'}
        client = self.components[component_id]

        response = client.start()
        response.update({'component_id': component_id})

        return response

    def start_all(self):
        return [self.start({'component_id': component_id}) for component_id in self.components]

    def started_component(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'started': False, 'message': f'Component {component_id} is not registered in this system.'}

        client = self.components[component_id]

        response = client.started()
        response.update({'component_id': component_id})

        return response

    def all_started(self):
        return [self.started_component({'component_id': component_id}) for component_id in self.components]

    def stop(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'stopped': False, 'message': f'Component {component_id} is not registered in this system.'}
        client = self.components[component_id]

        response = client.stop()
        response.update({'component_id': component_id})

        return response

    def stop_all(self):
        return [self.stop({'component_id': component_id}) for component_id in self.components]

    def stopped(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'stopped': False, 'message': f'Component {component_id} is not registered in this system.'}

        client = self.components[component_id]

        response = client.stopped()
        response.update({'component_id': component_id})

        return response

    def all_stopped(self):
        return [self.stopped({'component_id': component_id}) for component_id in self.components]

    def toggle_pause(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'paused': None, 'message': f'Component {component_id} is not registered in this system.'}

        client = self.components[component_id]

        response = client.toggle_pause()
        response.update({'component_id': component_id})

        return response

    def toggle_pause_all(self):
        return [self.toggle_pause({'component_id': component_id}) for component_id in self.components]

    def pause(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'paused': False, 'message': f'Component {component_id} is not registered in this system.'}
        client = self.components[component_id]

        response = client.pause()
        response.update({'component_id': component_id})

        return response

    def pause_all(self):
        return [self.pause({'component_id': component_id}) for component_id in self.components]

    def unpause(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'unpaused': False, 'message': f'Component {component_id} is not registered in this system.'}

        client = self.components[component_id]

        response = client.stopped()
        response.update({'component_id': component_id})

        return response

    def unpause_all(self):
        return [self.unpause({'component_id': component_id}) for component_id in self.components]

    def paused(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'paused': None, 'message': f'Component {component_id} is not registered in this system.'}

        client = self.components[component_id]

        response = client.paused()
        response.update({'component_id': component_id})

        return response

    def all_paused(self):
        return [self.paused({'component_id': component_id}) for component_id in self.components]

    def active(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'active': None, 'message': f'Component {component_id} is not registered in this system.'}

        client = self.components[component_id]

        response = client.active()
        response.update({'component_id': component_id})

        return response

    def all_active(self):
        return [self.active({'component_id': component_id}) for component_id in self.components]

    def reset(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'reset': False, 'message': f'Component {component_id} is not registered in this system.'}

        client = self.components[component_id]

        response = client.reset()
        response.update({'component_id': component_id})

        return response

    def reset_all(self):
        return [self.reset({'component_id': component_id}) for component_id in self.components]

    def error(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'error': False, 'message': f'Component {component_id} is not registered in this system.'}

        client = self.components[component_id]

        response = client.error()
        response.update({'component_id': component_id})

        return response

    def all_error(self):
        return [self.error({'component_id': component_id}) for component_id in self.components]

    def update_config(self, data):
        component_id = data['component_id']
        config = data['config']
        if component_id not in self.components:
            return {'updated': False, 'message': f'Component {component_id} is not registered in this system.'}

        client = self.components[component_id]

        response = client.update_config(config)
        response.update({'component_id': component_id})

        return response

    def get_config(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'stopped': False, 'message': f'Component {component_id} is not registered in this system.'}

        client = self.components[component_id]

        response = client.get_config()

        return response

    def get_all_configs(self):
        return [self.get_config({'component_id': component_id}) for component_id in self.components]

    def get_state(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'stopped': False, 'message': f'Component {component_id} is not registered in this system.'}

        client = self.components[component_id]

        response = {'component_id': component_id, 'state': client.get_status()}

        return response

    def get_all_states(self):
        return [self.get_state({'component_id': component_id}) for component_id in self.components]

    def get_status(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'stopped': False, 'message': f'Component {component_id} is not registered in this system.'}

        client = self.components[component_id]

        response = client.get_status()
        response.update({'component_id': component_id})

        return response

    def get_all_statuses(self):
        return [self.get_status({'component_id': component_id}) for component_id in self.components]

    def get_default_endpoints(self):
        return [
            Handler('/dependency', 'check_dependency', self.check_dependency),
            Handler('/component', 'get_component', self.get_component),
            Handler('/component/register', 'register_component', self.register_component, methods=['POST']),
            Handler('/component/start', 'start', self.start),
            Handler('/component/started', 'started_component', self.started_component),
            Handler('/component/stop', 'stop', self.stop),
            Handler('/component/stopped', 'stopped', self.stopped),
            Handler('/component/toggle_pause', 'toggle_pause', self.toggle_pause),
            Handler('/component/pause', 'pause', self.pause),
            Handler('/component/unpause', 'unpause', self.unpause),
            Handler('/component/paused', 'paused', self.paused),
            Handler('/component/active', 'active', self.active),
            Handler('/component/reset', 'reset', self.reset),
            Handler('/component/error', 'error', self.error),
            Handler('/component/config', 'get_config', self.get_config),
            Handler('/component/config', 'update_config', self.update_config, methods=['PATCH']),
            Handler('/component/state', 'get_state', self.get_state),
            Handler('/component/status', 'get_status', self.get_status),
            Handler('/components', 'get_components', self.get_components),
            Handler('/components/start', 'start_all', self.start_all),
            Handler('/components/started', 'all_started', self.all_started),
            Handler('/components/stop', 'stop_all', self.stop_all),
            Handler('/components/stopped', 'all_stopped', self.all_stopped),
            Handler('/components/toggle_pause', 'toggle_pause_all', self.toggle_pause_all),
            Handler('/components/pause', 'pause_all', self.pause_all),
            Handler('/components/unpause', 'unpause_all', self.unpause_all),
            Handler('/components/paused', 'all_paused', self.all_paused),
            Handler('/components/active', 'all_active', self.all_active),
            Handler('/components/reset', 'reset_all', self.reset_all),
            Handler('/components/error', 'all_error', self.all_error),
            Handler('/components/config', 'get_all_configs', self.get_all_configs),
            Handler('/components/state', 'get_all_states', self.get_all_states),
            Handler('/components/status', 'get_all_statuses', self.get_all_statuses),
        ]
