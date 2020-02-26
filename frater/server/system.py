from .middleware import get_default_middleware
from .server_manager import ServerManager
from ..system import SystemManager

__all__ = ['serve_system']


def serve_system(middleware=None):
    system_manager = SystemManager()

    if middleware is None:
        middleware = get_default_middleware()
    server_manager = ServerManager(middleware=middleware)
    server_manager.register_endpoints(system_manager.get_default_endpoints())

    return server_manager.get_server()
