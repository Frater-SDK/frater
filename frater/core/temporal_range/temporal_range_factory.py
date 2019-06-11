from typing import Dict, Union

from frater.validation.json import validate_json
from .temporal_range import TemporalRange
from .temporal_range_defaults import TEMPORAL_RANGE_JSON_DEFAULT
from ..proto import core

__all__ = ['json_to_temporal_range', 'temporal_range_to_json', 'protobuf_to_temporal_range',
           'temporal_range_to_protobuf']


@validate_json(default=TEMPORAL_RANGE_JSON_DEFAULT, completion=True)
def json_to_temporal_range(temporal_range: Union[None, Dict]) -> TemporalRange:
    start_frame = temporal_range['start_frame']
    end_frame = temporal_range['end_frame']
    return TemporalRange(start_frame, end_frame)


def temporal_range_to_json(temporal_range: TemporalRange) -> Union[Dict, None]:
    return {'start_frame': temporal_range.start_frame, 'end_frame': temporal_range.end_frame}


def protobuf_to_temporal_range(temporal_range: core.TemporalRange) -> TemporalRange:
    return TemporalRange(temporal_range.start_frame, temporal_range.end_frame)


def temporal_range_to_protobuf(temporal_range: TemporalRange) -> core.TemporalRange:
    return core.TemporalRange(start_frame=temporal_range.start_frame,
                              end_frame=temporal_range.end_frame)
