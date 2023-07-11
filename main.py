# -*- coding: utf-8 -*-
import argparse

import config
from convert import convert_video_to_frames


# main function
def main():
    # settings
    argument_parser = argparse.ArgumentParser()

    # create arguments
    argument_parser.add_argument('-i', '--input',
                                 type=str,
                                 default=config.PARAMETER['input_video'],
                                 help='path to input video file')

    argument_parser.add_argument('-o', '--output',
                                 type=str,
                                 default=config.PARAMETER['output_folder'],
                                 help='path to output frames directory')

    argument_parser.add_argument('-p', '--prefix',
                                 type=str,
                                 default=config.PARAMETER['name_prefix'],
                                 help='frame name prefix')

    argument_parser.add_argument('-f', '--format',
                                 type=str,
                                 default=config.PARAMETER['frame_format'],
                                 help='frame as image format')

    argument_parser.add_argument('-s', '--start',
                                 type=int,
                                 default=config.PARAMETER['start_frame'],
                                 help='start frame index')

    argument_parser.add_argument('-e', '--end',
                                 type=int,
                                 default=config.PARAMETER['end_frame'],
                                 help='end frame index')

    # parse arguments
    arguments = argument_parser.parse_args()

    # convert video to frames
    convert_video_to_frames(input_video=arguments.input, output_folder=arguments.output,
                            name_prefix=arguments.prefix, frame_format=arguments.format,
                            start_frame=arguments.start, end_frame=arguments.end)


# main
if __name__ == '__main__':
    main()
