class TemporalRange:
    def __init__(self, start_frame: int = 0, end_frame: int = 0):
        self._start_frame = start_frame
        self._end_frame = end_frame

    def __str__(self):
        return f'Start Frame: {self.start_frame} End Frame: {self.end_frame}'

    def __eq__(self, other: 'TemporalRange') -> bool:
        return self.start_frame == other.start_frame and self.end_frame == other.end_frame

    def __len__(self):
        return max(0, self.end_frame - self.start_frame + 1)

    def __contains__(self, item: int):
        return self.start_frame <= item <= self.end_frame

    def __iter__(self):
        for i in range(self.start_frame, self.end_frame + 1):
            yield i

    @property
    def start_frame(self) -> int:
        return self._start_frame

    @property
    def end_frame(self) -> int:
        return self._end_frame

    def union(self, other: 'TemporalRange'):
        return TemporalRange(min(self.start_frame, other.start_frame), max(self.end_frame, other.end_frame))

    def intersect(self, other: 'TemporalRange'):
        return TemporalRange(max(self.start_frame, other.start_frame), min(self.end_frame, other.end_frame))
