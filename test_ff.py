import os
import re
import time


def test_ff():
    path = os.environ['path']
    if re.findall("ffmpeg", path):
        print("ffmpeg exit")

    else:
        print("ffmpeg not exit, Installing that will restart the program")
        os.system("Install.bat")
        time.sleep(3)
        exit()

