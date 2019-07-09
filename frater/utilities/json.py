import json


def is_json_serializable(x):
    try:
        json.dumps(x)
        return True
    except:
        return False


def is_json_deserializable(x, decode_type='utf-8'):
    try:
        json.loads(x.decode())
        return True
    except:
        return False
