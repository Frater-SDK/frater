from dataclasses import dataclass

from .video_summary import get_video_summary
from ...logging import get_summary


@dataclass
class Video:
    video_name: str = ''
    experiment: str = ''
    width: int = 0
    height: int = 0
    framerate: float = 30.0
    start_frame: int = 1
    end_frame: int = 1

    @property
    def size(self):
        return self.width, self.height

    def summary(self, multiline=True):
        return get_summary(self, get_video_summary, multiline)

    def __len__(self):
        return self.end_frame - self.start_frame
