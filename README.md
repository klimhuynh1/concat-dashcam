# concat-dashcam

Dashcams often split recordings into several short video files. This script merges the front and rear dashcam videos into two single files.

The Python script uses FFmpeg to combine front and rear dashcam videos. It creates two text files, front_input.txt and rear_input.txt, which FFmpeg uses to generate the final videos.

## Requirements

concat-dashcam requires [Python 3+](https://www.python.org/downloads/) and [FFmpeg](https://ffmpeg.org/download.html) installed.

## Usage

1. Place your dashcam videos into a directory named `concat` in the same directory as the Python script.

2. Run the script using the following command:

	```bash
	python concat_dashcam.py
	```

3. The script will create two output files, concat_front.mp4 and concat_rear.mp4, containing concatenated front and rear dashcam videos, respectively.
## Notes

- This script was built for and tested on dashcam videos taken with the VIOFO A129 Plus.
