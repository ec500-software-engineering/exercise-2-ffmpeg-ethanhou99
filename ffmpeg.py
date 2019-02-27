#!/usr/bin/env python3.7.2
# encoding: utf-8
#Author - Yicun Hou
import os
import queue
import threading
import pytest
import subprocess
import time

v1 = False
v2 = False

def read_file(filepath):
    '''List all the mp4 files'''

    file_list = os.listdir(filepath)
    video_list = []
    for file in file_list:
        if file.endswith('.avi'):
            video_list.append(file)
    return video_list


def video_conv(video_name, progressive, Mbps, name):
    global v1, v2
    video = video_name
    subprocess.check_call(['ffmpeg', '-strict', '-2', '-i' , video, '-b:v' , Mbps+'M', '-s', 'hd'+progressive, name])
    time.sleep(30)

def if_true():
    global v1, v2
    if v1 == True and v2 == True:
        return True
    else:
        return False

def main():
    global v1, v2
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
        threads.append(threading.Thread(target=video_conv, kwargs={'video_name':video,'progressive':'720', 'Mbps':'2', 'name':'BU720.mp4'}))
        threads.append(threading.Thread(target=video_conv, kwargs={'video_name':video,'progressive':'480', 'Mbps':'1', 'name':'BU480.mp4'}))

    # Start convertion threads
    for thread in threads:
        thread.start()

    v1 = True
    v2 = True
    if_true()


if __name__ == '__main__':
    main()
