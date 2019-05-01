class TemporalRange:
    def __init__(self, start_frame: int = 0, end_frame: int = 0):
        self._start_frame = start_frame
        self._end_frame = end_frame

    def __str__(self):
        return f'Start Frame: {self.start_frame} End Frame: {self.end_frame}'

    def __eq__(self, other: 'TemporalRange') -> bool:
        return self.start_frame == other.start_frame and self.end_frame == other.end_frame

    @property
    def start_frame(self) -> int:
        return self._start_frame

    @property
    def end_frame(self) -> int:
        return self._end_frame
