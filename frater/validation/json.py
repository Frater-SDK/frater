import copy
import functools

from .error import ValidationError


def validate_json(_func=None, default=None, completion=True):
    def decorator_validate(func):
        @functools.wraps(func)
        def wrapper_validate(data):
            if completion:
                data = add_defaults(copy.deepcopy(data), default)
            else:
                validate_helper(data, default)
            return func(data)

        return wrapper_validate

    if _func is None:
        return decorator_validate
    else:
        return decorator_validate(_func)


def validate_helper(data, default):
    for key, value in default.items():
        if key not in data:
            raise ValidationError(
                'Key {} not found in {} Object'.format(key, type(data)))
        elif type(value) != type(data[key]):
            raise ValidationError(
                'Key {} is invalid type: default - {}, data - {}'.format(
                    key, type(value), type(data[key])
                )
            )


def add_defaults(data, default):
    default_keys = set(default.keys())
    data_keys = set(data.keys())
    default_keys.difference_update(data_keys)

    for key in default_keys:
        data[key] = default[key]

    return data
