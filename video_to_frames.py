# -*- coding: utf-8 -*-

import argparse
import os

import cv2


# main function
def main():
    # settings
    argument_parser = argparse.ArgumentParser()

    # create arguments
    argument_parser.add_argument('-i', '--input',
                                 type=str,
                                 default='video.avi',
                                 help='path to video file')
    argument_parser.add_argument('-o', '--output',
                                 type=str,
                                 default='frames',
                                 help='path to output frames directory')
    argument_parser.add_argument('-p', '--prefix',
                                 type=str,
                                 default='',
                                 help='frame prefix')
    argument_parser.add_argument('-f', '--format',
                                 type=str,
                                 default='jpg',
                                 help='frame as image format')
    argument_parser.add_argument('-s', '--start',
                                 type=int,
                                 default=0,
                                 help='start frame index')
    argument_parser.add_argument('-e', '--end',
                                 type=int,
                                 default=None,
                                 help='end frame index')

    # parse arguments
    arguments = argument_parser.parse_args()

    # convert video to frames
    video_to_frames(input_video=arguments.input, output_folder=arguments.output,
                    name_prefix=arguments.prefix, frame_format=arguments.format,
                    start_frame=arguments.start, end_frame=arguments.end)


# convert video to frames function
def video_to_frames(input_video, output_folder, name_prefix, frame_format, start_frame=0, end_frame=None):
    # info
    print('input: "{input}"'.format(input=input_video))
    print('output: "{output}"'.format(output=output_folder))
    print('prefix: "{prefix}"'.format(prefix=name_prefix))
    print('format: "{format}"'.format(format=frame_format))
    print('start: "{start}"'.format(start=start_frame))
    if end_frame is not None:
        print('end: "{end}"'.format(end=end_frame))

    # check output exists
    if not os.path.exists(output_folder):
        print('"{output}" directory does not exist.'.format(output=output_folder))
        os.makedirs(output_folder)
        print('"{output}" directory is created.'.format(output=output_folder))

    # capture video
    print('Converting is started.')
    video_capture = cv2.VideoCapture(filename=input_video)

    # read frame
    print('"{input}" is reading.'.format(input=input_video))
    success, frame = video_capture.read()

    # loop for frames
    frame_count = 0
    while success:
        if ((end_frame is not None) and (start_frame <= frame_count <= end_frame)) \
                or ((end_frame is None) and (start_frame <= frame_count)):
            frame_file_name = '{prefix}{frame_count:05d}.{format}'.format(prefix=name_prefix,
                                                                          frame_count=frame_count,
                                                                          format=frame_format)

            # save frame as image
            save_image(image_data=frame, image_file_name=frame_file_name, image_directory_path=output_folder)

        # read next frame
        success, frame = video_capture.read()
        frame_count += 1

    print('Converting is finished.')


# save image data as image file function
def save_image(image_data, image_file_name, image_directory_path, info=True):
    image_file_path = os.path.join(image_directory_path, image_file_name)
    cv2.imwrite(image_file_path, image_data)
    if info:
        print('"{image_file}" is saved into "{image_directory}".'.format(image_file=image_file_name,
                                                                         image_directory=image_directory_path))


# main
if __name__ == '__main__':
    main()
