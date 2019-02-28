# EC500-ffmpeg exercise

## Instructions
This script can help users convert the video to various format. For example, the ffmepg.py can convert an .avi video to 480P and 720P. For your convenience, there is a [BU introduction](https://www.youtube.com/watch?v=ufOtu6As9-M&t=89s) video that can be used for the testing. Have fun!

## Prerequisite
Before running the profram, the ffmepg needed to be installed.

### Install homebrew
Install homebrew on your mac by running the following command on your Terminal.
```
$ /usr/bin/ruby -e “$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
### Install ffmpeg
Once you have Homebrew installed install ffmpeg from the Terminal with the following command.
```
$ brew install ffmpeg
```

### Install the project
```
git clone https://github.com/ec500-software-engineering/exercise-2-ffmpeg-ethanhou99.git
```

## Function
- The read_file() in the ffmepg.py is to read videos from folders.
- The video_conv() in the ffmepg.py is the main convert function.
- The test_ffmpeg.py is designed for the testing.

## Flow chart
![image](https://github.com/ec500-software-engineering/exercise-2-ffmpeg-ethanhou99/blob/master/flowchart.png)
