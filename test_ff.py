import os
import re
import time
import sys


def test_ff():
    s = ['\\']
    path = str(os.environ['path'])
    for i in s:
        path = path.replace(i, '/')
        # print(path)

    current_Path = os.getcwd()
    for i in s:
        current_Path = current_Path.replace(i, '/')
        # print(current_Path)

    ffe_part = "/ffmpeg-master-latest-win64-gpl-shared/bin"

    join_part = current_Path + ffe_part
    # print(join_part)

    if re.findall(join_part, path):
        print("ffmpeg exit")
    else:
        print("ffmpeg not exit, Installing that will restart the program")
        cmd = 'setx path " " '
        os.system(cmd)
        os.system("env.bat")

if __name__ == '__main__':
    test_ff()