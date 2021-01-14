# imports
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

    # parse arguments
    arguments = argument_parser.parse_args()

    # convert video to frames
    video_to_frames(input=arguments.input, output=arguments.output, prefix=arguments.prefix, format=arguments.format)


# convert video to frames function
def video_to_frames(input, output, prefix, format, start=0, end=None):
    # info
    print('input: "{input}"'.format(input=input))
    print('output: "{output}"'.format(output=output))
    print('prefix: "{prefix}"'.format(prefix=prefix))
    print('format: "{format}"'.format(format=format))
    print('start: "{start}"'.format(start=start))
    if end is not None:
        print('end: "{end}"'.format(end=end))

    # check output exists
    if not os.path.exists(output):
        print('"{output}" directory does not exist.'.format(output=output))
        os.makedirs(output)
        print('"{output}" directory is created.'.format(output=output))

    # capture video
    print('Converting is started.')
    video_capture = cv2.VideoCapture(input)

    # read frame
    print('"{input}" is reading.'.format(input=input))
    success, frame = video_capture.read()

    # loop for frames
    frame_count = 0
    while success:
        if ((end is not None) and (start <= frame_count <= end)) or ((end is None) and (start <= frame_count)):
            frame_file_name = '{prefix}{frame_count:05d}.{format}'.format(prefix=prefix,
                                                                          frame_count=frame_count,
                                                                          format=format)

            # save frame as image
            save_image(image_data=frame, image_file_name=frame_file_name, image_directory_path=output)

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
