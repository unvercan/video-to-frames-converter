import argparse
import logging
from pathlib import Path

from app import process
from config import DEFAULT

if __name__ == "__main__":
    # configure logging
    logging.basicConfig(level=logging.INFO, format=DEFAULT["logging_format"])

    # command-line argument parser
    parser = argparse.ArgumentParser()

    # parsing command-line arguments
    parser.add_argument("-i", "--input", type=Path, default=DEFAULT["input"], help="path to input video file")
    parser.add_argument("-o", "--output", type=Path, default=DEFAULT["output"], help="path to output frames directory")
    parser.add_argument("-p", "--prefix", type=str, default=DEFAULT["prefix"], help="frame name prefix")
    parser.add_argument("-f", "--format", type=str, default=DEFAULT["format"], help="frame as image format")
    parser.add_argument("-s", "--start", type=int, default=DEFAULT["start"], help="start frame index")
    parser.add_argument("-e", "--end", type=int, default=DEFAULT["end"], help="end frame index")

    arguments = parser.parse_args()

    logging.info("Arguments: input='{input}' output:'{output}' prefix:'{prefix} format:'{format} start:'{start} end:'{end}'"
                 .format(input=arguments.input, output=arguments.output, prefix=arguments.prefix, format=arguments.format, start=arguments.start, end=arguments.end))

    # check if the input file exists
    if not arguments.input.exists():
        logging.error("Error: Input file '{input}' does not exist.".format(input=arguments.input))
        exit(1)

    # ensure the output directory exists
    arguments.output.mkdir(parents=True, exist_ok=True)

    # process
    process(input=arguments.input, output=arguments.output, prefix=arguments.prefix, format=arguments.format, start=arguments.start, end=arguments.end)
