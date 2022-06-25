import json
import requests
import re
import os


def youtube(url):
            headers = {
                'cookie': 'VISITOR_INFO1_LIVE=En-lfqNNXQw; PREF=tz=Asia.Hong_Kong&f4=4000000&f5=30000; GPS=1; YSC=o1EVGXJ0H7I',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36',
                'referer': 'https://www.youtube.com'
            }

            respons = requests.get(url=url, headers=headers)

            json_str = re.findall('var ytInitialPlayerResponse = (.*?);var', respons.text)[0]
            # print(json_str)
            json_data = json.loads(json_str)

            videourl = json_data['streamingData']['adaptiveFormats'][0]['url']
            audiourl = json_data['streamingData']['adaptiveFormats'][-2]['url']

            title = json_data['videoDetails']['title']

            print(videourl)
            print(audiourl)

            s = ['\n', '，', '。', ' ', '—', '”', '？', '“', '（', '）', '、', '|']
            for i in s:
                title = title.replace(i, '')
            print(f'Video Title："{title}"')

            # print("Downloading...")
            # video = requests.get(videourl)
            # with open(f'{title}.mp4', mode='wb') as f:
            #     f.write(video.content)
            #
            # audio = requests.get(audiourl)
            # with open(f'{title}.mp3', mode='wb') as f:
            #     f.write(audio.content)
            #
            # # 调用cmd执行ffmpeg程序来合并音频和视频
            # cmd = f'ffmpeg -i "{title}.mp4" -i "{title}.mp3" -c:v copy -c:a aac -strict -2 "Youtube{title}.mp4"'
            # os.system(cmd)
            #
            # # 删除原来的音频和视频
            # os.remove(title + '.mp4')
            # os.remove(title + '.mp3')
            # print('Download completed')

