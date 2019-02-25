#!/usr/bin/env python3.7.2
# encoding: utf-8
#Author - Yicun Hou
import os
import queue
import threading
import pytest
import subprocess


def read_file(filepath):
    '''List all the mp4 files'''

    file_list = os.listdir(filepath)
    video_list = []
    for file in file_list:
        if file.endswith('.mp4'):
            video_list.append(file)
    return video_list



def vedio_conv(video_name, progressive, Mbps, fps, name):
    video = video_name
    subprocess.check_call(['ffmpeg', '-i' , video, '-b:v' , Mbps+'M', '-s', 'hd'+progressive, video[0:-4]+name])
    #return video


def main():
    path = os.getcwd()
    all_video = read_file(path)
    q = queue.Queue()
    threads = []
    # Put videos in queue
    for video in all_video:
        q.put(video)

    # Modify the convertion method
    while q.qsize() != 0:
        video = q.get()
        threads.append(threading.Thread(target=vedio_conv, kwargs={'video_name':video,'progressive':'720', 'Mbps':'2', 'fps':'30', 'name':'720.avi'}))
        threads.append(threading.Thread(target=vedio_conv, kwargs={'video_name':video,'progressive':'480', 'Mbps':'1', 'fps':'30', 'name':'480.mp4'}))

    # Start convertion threads
    for thread in threads:
        thread.start()
    #print(str(COUNTER) + ' videos are in processing.')


if __name__ == '__main__':
    main()
