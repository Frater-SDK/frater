from typing import Dict, Union

from frater.validation.json import validate_json
from .temporal_range import TemporalRange
from .temporal_range_defaults import TEMPORAL_RANGE_JSON_DEFAULT

__all__ = ['json_to_temporal_range', 'temporal_range_to_json']


@validate_json(default=TEMPORAL_RANGE_JSON_DEFAULT, completion=True)
def json_to_temporal_range(temporal_range: Union[None, Dict]) -> TemporalRange:
    start_frame = temporal_range['start_frame']
    end_frame = temporal_range['end_frame']
    return TemporalRange(start_frame, end_frame)


def temporal_range_to_json(temporal_range: TemporalRange) -> Union[Dict, None]:
    return {
        'data_type': 'temporal_range',
        'start_frame': temporal_range.start_frame,
        'end_frame': temporal_range.end_frame
    }
