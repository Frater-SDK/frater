from PIL import ImageDraw

from frater.core import Frame, BoundingBox


def draw_bounding_box(bounding_box: BoundingBox, frame: Frame, color='red'):
    image = frame.image.copy()
    draw = ImageDraw.Draw(image)
    draw.rectangle(bounding_box.get_corners(), outline=color)
    del draw
    new_frame = Frame(**frame.__dict__.copy())
    new_frame.image = image
    return new_frame
