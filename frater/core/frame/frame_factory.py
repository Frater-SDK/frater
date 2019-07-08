from typing import Dict

from .frame import Frame, CroppedFrame
from .frame_defaults import FRAME_JSON_DEFAULT, CROPPED_FRAME_JSON_DEFAULT
from .modality import Modality
from ..bounding_box import json_to_bounding_box, bounding_box_to_json
from ...validation.json import validate_json

__all__ = ['frame_to_json', 'cropped_frame_to_json', 'json_to_frame', 'json_to_cropped_frame']


def frame_to_json(frame: Frame):
    return {
        'data_type': 'frame',
        'source_video': frame.source_video,
        'modality': frame.modality.name,
        'index': frame.index,
        'timestamp': frame.timestamp,
        'width': frame.width,
        'height': frame.height
    }


def cropped_frame_to_json(frame: CroppedFrame):
    frame_json = frame_to_json(frame)
    frame_json.update({
        'data_type': 'cropped_frame',
        'source_location': bounding_box_to_json(frame.source_location)
    })
    return frame_json


@validate_json(default=FRAME_JSON_DEFAULT, completion=True)
def json_to_frame(frame_json: Dict) -> Frame:
    source_video = frame_json['source_video']
    index = frame_json['index']
    timestamp = frame_json['timestamp']
    modality = Modality[frame_json['modality']]

    return Frame(None, modality, index, source_video, timestamp)


@validate_json(default=CROPPED_FRAME_JSON_DEFAULT, completion=True)
def json_to_cropped_frame(frame_json: Dict) -> CroppedFrame:
    frame = json_to_frame(frame_json)
    source_location = json_to_bounding_box(frame_json['source_location'])

    return frame.crop(source_location)
