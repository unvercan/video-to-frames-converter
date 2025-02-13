from pathlib import Path

# default values
DEFAULT: dict = {
    "input": Path.cwd() / "input.mp4",
    "output": Path.cwd() / "frames",
    "prefix": "",
    "format": "jpg",
    "start": 0,
    "end": None,
    "datetime_format": "%Y%m%d_%H%M%S",
    "logging_format": "%(asctime)s - %(levelname)s - %(message)s",
}
