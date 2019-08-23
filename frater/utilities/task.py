from .stream import StreamState


def mark_active(fn):
    def decorator(self, *args, **kwargs):
        self.active = True
        out = fn(self, *args, **kwargs)
        self.active = False
        return out

    return decorator


def is_end_of_sequence(data):
    return type(data) is StreamState and data == StreamState.EOS
