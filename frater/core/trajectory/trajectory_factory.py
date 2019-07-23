from typing import Dict

from frater.core.temporal_range import TemporalRange
from .trajectory import Trajectory
from .trajectory_defaults import TRAJECTORY_JSON_DEFAULT
from ..bounding_box.bounding_box_factory import *
from ..temporal_range.temporal_range_factory import *
from ...validation.json import validate_json

__all__ = ['json_to_trajectory', 'trajectory_to_json',
           'diva_format_to_trajectory']


@validate_json(default=TRAJECTORY_JSON_DEFAULT, completion=True)
def json_to_trajectory(trajectory: Dict) -> Trajectory:
    bounding_boxes = [json_to_bounding_box(
        box) for box in trajectory['bounding_boxes']]
    temporal_range = json_to_temporal_range(trajectory['temporal_range'])
    return Trajectory(bounding_boxes, temporal_range)


def trajectory_to_json(trajectory: Trajectory):
    return {
        'data_type': 'trajectory',
        'bounding_boxes': [bounding_box_to_json(bounding_box)
                           for bounding_box in trajectory.bounding_boxes],
        'temporal_range': temporal_range_to_json(trajectory.temporal_range)
    }


def diva_format_to_trajectory(trajectory: Dict) -> Trajectory:
    bounding_boxes = list()
    for bounding_box in trajectory.items():
        if 'boundingBox' not in bounding_box[1] or 'presenceConf' not in bounding_box[1]:
            continue
        bounding_boxes.append(diva_format_to_bounding_box(bounding_box))
    start = min(bounding_boxes, key=lambda b: b.frame).frame_index
    end = max(bounding_boxes, key=lambda b: b.frame).frame_index
    temporal_range = TemporalRange(start, end)
    return Trajectory(bounding_boxes, temporal_range)
