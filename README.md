# Video to Frames Converter

A Python script that extracts frames from a video file and saves them as images.

## Features

- Extracts frames from a video and saves them in a specified format.
- Allows specifying a start and end frame range.
- Uses OpenCV for video processing.
- Supports command-line arguments for flexibility.
- Creates an output directory if it doesn't exist.

## Prerequisites

Ensure you have the following installed:

- Python 3.7+
- OpenCV (`cv2`)

Install dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

Run the script using command-line arguments:

```bash
python main.py -i input.mp4 -o frames -p frame -f jpg -s 10 -e 100
```

### Command-Line Arguments:

| Argument         | Description                           | Default     |
|------------------|---------------------------------------|-------------|
| `-i`, `--input`  | Path to the input video file          | `input.mp4` |
| `-o`, `--output` | Directory to save extracted frames    | `frames/`   |
| `-p`, `--prefix` | Prefix for frame filenames            | `frame`     |
| `-f`, `--format` | Image format (e.g., jpg, png)         | `jpg`       |
| `-s`, `--start`  | Start frame index                     | `0`         |
| `-e`, `--end`    | End frame index (None for all frames) | `None`      |

## Example

Extract frames from `video.mp4`, save them as PNG, starting from frame 50 to 200:

```bash
python main.py -i video.mp4 -o output_frames -p img -f png -s 50 -e 200
```

## Project Structure

```
project-folder/
│── app.py          # Main processing logic
│── main.py         # CLI entry point
│── config.py       # Default configurations
│── requirements.txt # Dependencies
│── README.md       # Documentation
```

## License

This project is licensed under the MIT License.

