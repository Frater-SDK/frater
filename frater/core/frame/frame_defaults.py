from ..bounding_box import bounding_box_defaults

FRAME_JSON_DEFAULT = {
    'source_video': '',
    'modality': 'RGB',
    'index': 0,
    'timestamp': '',
    'width': 0,
    'height': 0
}

CROPPED_FRAME_JSON_DEFAULT = FRAME_JSON_DEFAULT.copy()
CROPPED_FRAME_JSON_DEFAULT.update({'source_location': bounding_box_defaults.BOUNDING_BOX_JSON_DEFAULT})
