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
    ffe_path = "C:/ffmpeg-master-latest-win64-gpl-shared/bin"

    if not re.findall(ffe_path, path) and not os.path.exists("C:\\ffmpeg-master-latest-win64-gpl-shared\\bin"):
        print("ffmpeg not exit, Installing")
        cmd = "xcopy /S /H /Y ffmpeg-master-latest-win64-gpl-shared c:\\ffmpeg-master-latest-win64-gpl-shared\\"
        os.system(cmd)
        os.system("env.bat")
        print("please restart the program")
        time.sleep(5)
        exit()
    elif not os.path.exists("C:\\ffmpeg-master-latest-win64-gpl-shared\\bin") and re.findall(ffe_path, path):
        print("ffmpeg file not exit, Installing")
        cmd = "xcopy /S /H /Y ffmpeg-master-latest-win64-gpl-shared c:\\ffmpeg-master-latest-win64-gpl-shared\\"
        os.system(cmd)
        print("please restart the program")
        time.sleep(5)
        exit()
    elif not re.findall(ffe_path, path) and os.path.exists("C:\\ffmpeg-master-latest-win64-gpl-shared\\bin"):
        print("ffmpeg environment not exit, Installing")
        os.system("env.bat")
        print("please restart the program")
        time.sleep(5)
        exit()
    else:
        print("ffmpeg exit")


if __name__ == '__main__':
    test_ff()
