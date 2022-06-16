import requests
from requests import RequestException
from lxml import etree
import re
import os
import json
import subprocess
import urllib3

urllib3.disable_warnings()


def getHtml(baseurl):
    basecookie = "buvid3=B39BF36D-A72F-FFD6-3B07-3793794AF5F839097infoc; i-wanna-go-back=-1; _uuid=8BA10109BF-CB28-8F7C-AAB5-B94A6FF1568341837infoc; buvid4=4BF069B5-2829-4930-3E5A-1FDEF88BD61B40081-022060822-c8mC4VtaIp+iQZbzRZBhhg%3D%3D; LIVE_BUVID=AUTO6616546974404852; rpdid=|(k|k)Y~~))k0J'uYlRYm~RRJ; fingerprint=2a12597d6214c18c48b2ff2655b026da; sid=k4d3y5cq; buvid_fp_plain=undefined; CURRENT_BLACKGAP=0; blackside_state=0; DedeUserID=493126139; DedeUserID__ckMd5=258df21515101e64; SESSDATA=350c8b72%2C1670825797%2Cc77b0*61; bili_jct=ec816c8bda09662d02b917ea6d85afaf; buvid_fp=2a12597d6214c18c48b2ff2655b026da; CURRENT_QUALITY=112; b_ut=5; bp_video_offset_493126139=671877445199069200; innersign=0; b_lsid=B849D5B1_1816C88A314; CURRENT_FNVAL=4048; b_timer=%7B%22ffp%22%3A%7B%22333.1007.fp.risk_B39BF36D%22%3A%221816C88A4BE%22%2C%22666.4.fp.risk_B39BF36D%22%3A%221816C88C3BD%22%2C%22666.25.fp.risk_B39BF36D%22%3A%221816C88CDAE%22%7D%7D; PVID=1"
    head = {  # 模拟浏览器身份头向对方发送消息
        "cookie": basecookie + "_jct=2b7857b0d0b011eaa7f77ea539b9b3b7; DedeUserID=391625460; DedeUserID__ckMd5=accdac0e7e5f4f56; SESSDATA=a7c5c1cc%2C1611478568%2C56408*71; bili_jct=fe0e50c7ef84f6938d345f2b0c5e31d4",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.56 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.56"
    }
    try:
        response = requests.get(url=baseurl, headers=head)
        if response.status_code == 200:
            return response.text
    except:
        print("请求失败")


def main():
    print("欢迎来到bilibili爬资源小程序，接下来让我们开始吧\n(只针对番剧,您现在正在使用账户名为xxx的用户的会员cookie)")
    judge = input("你想获得一系列(y)视频还是一个单一(N)视频?   [y/N]\n")
    if judge == "y":
        max = int(input("输入该系列视频的总数: "))
        ep = int(input("输入第一集的ep号: "))
        for ep in range(ep, ep + max):
            baseurl = "https://www.bilibili.com/bangumi/play/ep" + str(ep)
            getVideo(baseurl, ep)
    else:
        ep = input("如果是系列视频，请任选一集输入视频ep号\n")
        baseurl = "https://www.bilibili.com/bangumi/play/ep" + str(ep)
        getVideo(baseurl, ep)

    os.system("pause")


def getVideo(baseurl, ep):
    html = getHtml(baseurl)
    # 找到视频的标题
    pattern = r'\<script\>window\.__playinfo__=(.*?)\</script\>'
    result = re.findall(pattern, html)[0]
    pattern = r'\<h1 title="(.*?)"\>.*\</h1\>'
    title = re.findall(pattern, html)[0]
    print(title)
    temp = json.loads(result)
    print(("开始下载--->") + title)
    title = str(ep)
    try:
        video_url = temp['data']['dash']['video'][0]['baseUrl']
        audio_url = temp['data']['dash']['audio'][0]['baseUrl']
        fileDownload(homeurl=baseurl, url=video_url, title=title, typ=0)
        fileDownload(homeurl=baseurl, url=audio_url, title=title, typ=1)
        try:
            combine(title)
        except:
            print("对不起，您的电脑中未安装ffmpeg，不予享受合成服务，您可以尝试使用格式工厂等其他方式\n")
    except Exception:
        vedio_url = temp['data']['durl'][0]['url']
        fileDownload(homeurl=baseurl, url=video_url, title=title, typ=0)


def fileDownload(homeurl, url, title, typ):
    # 添加请求头键值对,写上 refered:请求来源
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }
    headers.update({'Referer': homeurl})
    if typ == 0:
        print("正在下载视频")
        filename = "./" + title + ".flv"
    else:
        print("正在下载音频")
        filename = "./" + title + ".mp3"
    res = requests.Session()
    # 指定每次下载1M的数据
    begin = 0
    end = 2048 * 4096 - 1
    flag = 0
    while True:
        # 添加请求头键值对,写上 range:请求字节范围
        headers.update({'Range': 'bytes=' + str(begin) + '-' + str(end)})
        # 获取视频分片
        res = requests.get(url=url, headers=headers, verify=False)
        if res.status_code != 416:
            # 响应码不为为416时有数据
            begin = end + 1
            end = end + 2048 * 4096
        else:
            headers.update({'Range': str(end + 1) + '-'})
            res = requests.get(url=url, headers=headers, verify=False)
            flag = 1
        with open(filename, 'ab') as fp:
            fp.write(res.content)
            fp.flush()
        if flag == 1:
            fp.close()
            break
    print("下载完成！")


def combine(title):
    videopath = "./" + title + ".flv"
    videopath = os.getcwd() + "\\" + title + ".flv"
    audiopath = "./" + title + ".mp3"
    audiopath = os.getcwd() + "\\" + title + ".mp3"
    outpath = "./" + title + ".flv"
    outpath = os.getcwd() + "\\" + title + ".mp4"
    subprocess.call(
        ("C:/ffmpeg-win64-static/bin/ffmpeg -i " + videopath + " -i " + audiopath + " -c copy " + outpath).encode(
            "utf-8").decode("utf-8"), shell=True)
    os.remove(videopath)
    # os.remove(audiopath)


if __name__ == "__main__":
    main()