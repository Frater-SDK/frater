from PIL import ImageDraw

from frater.core import Frame, BoundingBox


def draw_bounding_box(bounding_box: BoundingBox, frame: Frame, color='red'):
    image = frame.image.copy()
    draw = ImageDraw.Draw(image)
    draw.rectangle(bounding_box.get_corners(), outline=color, width=2)
    del draw
    return Frame(image, frame.modality, frame.index, frame.source_video, frame.experiment, frame.timestamp)
