import shutil
import time
import requests
import re
import json
import os
from tqdm import tqdm
from moviepy.editor import VideoFileClip


def bilibili(url, utype):
    headers = {
        'referer': 'https://www.bilibili.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'

    }
    response = requests.get(url=url, headers=headers)
    # print(response.text) #get the web data

    title = re.findall('<h1 title="(.*?)"', response.text)[0]
    s = ['\n', '，', '。', ' ', '—', '”', '？', '“', '（', '）', '、', '|', '/', '\\', '"', '【', '】', '&', ';', '.']
    for i in s:
        title = title.replace(i, '')
    print(f'Video Title："{title}"')
    # print("Downloading")

    playinfo = re.findall('<script>window.__playinfo__=(.*?)</script>', response.text)[0]

    # print(playinfo)
    # print(type(playinfo))

    json_playinfo = json.loads(playinfo)  # trun playinfo type to dict
    # print(type(json_playinfo))
    # pprint.pprint(json_playinfo) #formating output

    audio_url = json_playinfo['data']['dash']['audio'][0]['baseUrl']
    video_url = json_playinfo['data']['dash']['video'][0]['baseUrl']

    # print(audio_url)
    # print(video_url)

    # audio_content = requests.get(url=audio_url, headers=headers, stream=True).content
    # video_content = requests.get(url=video_url, headers=headers, stream=True).content

    if utype == "1":

        video = requests.get(url=video_url, headers=headers, stream=True)
        video_size = int(video.headers.get('Content-Length'))
        video_pbar = tqdm(total=video_size)

        with open(title + '.mp4', mode='wb') as f:
            for video_chunk in video.iter_content(1024 * 1024 * 2):
                f.write(video_chunk)
                video_pbar.set_description('Downloading video...')
                video_pbar.update(1024 * 1024 * 2)
            video_pbar.set_description('Completed download video')
            video_pbar.close()

        audio = requests.get(url=audio_url, headers=headers, stream=True)
        audio_size = int(audio.headers.get('Content-Length'))
        audio_pbar = tqdm(total=audio_size)

        with open(title + '.mp3', mode='wb') as f:
            for audio_chunk in audio.iter_content(1024 * 1024 * 2):
                f.write(audio_chunk)
                audio_pbar.set_description('Downloading audio...')
                audio_pbar.update(1024 * 1024 * 2)
            audio_pbar.set_description('Completed download audio')
            audio_pbar.close()

        try:
            cmd1 = f"ffmpeg -i {title}.mp3 -f mp3 comp{title}.mp3"
            os.system(cmd1)

            cmd2 = f' ffmpeg  -i {title}.mp4 -i comp{title}.mp3 -acodec copy -vcodec copy bilibili_{title}.mp4'
            os.system(cmd2)
            time.sleep(1)
            # clip = VideoFileClip(f"bilibili{title}.mp4")
            # newclip = clip.volumex(1)
            # newclip.write_videofile(f"bilibili_{title}.mp4")
            shutil.move(f'.\\bilibili_{title}.mp4', '.\\Download\\Video')
            time.sleep(1)

            # delete the video amd audio that not join
            os.remove(title + '.mp4')
            os.remove(title + '.mp3')
            os.remove("comp" + title + ".mp3")

            print('Download completed')
        except:
            os.remove(title + '.mp4')
            os.remove(title + '.mp3')

    elif utype == "2":

        video = requests.get(url=video_url, headers=headers, stream=True)
        video_size = int(video.headers.get('Content-Length'))
        video_pbar = tqdm(total=video_size)

        with open("bilibili_NoS" + title + '.mp4', mode='wb') as f:
            for video_chunk in video.iter_content(1024 * 1024 * 2):
                f.write(video_chunk)
                video_pbar.set_description('Downloading video...')
                video_pbar.update(1024 * 1024 * 2)
            video_pbar.set_description('Completed download video')
            video_pbar.close()

        # move the video into Download folder
        shutil.move(f'.\\bilibili_NoS{title}.mp4', '.\\Download\\VideoNoSound')

    elif utype == "3":

        audio = requests.get(url=audio_url, headers=headers, stream=True)
        audio_size = int(audio.headers.get('Content-Length'))
        audio_pbar = tqdm(total=audio_size)

        with open(title + '.mp3', mode='wb') as f:
            for audio_chunk in audio.iter_content(1024 * 1024 * 2):
                f.write(audio_chunk)
                audio_pbar.set_description('Downloading audio...')
                audio_pbar.update(1024 * 1024 * 2)
            audio_pbar.set_description('Completed download audio')
            audio_pbar.close()

        try:
            cmd1 = f"ffmpeg -i {title}.mp3 -f mp3 bilibili_{title}.mp3"
            os.system(cmd1)
            # move the video into Download folder
            shutil.move(f'.\\bilibili_{title}.mp3', '.\\Download\\Audio')
            os.remove(title + ".mp3")
            print("Completed Download")
        except:
            os.remove(title + '.mp3')
