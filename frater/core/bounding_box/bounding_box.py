class BoundingBox:
    def __init__(self, x: float = 0, y: float = 0, w: float = 0, h: float = 0,
                 confidence: float = 0.0, frame: int = 0):
        self._x = x
        self._y = y

        self._w = w
        self._h = h

        self._confidence = confidence
        self._frame = frame

    def __eq__(self, other: 'BoundingBox') -> bool:
        return (self.x == other.x and
                self.y == other.y and
                self.w == other.w and
                self.h == other.h and
                self.confidence == other.confidence and
                self.frame == other.frame)

    @property
    def x(self) -> float:
        return self._x

    @property
    def x_0(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @property
    def y_0(self) -> float:
        return self._y

    @property
    def w(self) -> float:
        return self._w

    @property
    def width(self) -> float:
        return self._w

    @property
    def h(self) -> float:
        return self._h

    @property
    def height(self) -> float:
        return self._h

    @property
    def x_1(self) -> float:
        return self.x_0 + self.w

    @property
    def y_1(self) -> float:
        return self.y_0 + self.h

    @property
    def confidence(self):
        return self._confidence

    @property
    def frame(self) -> int:
        return self._frame
