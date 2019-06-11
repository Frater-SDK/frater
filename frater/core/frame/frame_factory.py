from typing import Dict

from .frame import Frame, CroppedFrame
from .modality import Modality
from ..bounding_box import json_to_bounding_box, bounding_box_to_json
from ...components.data_store import FrameStore

__all__ = ['frame_to_json', 'cropped_frame_to_json', 'json_to_frame', 'json_to_cropped_frame']


def frame_to_json(frame: Frame):
    return {
        'source_video': frame.source_video,
        'modality': frame.modality.name,
        'index': frame.index,
        'timestamp': frame.timestamp,
        'width': frame.width,
        'height': frame.height
    }


def cropped_frame_to_json(frame: CroppedFrame):
    frame_json = frame_to_json(frame)
    frame_json.update({'source_location': bounding_box_to_json(frame.source_location)})
    return frame_json


def json_to_frame(frame_json: Dict, frame_store: FrameStore = None) -> Frame:
    source_video = frame_json['source_video']
    index = frame_json['index']
    timestamp = frame_json['timestamp']
    modality = Modality[frame_json['modality']]
    if frame_store:
        frame = frame_store.get_frame(source_video, index, modality, timestamp)
    else:
        frame = Frame(None, modality, index, source_video, timestamp)

    return frame


def json_to_cropped_frame(frame_json: Dict) -> CroppedFrame:
    frame = json_to_frame(frame_json)
    source_location = json_to_bounding_box(frame_json['source_location'])

    return frame.crop(source_location)
