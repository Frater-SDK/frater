import copy
import functools

from .error import ValidationError
from ..core import JSON_DEFAULTS


def validate_json(_func=None, default=True, data_type=None):
    def decorator_validate(func):
        @functools.wraps(func)
        def wrapper_validate(data):
            if default:
                data = add_defaults(copy.deepcopy(data), data_type)
            else:
                validate_helper(data, data_type)
            return func(data)

        return wrapper_validate

    if _func is None:
        return decorator_validate
    else:
        return decorator_validate(_func)


def validate_helper(data, data_type):
    defaults = get_defaults(data_type)
    for key, value in defaults.items():
        if key not in data:
            raise ValidationError(
                'Key {} not found in {} Object'.format(key, data_type))
        elif type(value) != type(data[key]):
            raise ValidationError(
                'Key {} is invalid type: default - {}, data - {}'.format(
                    key, type(value), type(data[key])
                )
            )


def get_defaults(data_type):
    return JSON_DEFAULTS[data_type]


def add_defaults(data, data_type):
    defaults = get_defaults(data_type)

    default_keys = set(defaults.keys())
    data_keys = set(data.keys())
    default_keys.difference_update(data_keys)

    for key in default_keys:
        data[key] = defaults[key]

    return data
