from enum import IntEnum
from typing import Dict

from ..io.deserializers import json_deserializers
from ..io.serializers import json_serializers
from ..validation.json import validate_json


class StreamState(IntEnum):
    STOP = 0
    START = 1
    END = 2  # end of sequence


STREAM_STATE_JSON_DEFAULTS = {
    'data_type': 'stream_state',
    'stream_state': 0
}


@json_deserializers.register('stream_state')
@validate_json(default=STREAM_STATE_JSON_DEFAULTS, completion=True)
def json_to_stream_state(data: Dict):
    return StreamState(data['stream_state'])


@json_serializers.register(StreamState)
def stream_state_to_json(state: StreamState):
    return {'stream_state': state.value, 'data_type': 'stream_state'}


def is_end_of_stream(data):
    return isinstance(data, StreamState) and data == StreamState.END


def is_start_of_stream(data):
    return isinstance(data, StreamState) and data == StreamState.START
