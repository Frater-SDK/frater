from unittest import TestCase

from frater.core.bounding_box import *


class TestBoundingBoxFunctions(TestCase):
    def test_combine_bounding_boxes(self):
        first_bounding_box = BoundingBox(10, 10, 20, 20, confidence=0.95)
        second_bounding_box = BoundingBox(20, 20, 20, 20, confidence=0.33)
        target_bounding_box = BoundingBox(10, 10, 30, 30, confidence=0.95)
        assert target_bounding_box == combine_bounding_boxes([first_bounding_box, second_bounding_box])

    def test_compute_spatial_iou(self):
        first_bounding_box = BoundingBox(10, 10, 20, 20, confidence=0.95)
        second_bounding_box = BoundingBox(20, 10, 20, 20, confidence=0.33)

        target_iou = 1.0 / 3.0
        self.assertAlmostEqual(target_iou, compute_spatial_iou(first_bounding_box, second_bounding_box))
