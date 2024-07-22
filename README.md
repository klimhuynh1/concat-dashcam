
# concat-dashcam

This Python script is designed specifically for concatenating front and rear dashcam videos into two separate files using FFmpeg. It creates two text files, `front_input.txt` and `rear_input.txt`, which are then used as input to the FFmpeg command.

  

## Requirements

concat-dashcam requires [Python 3+](https://www.python.org/downloads/) and [FFmpeg](https://ffmpeg.org/download.html) installed.

  

## Usage

1. Place your dashcam videos into a directory named `concat` in the same directory as the Python script.

2. Run the script using the following command:

	```bash
	python concat_dashcam.py
	```

3. The script will create two output files, concat_front.mp4 and concat_rear.mp4, containg concatenated front and rear dashcam videos, respectively.

  

## Notes

- This script has only been tested on dashcam videos taken on the VIOFO A129 Plus.
