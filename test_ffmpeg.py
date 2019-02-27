from ffmpeg import video_conv as convert
from ffmpeg import read_file
from pytest import approx
import subprocess
import json
import os
from pathlib import Path
import time

def atest_input_file():
    outlist = ['BU.avi']
    path = os.getcwd()
    fout = read_file(path)

    assert outlist == fout

def test_video1():
    fnin = 'BU.avi'
    fnout = 'BU480.mp4'

    orig_meta = ffprobe_sync(fnin)
    orig_duration = float(orig_meta['streams'][0]['duration'])

    convert(fnin, '480', '2', fnout)

    meta_480 = ffprobe_sync(fnout)
    duration_480 = float(meta_480['streams'][0]['duration'])
    
    time.sleep(20)
    assert orig_duration == approx(duration_480, rel=0.01)

def test_video2():
    fnin = 'BU.avi'
    fnout = 'BU720.mp4'

    orig_meta = ffprobe_sync(fnin)
    orig_duration = float(orig_meta['streams'][0]['duration'])

    convert(fnin, '720', '1', fnout)

    meta_720 = ffprobe_sync(fnout)
    duration_720 = float(meta_720['streams'][0]['duration'])
    time.sleep(20)
    assert orig_duration == approx(duration_720, rel=0.01)

def ffprobe_sync(filein: Path) -> dict:
    """ get media metadata """
    meta = subprocess.check_output(['ffprobe', '-v', 'warning',
                                	'-print_format', 'json',
                                	'-show_streams',
                                	'-show_format', 
                                    str(filein)], 
                                    text=True)
    return json.loads(meta)