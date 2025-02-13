import logging
from pathlib import Path
import cv2
from config import DEFAULT


def process(input: Path = DEFAULT["input"], output: Path = DEFAULT["output"], prefix: str = DEFAULT["prefix"],
            format: str = DEFAULT["format"], start: int = DEFAULT["start"], end: int | None = DEFAULT["end"]):
    """converts a video file into individual frames and saves them as images"""

    logging.info("Processing started...")

    # open the video file
    capture = cv2.VideoCapture(filename=str(input))

    if not capture.isOpened():
        logging.error("Error: Unable to open video file '{input}'".format(input=input))
        return

    # read the first frame
    success, frame = capture.read()

    if not success:
        logging.error("Error: Unable to read frames from '{input}'".format(input=input))
        capture.release()
        return

    # Frame counter
    count: int = 0

    while success:
        # save frame only if it falls within the specified range
        if count >= start and (end is None or count <= end):
            file_name: str = "{prefix}_{count:05d}.{format}".format(prefix=prefix, count=count, format=format).lstrip("_")
            file_path: Path = output / file_name

            # save the frame as an image file
            if cv2.imwrite(filename=str(file_path), img=frame):
                logging.info("Saved frame {count} -> '{file_path}'".format(count=count, file_path=file_path))
            else:
                logging.error("Failed to save frame {count}".format(count=count))

        # read next frame
        success, frame = capture.read()
        count += 1

    # close the video file
    capture.release()

    logging.info("Processing completed.")
