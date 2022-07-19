from libraries import *


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
        os.system("admin.cmd")
        print("please restart the program")
        os.system("restartmes.cmd")

    elif not os.path.exists("C:\\ffmpeg-master-latest-win64-gpl-shared\\bin") and re.findall(ffe_path, path):
        print("ffmpeg file not exit, Installing")
        cmd = "xcopy /S /H /Y ffmpeg-master-latest-win64-gpl-shared c:\\ffmpeg-master-latest-win64-gpl-shared\\"
        os.system(cmd)
        print("please restart the program")
        os.system("restartmes.cmd")

    elif not re.findall(ffe_path, path) and os.path.exists("C:\\ffmpeg-master-latest-win64-gpl-shared\\bin"):
        print("ffmpeg environment not exit, Installing")
        os.system("admin.cmd")
        print("please restart the program")
        os.system("restartmes.cmd")

    else:
        print("ffmpeg exit")


