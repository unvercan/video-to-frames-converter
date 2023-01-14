# -*- coding: utf-8 -*-

import argparse
import os

import cv2

# file path
PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))

# default parameters
PARAMETER = {
    'input_video': os.path.join(PROJECT_FOLDER, 'input.avi'),
    'output_folder': os.path.join(PROJECT_FOLDER, 'frames'),
    'name_prefix': '',
    'frame_format': 'jpg',
    'start_frame': 0,
    'end_frame': None
}


# main function
def main():
    # settings
    argument_parser = argparse.ArgumentParser()

    # create arguments
    argument_parser.add_argument('-i', '--input',
                                 type=str,
                                 default=PARAMETER['input_video'],
                                 help='path to video file')

    argument_parser.add_argument('-o', '--output',
                                 type=str,
                                 default=PARAMETER['output_folder'],
                                 help='path to output frames directory')

    argument_parser.add_argument('-p', '--prefix',
                                 type=str,
                                 default=PARAMETER['name_prefix'],
                                 help='frame name prefix')

    argument_parser.add_argument('-f', '--format',
                                 type=str,
                                 default=PARAMETER['frame_format'],
                                 help='frame as image format')

    argument_parser.add_argument('-s', '--start',
                                 type=int,
                                 default=PARAMETER['start_frame'],
                                 help='start frame index')

    argument_parser.add_argument('-e', '--end',
                                 type=int,
                                 default=PARAMETER['end_frame'],
                                 help='end frame index')

    # parse arguments
    arguments = argument_parser.parse_args()

    # convert video to frames
    convert_video_to_frames(input_video=arguments.input, output_folder=arguments.output,
                            name_prefix=arguments.prefix, frame_format=arguments.format,
                            start_frame=arguments.start, end_frame=arguments.end)


# convert video to frames function
def convert_video_to_frames(input_video=PARAMETER['input_video'], output_folder=PARAMETER['output_folder'],
                            name_prefix=PARAMETER['name_prefix'], frame_format=PARAMETER['frame_format'],
                            start_frame=PARAMETER['start_frame'], end_frame=PARAMETER['end_frame']):
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
            save_image_file(image_data=frame, image_file_name=frame_file_name, directory_path=output_folder)

        # read next frame
        success, frame = video_capture.read()
        frame_count += 1

    print('Converting video to frames is finished.')


# save image data as image file function
def save_image_file(image_data, image_file_name, directory_path, show_info=True):
    image_file_path = os.path.join(directory_path, image_file_name)
    cv2.imwrite(image_file_path, image_data)
    if show_info:
        print('"{image_file_name}" file is saved into "{directory_path}" directory.'.format(
            image_file_name=image_file_name,
            directory_path=directory_path))


# main
if __name__ == '__main__':
    main()
