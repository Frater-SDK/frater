def mark_active(fn):
    def decorator(self, *args, **kwargs):
        self.active = True
        out = fn(self, *args, **kwargs)
        self.active = False
        return out

    return decorator
