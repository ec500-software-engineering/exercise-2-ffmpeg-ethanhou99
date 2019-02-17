#!/usr/bin/env python3.7.2
# encoding: utf-8
#Author - Yicun Hou
import wget
import os
import queue
import threading

COUNTER = 0

def list_file(filepath):
    '''List all the mp4 files'''

    file_list = os.listdir(filepath)
    video_list = []
    for file in file_list:
        if file.endswith('.mp4'):
            video_list.append(file)
    return video_list

def vedio_conv(fileName, progressive, Mbps, fps):
    '''Convert the video files'''

    global COUNTER
    os.system('ffmpeg -i ' + fileName + ' -b:v ' + Mbps + 'M -vf fps=fps=' + fps + ' -s hd' + progressive + ' ' + fileName[0:-4] + '.avi >/dev/null 2>&1')
    print(fileName + ' converted successfully.')
    COUNTER -= 1
    if COUNTER == 1:
        print(str(COUNTER) + ' video is in processing.')
    elif COUNTER == 0:
        print("*** Convertion finished ***")
    else:
        print(str(COUNTER) + ' videos are in processing.')

def vedio_set(fileName):
    '''Set video's progressive scan, Mbps and fps'''

    print('Please input the progressive for ' + fileName)
    pro = input()
    print('Please input the Mbps value for ' + fileName)
    Mbps = input()
    print('Pleast input the fps value for ' + fileName)
    fps = input()
    print('Your vedio ' + fileName + 'convertion method is ' + pro + 'p, ' + Mbps + 'Mbps, and ' + fps + 'fps.')
    print(str(COUNTER) + ' videos are in processing.')
    return pro, Mbps, fps

def main():
    global COUNTER
    path = os.getcwd()
    all_vedio = list_file(path)
    q = queue.Queue()
    threads = []
    # Put videos in queue
    for vedio in all_vedio:
        q.put(vedio)

    COUNTER = q.qsize()
    # Modify the convertion method
    print('There are ' + str(q.qsize()) + ' files in queue to convert.')
    print("Press 'y' to modify the video or 'n' to use default value.")
    if input() == 'y':
        for video in all_vedio:
            pro, Mbps, fps = vedio_set(video)
            threads.append(threading.Thread(target=vedio_conv, kwargs={'fileName':q.get(),'progressive':pro, 'Mbps':Mbps, 'fps':fps}))
    else:
        print("You choose to use default values to convert the video(720P, 2Mbps, 30fps).")
        while q.qsize() != 0:
            threads.append(threading.Thread(target=vedio_conv, kwargs={'fileName':q.get(),'progressive':'720', 'Mbps':'2', 'fps':'30'}))
    
    # Start convertion threads
    for thread in threads:
        thread.start()
    #print(str(COUNTER) + ' videos are in processing.')


if __name__ == '__main__':
    main()