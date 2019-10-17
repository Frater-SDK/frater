from dataclasses import dataclass
from typing import Tuple

from . import get_bounding_box_summary
from ...logging import get_summary


@dataclass
class BoundingBox:
    x: float = 0.0
    y: float = 0.0
    w: float = 0.0
    h: float = 0.0
    confidence: float = 0.0
    frame_index: int = 0

    def __add__(self, other: 'BoundingBox') -> 'BoundingBox':
        x = min(self.x_0, other.x_0)
        y = min(self.y_0, other.y_0)
        w = max(self.x_1, other.x_1) - x
        h = max(self.y_1, other.y_1) - y
        confidence = max(self.confidence, other.confidence)
        frame_index = self.frame_index
        return BoundingBox(x, y, w, h, confidence, frame_index)

    @property
    def x_0(self) -> float:
        return self.x

    @property
    def y_0(self) -> float:
        return self.y

    @property
    def width(self) -> float:
        return self.w

    @property
    def height(self) -> float:
        return self.h

    @property
    def x_1(self) -> float:
        return self.x_0 + self.w

    @property
    def y_1(self) -> float:
        return self.y_0 + self.h

    @property
    def center(self) -> Tuple[float, float]:
        return self.x + (self.w / 2), self.y + (self.h / 2)

    def summary(self, multiline=True):
        return get_summary(self, get_bounding_box_summary, multiline)

    def get_corners(self):
        return self.x_0, self.y_0, self.x_1, self.y_1

    def area(self):
        return self.width * self.height

    def union(self, other: 'BoundingBox') -> 'BoundingBox':
        return self + other

    def intersect(self, other: 'BoundingBox') -> 'BoundingBox':
        x = max(self.x_0, other.x_0)
        y = max(self.y_0, other.y_0)
        w = max(min(self.x_1, other.x_1) - x, 0.0)
        h = max(min(self.y_1, other.y_1) - y, 0.0)

        confidence = max(self.confidence, other.confidence)
        frame = self.frame_index
        return BoundingBox(x, y, w, h, confidence, frame)

    @classmethod
    def init_from_corners(cls, corners: Tuple[float, float, float, float],
                          confidence: float = 0.0, frame_index: int = 0) -> 'BoundingBox':
        x_0, y_0, x_1, y_1 = corners
        width = x_1 - x_0
        height = y_1 - y_0
        return BoundingBox(x_0, y_0, width, height, confidence, frame_index)

    @classmethod
    def init_from_center(cls, center: Tuple[float, float], width: float, height: float,
                         confidence: float = 0.0, frame_index: int = 0) -> 'BoundingBox':
        x = center[0] - (width / 2)
        y = center[1] - (height / 2)
        return BoundingBox(x, y, width, height, confidence, frame_index)
