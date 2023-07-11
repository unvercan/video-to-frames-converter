# -*- coding: utf-8 -*-

import os

# file path
PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))

# default parameters
PARAMETER = {
    'input_video': os.path.join(PROJECT_FOLDER, 'input.avi'),
    'output_folder': os.path.join(PROJECT_FOLDER, 'frames'),
    'name_prefix': '',
    'frame_format': 'jpg',
    'start_frame': 0,
    'end_frame': None,
    'show_info': True
}
