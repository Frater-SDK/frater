from typing import Dict

from .video import Video
from .video_defaults import VIDEO_JSON_DEFAULT
from ...validation.json import validate_json


def video_to_json(video: Video) -> Dict:
    return {
        'data_type': 'video',
        'video_name': video.video_name,
        'experiment': video.experiment,
        'width': video.width,
        'height': video.height,
        'framerate': video.framerate,
        'start_frame': video.start_frame,
        'end_frame': video.end_frame
    }


@validate_json(default=VIDEO_JSON_DEFAULT, completion=True)
def json_to_video(video: Dict) -> Video:
    return Video(video['video_name'],
                 video['experiment'],
                 video['width'],
                 video['height'],
                 video['framerate'],
                 video['start_frame'],
                 video['end_frame'])
