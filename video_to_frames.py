# imports
from argparse import ArgumentParser
from os import path, makedirs
import cv2 as cv


# main function
def main():
    # settings
    argument_parser = ArgumentParser()

    # arguments
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
    argument_parser.add_argument('-f', '--image-format',
                                 type=str,
                                 default='jpg',
                                 help='frame as image format')

    # arguments
    arguments = argument_parser.parse_args()

    # parameters
    input = arguments.input_base
    output = arguments.output_base
    prefix = arguments.prefix
    format = arguments.image_format

    # convert video to frames
    video_to_frames(input=input, output=output, prefix=prefix, format=format)


# convert video to frames function
def video_to_frames(input, output, prefix, format):
    # info
    print('Video to Frames Converting')
    print('*' * 50)
    print('input: "{input}"'.format(input=input))
    print('output: "{output}"'.format(output=output))
    print('prefix: "{prefix}"'.format(prefix=prefix))
    print('format: "{format}"'.format(format=format))

    # check output exists
    if not path.exists(output):
        print('"{output}" directory does not exist.'.format(output=output))
        makedirs(output)
        print('"{output}" directory is created.'.format(output=output))

    # capture video
    print('Converting is started.')
    video_capture = cv.VideoCapture(input)

    # read frame
    print('"{input}" is reading.'.format(input=input))
    success, frame = video_capture.read()

    # loop for frames
    frame_count = 0
    while success:
        # save frame as image
        frame_file_name = '{prefix}{frame_count:05d}.{format}'.format(prefix=prefix, frame_count=frame_count,
                                                                      format=format)
        frame_path = path.join(output, frame_file_name)
        cv.imwrite(frame_path, frame)
        print('"{frame_file}" is saved into "{frames_directory}".'.format(frame_file=frame_file_name,
                                                                          frames_directory=output))

        # read next frame
        success, frame = video_capture.read()
        frame_count += 1

    print('*' * 50)
    print('Converting is finished.')


# main
if __name__ == '__main__':
    main()
