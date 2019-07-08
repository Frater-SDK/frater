from enum import Enum

from typing import Dict


class StreamState(Enum):
    STOP = 0
    START = 1
    EOS = 2  # end of sequence


def json_to_stream_state(data: Dict):
    return StreamState(data['stream_state'])


def stream_state_to_json(state: StreamState):
    return {'stream_state': state.value}
