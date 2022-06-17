import re

value = input("Please input the link ")
Bilibili_checkurl = "www.bilibili.com"
Youtube_checkurl = "www.youtube.com"
url=value
if __name__ == '__main__':

    if re.findall(Bilibili_checkurl, value):
        import BilibiliSP
    # elif re.findall(Youtube_checkurl, url):
    #     import YoutubeSp
