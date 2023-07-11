# -*- coding: utf-8 -*-
import os

import cv2

import config


# save image data as image file function
def save_image_file(image_data, image_file_name,
                    directory_path=config.PARAMETER['output_folder'],
                    show_info=config.PARAMETER['show_info']):
    image_file_path = os.path.join(directory_path, image_file_name)
    cv2.imwrite(image_file_path, image_data)

    if show_info:
        print('"{image_file_name}" file is saved into "{directory_path}" directory.'.format(
            image_file_name=image_file_name,
            directory_path=directory_path))
