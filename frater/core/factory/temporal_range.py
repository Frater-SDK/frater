from typing import Tuple, Dict, Union

from ..proto import core
from ...validation.json import validate_json

__all__ = ['json_to_temporal_range', 'temporal_range_to_json', 'protobuf_to_temporal_range',
           'temporal_range_to_protobuf']


@validate_json(default=True, data_type='temporal_range')
def json_to_temporal_range(temporal_range: Union[None, Dict]) -> Union[Tuple[int, int], None]:
    return temporal_range['start_frame'], temporal_range['end_frame']


def temporal_range_to_json(temporal_range: Union[Tuple[int, int], None]) -> Union[Dict, None]:
    return {'start_frame': temporal_range[0], 'end_frame': temporal_range[1]}


def protobuf_to_temporal_range(temporal_range: core.TemporalRange) -> Union[Tuple[int, int], None]:
    return temporal_range.start_frame, temporal_range.end_frame


def temporal_range_to_protobuf(temporal_range: Union[Tuple[int, int], None]) -> core.TemporalRange:
    return core.TemporalRange(start_frame=temporal_range[0],
                              end_frame=temporal_range[1])
