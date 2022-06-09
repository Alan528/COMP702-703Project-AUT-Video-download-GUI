import requests
from lxml import html
import re
import json
import os


def get_title_json(url):
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67'
    }
    r = requests.get(url, headers=head)

    # 通过xpath获取视频的标题
    tree = html.fromstring(r.text)
    title = str(tree.xpath('//*[@id="viewbox_report"]/h1/@title')[0])
    # 除去标题中的奇怪字符，这些字符会影响文件名的保存，产生未知错误
    s = ['\n', '，', '。', ' ', '—', '”', '？', '“', '（', '）', '、', '|']
    for i in s:
        title = title.replace(i, '')
    print(f'视频标题："{title}"')

    # 通过re获取包含视频和音频地址的json字段
    json_data = re.findall('<script>window.__playinfo__=(.*?)</script>', r.text)[0]
    json_data = json.loads(json_data)

    audio_url = json_data['data']['dash']['audio'][0]['backupUrl'][0]
    print('got audio link')
    video_url = json_data['data']['dash']['video'][0]['backupUrl'][0]
    print('got video link')
    return title, audio_url, video_url


def download(title, audio_url, video_url):
    # 这里的head加上Referer，避免让网站发现自己是爬虫
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67',
        'Referer': url
    }
    print('Start to download audio')
    r_audio = requests.get(url=audio_url, headers=head)
    audio_data = r_audio.content
    with open(title + '.mp3', mode='wb') as f:
        f.write(audio_data)
    print('Audio download complete')

    print('Start to download vedio')
    print('Downloading')
    r_video = requests.get(url=video_url, headers=head)
    video_data = r_video.content
    with open(title + '.mp4', mode='wb') as f:
        f.write(video_data)
    print('video download complete')


def audio_video_add(title):
    print('Compositing')
    cmd = f' ffmpeg  -i {title}.mp4 -i {title}.mp3 -acodec copy -vcodec copy bili_{title}.mp4'
    # 调用cmd执行ffmpeg程序来合并音频和视频
    os.system(cmd)
    # 删除原来的音频和视频
    os.remove(title + '.mp4')
    os.remove(title + '.mp3')
    print('Composited')


if __name__ == "__main__":
    while True:
        value = input('Please input video link quite to exic）')
        if value == 'quit':
            break
        else:
            url = value
            title, audio_url, video_url = get_title_json(url)
            download(title, audio_url, video_url)
            audio_video_add(title)