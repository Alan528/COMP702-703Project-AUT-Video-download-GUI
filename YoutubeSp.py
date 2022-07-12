import json
import shutil
from tqdm import tqdm
import requests
import re
import os


def youtube(url, utype):
    headers = {
        'cookie': 'VISITOR_INFO1_LIVE=En-lfqNNXQw; PREF=tz=Asia.Hong_Kong&f4=4000000&f5=30000; GPS=1; YSC=o1EVGXJ0H7I',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36',
        'referer': 'https://www.youtube.com'
    }
    respons = requests.get(url=url, headers=headers)
    json_str = re.findall('var ytInitialPlayerResponse = (.*?);var', respons.text)[0]
    # print(json_str)
    json_data = json.loads(json_str)

    video_url = json_data['streamingData']['adaptiveFormats'][0]['url']
    audio_url = json_data['streamingData']['adaptiveFormats'][-2]['url']

    title = json_data['videoDetails']['title']

    # print(video_url)
    # print(audio_url)

    s = ['\n', '，', '。', ' ', '—', '”', '？', '“', '（', '）', '、', '|']
    for i in s:
        title = title.replace(i, '')
    print(f'Video Title："{title}"')

    # print("Downloading...")
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

        cmd = f' ffmpeg  -i {title}.mp4 -i {title}.mp3 -acodec copy -vcodec copy youtube_{title}.mp4'
        # use cmd run ffmpeg join video and video
        os.system(cmd)

        # move the video into Download folder
        shutil.move(f'.\\youtube_{title}.mp4', '.\\Download')

        # delete the video amd audio that not join
        os.remove(title + '.mp4')
        os.remove(title + '.mp3')

        print('Download completed')

    elif utype == "2":

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

        # move the video into Download folder
        shutil.move(f'.\\{title}.mp4', '.\\Download')

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

        # move the video into Download folder
        shutil.move(f'.\\{title}.mp3', '.\\Download')