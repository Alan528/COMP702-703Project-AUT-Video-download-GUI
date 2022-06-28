import requests
import re
import json
import pprint
import os
import main


def bilibili(url, userinput):
    headers = {
        'referer': 'https://www.bilibili.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'

    }
    try:
        response = requests.get(url=url, headers=headers)
        # print(response.text) #获取网页数据

        title = re.findall('<h1 title="(.*?)"', response.text)[0]
        s = ['\n', '，', '。', ' ', '—', '”', '？', '“', '（', '）', '、', '|']
        for i in s:
            title = title.replace(i, '')
        print(f'Video Title："{title}"')
        print("Downloading")

        playinfo = re.findall('<script>window.__playinfo__=(.*?)</script>', response.text)[0]

        # print(playinfo)
        # print(type(playinfo))

        json_playinfo = json.loads(playinfo)  # 转换playinfo数据类型为字典
        # print(type(json_playinfo))
        # pprint.pprint(json_playinfo) #格式化输出

        audio_url = json_playinfo['data']['dash']['audio'][0]['baseUrl']
        video_url = json_playinfo['data']['dash']['video'][0]['baseUrl']

        # print(audio_url)
        # print(video_url)

        audio_content = requests.get(url=audio_url, headers=headers).content
        video_content = requests.get(url=video_url, headers=headers).content

        if userinput == "1":
            with open(title + '.mp3', mode='wb') as f:
                f.write(audio_content)
            with open(title + '.mp4', mode='wb') as f:
                f.write(video_content)

            cmd = f' ffmpeg  -i {title}.mp4 -i {title}.mp3 -acodec copy -vcodec copy bili_{title}.mp4'
            # 调用cmd执行ffmpeg程序来合并音频和视频
            os.system(cmd)
            # 删除原来的音频和视频
            os.remove(title + '.mp4')
            os.remove(title + '.mp3')
            print('Download completed')

        elif userinput == "2":
            with open(title + 'bili_.mp4', mode='wb') as f:
                f.write(video_content)
            print('Download completed')

        elif userinput == "3":
            with open(title + 'bili_.mp3', mode='wb') as f:
                f.write(audio_content)
            print('Download completed')

    except:
        print("Please input a exit Bilibili video link")
