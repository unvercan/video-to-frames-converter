# video-to-frames-converter

Command-line video to frame converter.

## Arguments:

* -i or --input: path to video file
* -o or --output: path to output frames directory
* -p or --prefix: frame prefix
* -f or --format: frame as image format
* -s or --start: start frame index
* -e or --end: end frame index

## Example Usage:

```
python video_to_frames.py 
    -i /home/unvercanunlu/videos/video.avi 
    -o /home/unvercanunlu/frames 
    -p frame 
    -f jpg
    -s 100
    -e 150
```
