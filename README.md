# Video Frame Extractor

This Python script is designed to extract frames from video files and organize them into separate directories for each video. It supports video formats such as `.mp4` and `.avi`. The script extracts frames at intervals and then distributes these frames into three parts for each video, facilitating easier management and analysis of video content.

## Features

- **Frame Extraction:** Extracts frames from each video file at specified intervals.
- **Automatic Directory Management:** Creates a directory for each video file and further organizes extracted frames into three parts.
- **Supported Video Formats:** Works with `.mp4` and `.avi` video formats.

## Requirements

- Python 3.x
- OpenCV library (cv2)
- os and shutil modules (included with Python)

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install OpenCV if you haven't already. You can install it using pip:

   ```sh
   pip install opencv-python
   ```
