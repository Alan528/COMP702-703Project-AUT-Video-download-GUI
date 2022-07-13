import requests
import re
import shutil
import os
import time
import moviepy
from tqdm import tqdm
from moviepy.editor import VideoFileClip


def douyin(url, utype):
    headers = {

        'cookie': 'ttwid=1%7CierYIogGd1GwG83kmIkHxy9RrtQaf2QxGK7oMYvME-U%7C1657091868%7Ccd3bdbc32c8e356620009da92d6cdb53c1d9108099049eec06ab702302c72d73; douyin.com; strategyABtestKey=1657091870.704; s_v_web_id=verify_l599pqqx_64Mimpua_nCsC_45zg_A4rU_QVYN1FuQuCs5; passport_csrf_token=263e588f55bb28153ca04cc6d4d5bc85; passport_csrf_token_default=263e588f55bb28153ca04cc6d4d5bc85; AVATAR_FULL_LOGIN_GUIDE_TIMESTAMP=%221657091870547%22; AVATAR_FULL_LOGIN_GUIDE_COUNT=%221%22; ttcid=5309b3fadf864e64818d6983043536b229; THEME_STAY_TIME=%22299503%22; IS_HIDE_THEME_CHANGE=%221%22; odin_tt=c36d086199f1a2101a1e3522cc7305ffdf3e7149791e0f712f2e7952936cf96e3b953e063856a90e0e62b1fc2a96e306f9e0c0961d5883295acc2a0bc149963f; pwa_guide_count=%223%22; __ac_nonce=062c53f2e004c2041b128; __ac_signature=_02B4Z6wo00f01NKTQxwAAIDBsZmDdSSq6dDSs0eAAFZnQH1gq-dJxLNLyH7l3Pw4qvVrx8Xye-olHZPOonKcXRVsGRLsFddQhG6jLMgEgtaDHNUK0DNvO8zYVygde9sJZuE.T-sqGHcE4XY4f4; home_can_add_dy_2_desktop=%221%22; msToken=bzaNQ7UA4cOtSNjxa5dAv4Ia0p24m6xbD7SOyGX680T6UTbc_GUwC-xIPjs67loKa97h4Y_0Gjtwt0Y58NncCEdm-e78w23EBhsS3beWQuZGAQ92Lrnpk6FAHdLeU5o=; tt_scid=iDCSeh.J0Ips3kRPB0YSQGAS5nE4Y.cRKWxQFikmRQC6gktnDKROBQuWMkm0PYMa2f37; msToken=mK-fNgB8xg2xEEq3W04mFCNsZJmWy7f9mlN_ymgWqRqOqTcP7i_-kAta7yh0nKRtRp7qi-xQymjGEDY0HoYEqdwKwHQhDByjUXG_P-ZoZZBrp8YcPy5J7KFtJ4FerLA=',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

    }
    response = requests.get(url=url, headers=headers)
    # print(response.text)

    title = re.findall('<meta data-react-helmet="true" name="lark:url:video_title" content=(.*?)/>', response.text)[0]
    s = ['\n', '，', '。', ' ', '—', '”', '？', '“', '（', '）', '、', '|', '/', '\\', '"']
    for i in s:
        title = title.replace(i, '')
    print(f'Video Title："{title}"')

    # print(response.text)
    video_url = re.findall('src(.*?)src%22%3A%', response.text)[0]
    video_url = requests.utils.unquote(video_url).replace('":"', 'http:')

    # print(video_url)
    # video_content = requests.get(url=video_url, headers=headers).content

    if utype == "1":
        video = requests.get(url=video_url, headers=headers, stream=True)
        video_size = int(video.headers.get('Content-Length'))
        video_pbar = tqdm(total=video_size)

        with open("douyin_"+title + '.mp4', mode='wb') as f:
            for video_chunk in video.iter_content(1024 * 1024 * 2):
                f.write(video_chunk)
                video_pbar.set_description('Downloading video...')
                video_pbar.update(1024 * 1024 * 2)
            video_pbar.set_description('Completed download video')
            video_pbar.close()

        # move the video into Download folder
        shutil.move(f'.\\douyin_{title}.mp4', '.\\Download\\Video')

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

        video = VideoFileClip(f"{title}.mp4")
        video = video.without_audio()
        video.write_videofile(f"douyin_NoS{title}.mp4")
        shutil.move(f'.\\douyin_NoS{title}.mp4', '.\\Download\\VideoNoSound')
        cmd = "taskkill /f /t /im ffmpeg-win64-v4.2.2.exe"
        os.system(cmd)
        time.sleep(1)
        os.remove(title + '.mp4')

    elif utype == "3":

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

        cmd1 = f"ffmpeg -i {title}.mp4 -f mp3 douyin_{title}.mp3"
        os.system(cmd1)
        shutil.move(f'.\\douyin_{title}.mp3', '.\\Download\\Audio')
        os.remove(title + '.mp4')

    print("Complete Download")
