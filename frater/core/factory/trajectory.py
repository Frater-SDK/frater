from typing import Dict

from .bounding_box import *
from .temporal_range import (json_to_temporal_range,
                             temporal_range_to_json,
                             protobuf_to_temporal_range,
                             temporal_range_to_protobuf)
from ..proto import core
from ..trajectory import Trajectory

__all__ = ['json_to_trajectory', 'trajectory_to_json',
           'diva_format_to_trajectory',
           'protobuf_to_trajectory', 'trajectory_to_protobuf']


def json_to_trajectory(trajectory: Dict) -> Trajectory:
    bounding_boxes = [json_to_bounding_box(
        box) for box in trajectory['bounding_boxes']]
    temporal_range = json_to_temporal_range(trajectory['temporal_range'])
    scale = trajectory['scale']
    return Trajectory(bounding_boxes, temporal_range, scale)


def trajectory_to_json(trajectory: Trajectory):
    return {
        'bounding_boxes': [bounding_box_to_json(bounding_box)
                           for bounding_box in trajectory.bounding_boxes],
        'temporal_range': temporal_range_to_json(trajectory.temporal_range),
        'scale': trajectory.scale
    }


def diva_format_to_trajectory(trajectory: Dict) -> Trajectory:
    bounding_boxes = list()
    for bounding_box in trajectory.items():
        if 'boundingBox' not in bounding_box[1] or 'presenceConf' not in bounding_box[1]:
            continue
        bounding_boxes.append(diva_format_to_bounding_box(bounding_box))
    start = min(bounding_boxes, key=lambda b: b.frame).frame
    end = max(bounding_boxes, key=lambda b: b.frame).frame
    temporal_range = start, end
    scale = 1.0
    return Trajectory(bounding_boxes, temporal_range, scale)


def protobuf_to_trajectory(trajectory: core.Trajectory) -> Trajectory:
    bounding_boxes = [protobuf_to_bounding_box(
        bounding_box) for bounding_box in trajectory.bounding_boxes]
    temporal_range = protobuf_to_temporal_range(trajectory.temporal_range)
    scale = trajectory.scale
    return Trajectory(bounding_boxes, temporal_range, scale)


def trajectory_to_protobuf(trajectory: Trajectory):
    bounding_boxes = [bounding_box_to_protobuf(bounding_box)
                      for bounding_box in trajectory.bounding_boxes]
    temporal_range = temporal_range_to_protobuf(trajectory.temporal_range)
    return core.Trajectory(bounding_boxes=bounding_boxes,
                           temporal_range=temporal_range,
                           scale=trajectory.scale)
