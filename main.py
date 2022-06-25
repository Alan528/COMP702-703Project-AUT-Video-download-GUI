import BilibiliSP
import YoutubeSp
import re


if __name__ == '__main__':

        bilibili_checkurl = "www.bilibili.com"
        youtube_checkurl = "www.youtube.com"
        while True:
            value = input("Please input you link: ")

            if re.findall(bilibili_checkurl, value):
                BilibiliSP.bilibili(value)
            elif re.findall(youtube_checkurl, value):
                YoutubeSp.youtube(value)
            else:
                print("Please input a Bilibili or Youtube link")
