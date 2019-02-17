# EC500-ffmpeg exercise

## Instructions
This script can help user convert the video to various format. For your convenience, there is a [BU introduction](https://www.youtube.com/watch?v=ufOtu6As9-M&t=89s) video that can be used for the testing. Have fun!
## Demo
Before convertion, users can set the progressive, Mbps and fps:
```
There are 2 files in queue to convert.
Press 'y' to modify the video or 'n' to use default value.
y
Please input the progressive for BU.mp4
720
Please input the Mbps value for BU.mp4
2
Pleast input the fps value for BU.mp4
30
Your vedio BU.mp4convertion method is 720 p 2 Mbps 30 fps.
Please input the progressive for BU_copy.mp4
480
Please input the Mbps value for BU_copy.mp4
1
Pleast input the fps value for BU_copy.mp4
20
Your vedio BU_copy.mp4convertion method is 480 p 1 Mbps 20 fps.
BU.mp4 converted successfully.
1 video is in processing.
BU_copy.mp4 converted successfully.
Convertion finished.
```
If user choose not to set these values, it will use default value: 720P, 2Mbps and 30fps:
```
There are 2 files in queue to convert.
Press 'y' to modify the video or 'n' to use default value.
n
2 videos are in processing.
BU_copy.mp4 converted successfully.
1 video is in processing.
BU.mp4 converted successfully.
0 videos are in processing.
```