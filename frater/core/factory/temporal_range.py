from typing import Tuple, Dict, Union

from ..proto import core

__all__ = ['json_to_temporal_range', 'temporal_range_to_json', 'protobuf_to_temporal_range',
           'temporal_range_to_protobuf']


def json_to_temporal_range(temporal_range: Union[None, Dict]) -> Union[Tuple[int, int], None]:
    if temporal_range is None:
        return None
    if 'start_frame' not in temporal_range:
        return None
    if 'end_frame' not in temporal_range:
        return None

    start, end = temporal_range['start_frame'], temporal_range['end_frame']

    if start > end:
        return None

    return start, end


def temporal_range_to_json(temporal_range: Union[Tuple[int, int], None]) -> Union[Dict, None]:
    if temporal_range is None:
        return None
    elif len(temporal_range) != 2:
        return None
    elif temporal_range[0] > temporal_range[1]:
        return None
    return {'start_frame': temporal_range[0], 'end_frame': temporal_range[1]}


def protobuf_to_temporal_range(temporal_range: core.TemporalRange) -> Union[Tuple[int, int], None]:
    if temporal_range is None:
        return None
    if temporal_range.start_frame > temporal_range.end_frame:
        return None

    return temporal_range.start_frame, temporal_range.end_frame


def temporal_range_to_protobuf(temporal_range: Union[Tuple[int, int], None]) -> core.TemporalRange:
    if temporal_range is None:
        return None
    if temporal_range is None:
        return None
    elif len(temporal_range) != 2:
        return None
    elif temporal_range[0] > temporal_range[1]:
        return None
    return core.TemporalRange(start_frame=temporal_range[0],
                              end_frame=temporal_range[1])
