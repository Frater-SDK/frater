class Factory:
    def __getitem__(self, key):
        return self.get(key)

    def __init__(self):
        self.factory_map = dict()

    def __contains__(self, item):
        return item in self.factory_map

    def register(self, key):
        def wrapper(value):
            if key in self.factory_map:
                if self.factory_map[key] is not value:
                    raise KeyError(f'{key} already exists')
            else:
                self.factory_map[key] = value
            return value

        return wrapper

    def register_item(self, key, value):
        return self.register(key)(value)

    def unregister(self, key):
        if key not in self.factory_map:
            raise KeyError(f'{key} does not exist')

        del self.factory_map[key]

    def get(self, key):
        return self.factory_map[key]

    def get_registered_keys(self):
        return list(self.factory_map.keys())

    def get_registered_values(self):
        return list(self.factory_map.values())
