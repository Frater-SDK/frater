class BoundingBox:
    def __init__(self, x: float = 0, y: float = 0, w: float = 0, h: float = 0,
                 confidence: float = 0.0, frame: int = 0):
        self._x = max(x, 0.0)
        self._y = max(y, 0.0)

        self._w = max(w, 0.0)
        self._h = max(h, 0.0)

        self._confidence = confidence
        self._frame = frame

    def __eq__(self, other: 'BoundingBox') -> bool:
        return (self.x == other.x and
                self.y == other.y and
                self.w == other.w and
                self.h == other.h and
                self.confidence == other.confidence and
                self.frame == other.frame)

    def __add__(self, other: 'BoundingBox') -> 'BoundingBox':
        x = min(self.x_0, other.x_0)
        y = min(self.y_0, other.y_0)
        w = max(self.x_1, other.x_1) - x
        h = max(self.y_1, other.y_1) - y
        confidence = max(self.confidence, other.confidence)
        frame = self.frame
        return BoundingBox(x, y, w, h, confidence, frame)

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

    def get_corners(self):
        return self.x_0, self.y_0, self.x_1, self.y_1

    def area(self):
        return self.width * self.height

    def union(self, other: 'BoundingBox') -> 'BoundingBox':
        return self + other

    def intersect(self, other: 'BoundingBox') -> 'BoundingBox':
        x = max(self.x_0, other.x_0)
        y = max(self.y_0, other.y_0)
        w = min(self.x_1, other.x_1) - x
        h = min(self.y_1, other.y_1) - y

        confidence = max(self.confidence, other.confidence)
        frame = self.frame
        return BoundingBox(x, y, w, h, confidence, frame)
