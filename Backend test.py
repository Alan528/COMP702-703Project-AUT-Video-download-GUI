import BilibiliSP
import YoutubeSp
import re
import CheckVideo

if __name__ == '__main__':

    bilibili_checkurl = "www.bilibili.com"
    youtube_checkurl = "www.youtube.com"

    while True:
        value = input("Please input you link: ")
        print("Which type of the item you want to download？")
        userinput = input("1. MP4(Has Sound) 2. MP4(No Sound) 3. MP3: ")



        if re.findall(bilibili_checkurl, value):
            BilibiliSP.bilibili(value, userinput)
        elif re.findall(youtube_checkurl, value):
            YoutubeSp.youtube(value, userinput)
        else:
            print("Please input a Bilibili or Youtube link")

