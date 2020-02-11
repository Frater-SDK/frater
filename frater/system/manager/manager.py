from typing import Dict

from frater.component import ComponentClientConfig, ComponentClient
from frater.server import Handler, ServerManager

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

    def start_component(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'started': False, 'message': f'Component {component_id} is not registered in this system.'}
        client = self.components[component_id]

        response = client.start()
        response.update({'component_id': component_id})

        return response

    def start_all_components(self):
        return [self.start_component({'component_id': component_id}) for component_id in self.components]

    def started_component(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'started': False, 'message': f'Component {component_id} is not registered in this system.'}

        client = self.components[component_id]

        response = client.started()
        response.update({'component_id': component_id})

        return response

    def started_all_components(self):
        return [self.started_component({'component_id': component_id}) for component_id in self.components]

    def stop_component(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'stopped': False, 'message': f'Component {component_id} is not registered in this system.'}
        client = self.components[component_id]

        response = client.stop()
        response.update({'component_id': component_id})

        return response

    def stop_all_components(self):
        return [self.stop_component({'component_id': component_id}) for component_id in self.components]

    def stopped_component(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'stopped': False, 'message': f'Component {component_id} is not registered in this system.'}

        client = self.components[component_id]

        response = client.stopped()
        response.update({'component_id': component_id})

        return response

    def stopped_all_components(self):
        return [self.stopped_component({'component_id': component_id}) for component_id in self.components]

    def toggle_pause_component(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'paused': None, 'message': f'Component {component_id} is not registered in this system.'}

        client = self.components[component_id]

        response = client.toggle_pause()
        response.update({'component_id': component_id})

        return response

    def toggle_pause_all_components(self):
        return [self.toggle_pause_component({'component_id': component_id}) for component_id in self.components]

    def pause_component(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'paused': False, 'message': f'Component {component_id} is not registered in this system.'}
        client = self.components[component_id]

        response = client.pause()
        response.update({'component_id': component_id})

        return response

    def pause_all_components(self):
        return [self.pause_component({'component_id': component_id}) for component_id in self.components]

    def unpause_component(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'unpaused': False, 'message': f'Component {component_id} is not registered in this system.'}

        client = self.components[component_id]

        response = client.stopped()
        response.update({'component_id': component_id})

        return response

    def unpause_all_components(self):
        return [self.unpause_component({'component_id': component_id}) for component_id in self.components]

    def paused_component(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'paused': None, 'message': f'Component {component_id} is not registered in this system.'}

        client = self.components[component_id]

        response = client.paused()
        response.update({'component_id': component_id})

        return response

    def paused_all_components(self):
        return [self.paused_component({'component_id': component_id}) for component_id in self.components]

    def active_component(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'active': None, 'message': f'Component {component_id} is not registered in this system.'}

        client = self.components[component_id]

        response = client.active()
        response.update({'component_id': component_id})

        return response

    def active_all_components(self):
        return [self.active_component({'component_id': component_id}) for component_id in self.components]

    def reset_component(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'reset': False, 'message': f'Component {component_id} is not registered in this system.'}

        client = self.components[component_id]

        response = client.reset()
        response.update({'component_id': component_id})

        return response

    def reset_all_components(self):
        return [self.reset_component({'component_id': component_id}) for component_id in self.components]

    def error_component(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'error': False, 'message': f'Component {component_id} is not registered in this system.'}

        client = self.components[component_id]

        response = client.error()
        response.update({'component_id': component_id})

        return response

    def error_all_components(self):
        return [self.error_component({'component_id': component_id}) for component_id in self.components]

    def update_component_config(self, data):
        component_id = data['component_id']
        config = data['config']
        if component_id not in self.components:
            return {'updated': False, 'message': f'Component {component_id} is not registered in this system.'}

        client = self.components[component_id]

        response = client.update_config(config)
        response.update({'component_id': component_id})

        return response

    def get_component_config(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'stopped': False, 'message': f'Component {component_id} is not registered in this system.'}

        client = self.components[component_id]

        response = client.get_config()

        return response

    def get_all_component_configs(self):
        return [self.get_component_config({'component_id': component_id}) for component_id in self.components]

    def get_component_state(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'stopped': False, 'message': f'Component {component_id} is not registered in this system.'}

        client = self.components[component_id]

        response = {'component_id': component_id, 'state': client.get_status()}

        return response

    def get_all_component_states(self):
        return [self.get_component_state({'component_id': component_id}) for component_id in self.components]

    def get_component_status(self, params):
        component_id = params['component_id']
        if component_id not in self.components:
            return {'stopped': False, 'message': f'Component {component_id} is not registered in this system.'}

        client = self.components[component_id]

        response = client.get_status()
        response.update({'component_id': component_id})

        return response

    def get_all_component_statuses(self):
        return [self.get_component_status({'component_id': component_id}) for component_id in self.components]

    def register_endpoints(self, server_manager: ServerManager):
        for handler in self.get_default_endpoints():
            server_manager.add_handler(handler)

    def get_default_endpoints(self):
        return [
            Handler('dependency', 'check_dependency', self.check_dependency),
            Handler('component', 'get_component', self.get_component),
            Handler('component/register', 'register_component', self.register_component, methods=['POST']),
            Handler('component/start', 'start_component', self.start_component),
            Handler('component/started', 'started_component', self.started_component),
            Handler('component/stop', 'stop_component', self.stop_component),
            Handler('component/stopped', 'stopped_component', self.stopped_component),
            Handler('component/toggle_pause', 'toggle_pause_component', self.toggle_pause_component),
            Handler('component/pause', 'pause_component', self.pause_component),
            Handler('component/unpause', 'unpause_component', self.unpause_component),
            Handler('component/paused', 'paused_component', self.paused_component),
            Handler('component/active', 'active_component', self.active_component),
            Handler('component/reset', 'reset_component', self.reset_component),
            Handler('component/error', 'error_component', self.error_component),
            Handler('component/config', 'get_component_config', self.get_component_config),
            Handler('component/config', 'update_component_config', self.update_component_config, methods=['PATCH']),
            Handler('component/state', 'get_component_state', self.get_component_state),
            Handler('component/status', 'get_component_status', self.get_component_status),
            Handler('components', 'get_components', self.get_components),
            Handler('components/start', 'start_all_components', self.start_all_components),
            Handler('components/started', 'started_all_components', self.started_all_components),
            Handler('components/stop', 'stop_all_components', self.stop_all_components),
            Handler('components/stopped', 'stopped_all_components', self.stopped_all_components),
            Handler('components/toggle_pause', 'toggle_pause_all_components', self.toggle_pause_all_components),
            Handler('components/pause', 'pause_all_components', self.pause_all_components),
            Handler('components/unpause', 'unpause_all_components', self.unpause_all_components),
            Handler('components/paused', 'paused_all_components', self.paused_all_components),
            Handler('components/active', 'active_all_components', self.active_all_components),
            Handler('components/reset', 'reset_all_components', self.reset_all_components),
            Handler('components/error', 'error_all_components', self.error_component),
            Handler('components/config', 'get_all_component_configs', self.get_all_component_configs),
            Handler('components/state', 'get_all_component_states', self.get_all_component_states),
            Handler('components/status', 'get_all_component_statuses', self.get_all_component_statuses),
        ]
