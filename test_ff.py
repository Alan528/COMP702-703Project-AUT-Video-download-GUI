import os
import re
import shutil
import time
import sys


def test_ff():
    s = ['\\']
    path = str(os.environ['path'])
    for i in s:
        path = path.replace(i, '/')
        print(path)

    ffe_part = "C:/ffmpeg-master-latest-win64-gpl-shared/bin"

    if re.findall(ffe_part, path):
        print("ffmpeg exit")
    else:
        print("ffmpeg not exit, Installing")
        shutil.move(".\\ffmpeg-master-latest-win64-gpl-shared", "C:\\")
        os.system("env.bat")
        print("please restart the program")
        time.sleep(3)
        exit()

