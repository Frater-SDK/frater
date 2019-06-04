import json


def is_json_serializable(x):
    try:
        json.dumps(x)
        return True
    except:
        return False


def is_json_deserializable(x):
    try:
        json.loads(x)
        return True
    except:
        return False
