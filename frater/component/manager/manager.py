from threading import Lock
from typing import List

from .thread import ComponentThread
from ..component import Component
from ...utilities import Handler


class ComponentManager:
    def __init__(self, component: Component):
        self.component = component
        self.lock = Lock()
        self.thread = self.create_component_thread()

    def create_component_thread(self):
        return ComponentThread(self.component)

    def started(self):
        return {'started': self.component.started}

    def stopped(self):
        return {'stopped': self.component.stopped}

    def start(self):
        if self.component.started:
            message = 'Component already started. Cannot be started twice.'
        else:
            if self.thread.started_once:
                self.thread = self.create_component_thread()
                message = 'Component restarted.'
            else:
                message = 'Component successfully started.'

            self.thread.start()

        return {'started': True, 'message': message}

    def stop(self):
        if self.component.paused:
            return {'stopped': False, 'message': 'unable to stop when component is paused'}

        if self.component.stopped:
            return {'stopped': True, 'message': 'Component already stopped'}

        with self.lock:
            self.component.stop()

        try:
            self.thread.join()
            return {'stopped': True, 'message': 'Component successfully stopped'}

        except BaseException as e:
            return {'stopped': False, 'message': str(e)}

    def error(self):
        has_error = self.thread.has_error()
        message = str(self.thread.error) if has_error else 'No current error'
        response = {'error': has_error, 'message': message}

        return response

    def reset(self):
        with self.lock:
            self.component.reset()

        return {'reset': True}

    def get_config(self):
        return self.component.config.to_dict()

    def update_config(self, update):
        with self.lock:
            self.component.config.update_from_dict(update)

        return {'updated': True, 'config': self.component.config.to_dict()}

    def toggle_pause(self):
        if self.component.stopped:
            return {'paused': None, 'error': True, 'message': 'unable to pause since component is not started'}
        with self.lock:
            self.component.toggle_pause()

        return {'paused': self.component.paused, 'message': 'Pause toggled'}

    def pause(self):
        if self.component.stopped:
            return {'paused': False, 'message': 'unable to pause since component is not started'}
        if self.component.paused:
            return {'paused': True, 'message': 'Component already paused'}
        else:
            with self.lock:
                self.component.pause()

            return {'paused': self.component.paused}

    def unpause(self):
        if self.component.stopped:
            return {'unpaused': False, 'message': 'unable to unpause since component is not started'}
        if not self.component.paused:
            return {'unpaused': True, 'message': 'Component already unpaused'}
        else:
            with self.lock:
                self.component.unpause()
            return {'unpaused': not self.component.paused}

    def paused(self):
        return {'paused': self.component.paused}

    def active(self):
        return {'active': self.component.active}

    def get_status(self):
        status = {
            'config': self.get_config(),
            'state': self.get_state()
        }

        status.update(self.started())
        status.update(self.active())
        status.update(self.stopped())
        status.update(self.paused())

        return status

    def get_state(self):
        return self.component.state.to_dict()

    def get_endpoints(self):
        return [handler.to_dict() for handler in self.get_all_handlers()]

    def get_all_handlers(self):
        return self.get_default_handlers() + self.component.get_additional_handlers()

    def get_default_handlers(self) -> List[Handler]:
        return [
            Handler('/start', 'start', self.start),
            Handler('/started', 'started', self.started),
            Handler('/stop', 'stop', self.stop),
            Handler('/stopped', 'stopped', self.stopped),
            Handler('/toggle_pause', 'toggle_pause', self.toggle_pause),
            Handler('/pause', 'pause', self.pause),
            Handler('/unpause', 'unpause', self.unpause),
            Handler('/paused', 'paused', self.paused),
            Handler('/active', 'active', self.active),
            Handler('/reset', 'reset', self.reset),
            Handler('/error', 'error', self.error),
            Handler('/config', 'update_config', self.update_config, methods=['PATCH']),
            Handler('/config', 'get_config', self.get_config),
            Handler('/state', 'get_state', self.get_state),
            Handler('/status', 'get_status', self.get_status),
            Handler('/endpoints', 'get_endpoints', self.get_endpoints)
        ]
