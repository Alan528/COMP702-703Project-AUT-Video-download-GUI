from libraries import *

def checkbilibili(url):
    headers = {
        'referer': 'https://www.bilibili.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'

    }
    response = requests.get(url=url, headers=headers)
    playinfo = re.findall('<script>window.__playinfo__=(.*?)</script>', response.text)[0]
    json_playinfo = json.loads(playinfo)  # 转换playinfo数据类型为字典
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
    json_data = json.loads(json_str)
    videourl = json_data['streamingData']['adaptiveFormats'][0]['url']
    audiourl = json_data['streamingData']['adaptiveFormats'][-2]['url']

def checkdouyin(url):
    headers = {

        'cookie': 'ttwid=1%7CierYIogGd1GwG83kmIkHxy9RrtQaf2QxGK7oMYvME-U%7C1657091868%7Ccd3bdbc32c8e356620009da92d6cdb53c1d9108099049eec06ab702302c72d73; douyin.com; strategyABtestKey=1657091870.704; s_v_web_id=verify_l599pqqx_64Mimpua_nCsC_45zg_A4rU_QVYN1FuQuCs5; passport_csrf_token=263e588f55bb28153ca04cc6d4d5bc85; passport_csrf_token_default=263e588f55bb28153ca04cc6d4d5bc85; AVATAR_FULL_LOGIN_GUIDE_TIMESTAMP=%221657091870547%22; AVATAR_FULL_LOGIN_GUIDE_COUNT=%221%22; ttcid=5309b3fadf864e64818d6983043536b229; THEME_STAY_TIME=%22299503%22; IS_HIDE_THEME_CHANGE=%221%22; odin_tt=c36d086199f1a2101a1e3522cc7305ffdf3e7149791e0f712f2e7952936cf96e3b953e063856a90e0e62b1fc2a96e306f9e0c0961d5883295acc2a0bc149963f; pwa_guide_count=%223%22; __ac_nonce=062c53f2e004c2041b128; __ac_signature=_02B4Z6wo00f01NKTQxwAAIDBsZmDdSSq6dDSs0eAAFZnQH1gq-dJxLNLyH7l3Pw4qvVrx8Xye-olHZPOonKcXRVsGRLsFddQhG6jLMgEgtaDHNUK0DNvO8zYVygde9sJZuE.T-sqGHcE4XY4f4; home_can_add_dy_2_desktop=%221%22; msToken=bzaNQ7UA4cOtSNjxa5dAv4Ia0p24m6xbD7SOyGX680T6UTbc_GUwC-xIPjs67loKa97h4Y_0Gjtwt0Y58NncCEdm-e78w23EBhsS3beWQuZGAQ92Lrnpk6FAHdLeU5o=; tt_scid=iDCSeh.J0Ips3kRPB0YSQGAS5nE4Y.cRKWxQFikmRQC6gktnDKROBQuWMkm0PYMa2f37; msToken=mK-fNgB8xg2xEEq3W04mFCNsZJmWy7f9mlN_ymgWqRqOqTcP7i_-kAta7yh0nKRtRp7qi-xQymjGEDY0HoYEqdwKwHQhDByjUXG_P-ZoZZBrp8YcPy5J7KFtJ4FerLA=',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

    }
    response = requests.get(url=url, headers=headers)
    # print(response.text)

    # print(response.text)
    video_url = re.findall('src(.*?)src%22%3A%', response.text)[0]
    video_url = requests.utils.unquote(video_url).replace('":"', 'http:')
