from dataclasses import dataclass

from .temporal_range_summary import get_temporal_range_summary
from ...logging import get_summary


@dataclass
class TemporalRange:
    start_frame: int = 0
    end_frame: int = 0

    def summary(self, multiline=True):
        return get_summary(self, get_temporal_range_summary, multiline)

    def __len__(self):
        return max(0, self.end_frame - self.start_frame + 1)

    def __contains__(self, item: int):
        return self.start_frame <= item <= self.end_frame

    def __iter__(self):
        for i in range(self.start_frame, self.end_frame + 1):
            yield i

    def union(self, other: 'TemporalRange'):
        return TemporalRange(min(self.start_frame, other.start_frame), max(self.end_frame, other.end_frame))

    def intersect(self, other: 'TemporalRange'):
        return TemporalRange(max(self.start_frame, other.start_frame), min(self.end_frame, other.end_frame))
