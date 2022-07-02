import requests
import re
import json


def checkbilibili(url):
    headers = {
        'referer': 'https://www.bilibili.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'

    }
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


def checkyoutube(url):
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
