# -*- coding: utf-8 -*-

import os

import cv2

import config
from image import save_image_file


# convert video to frames function
def convert_video_to_frames(input_video=config.PARAMETER['input_video'],
                            output_folder=config.PARAMETER['output_folder'],
                            name_prefix=config.PARAMETER['name_prefix'],
                            frame_format=config.PARAMETER['frame_format'],
                            start_frame=config.PARAMETER['start_frame'],
                            end_frame=config.PARAMETER['end_frame']):
    # show info
    print('Video To Frames Converter:')
    print('input video: "{input_video}"'.format(input_video=input_video))
    print('output folder: "{output_folder}"'.format(output_folder=output_folder))
    print('name prefix: "{name_prefix}"'.format(name_prefix=name_prefix))
    print('frame format: "{frame_format}"'.format(frame_format=frame_format))
    print('start frame: {start_frame}'.format(start_frame=start_frame))
    if end_frame is not None:
        print('end frame: {end_frame}'.format(end_frame=end_frame))

    # check input video file path exists
    if not os.path.exists(input_video):
        print('"{input_video}" does not exist.'.format(input_video=input_video))
        return

    # check output folder exists
    if not os.path.exists(output_folder):
        print('"{output_folder}" directory does not exist.'.format(output_folder=output_folder))
        os.makedirs(output_folder)
        print('"{output_folder}" directory is created.'.format(output_folder=output_folder))

    # capture video
    print('Converting video to frames is started.')
    video_capture = cv2.VideoCapture(filename=input_video)

    # read frames
    print('"{input_video}" file is reading.'.format(input_video=input_video))
    success, frame = video_capture.read()

    # loop for frames
    frame_count = 0
    while success:
        if ((end_frame is not None) and (start_frame <= frame_count <= end_frame)) \
                or ((end_frame is None) and (start_frame <= frame_count)):
            frame_file_name = '{name_prefix}{frame_count:05d}.{frame_format}'.format(name_prefix=name_prefix,
                                                                                     frame_count=frame_count,
                                                                                     frame_format=frame_format)

            # save frame as image file
            save_image_file(image_data=frame, image_file_name=frame_file_name,
                            directory_path=output_folder, show_info=config.PARAMETER['show_info'])

        # read next frame
        success, frame = video_capture.read()
        frame_count += 1

    print('Converting video to frames is finished.')
