from frater.factory.factory import Factory


class ObjectFactory(Factory):
    def __init__(self, base_type: type = object):
        super(ObjectFactory, self).__init__()
        self._base_type = base_type

    def get_registered_objects(self):
        return self.get_registered_values()

    def register(self, key: str):
        def wrapper(derived: type):
            if not issubclass(derived, self._base_type):
                raise TypeError(f'{derived} is not a subclass of {self._base_type}')
            elif key in self.factory_map:
                if self.factory_map[key] is not derived:
                    raise KeyError(f'{key} already exists')
            else:
                self.factory_map[key] = derived
            return derived

        return wrapper

    def register_class(self, key: str, derived: type):
        self.register(key)(derived)
