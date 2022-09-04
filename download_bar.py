# Import the libraries file
from libraries import *
from notification_screen import *

# purpose of this global variable is let the system know which button has been clicked
# and called exactly that function for downloading
flag = 0
bilibili_checkurl = "www.bilibili.com"
youtube_checkurl = "www.youtube.com"
douyin_checkurl = "www.douyin.com"

class download(object):

    # Creat GUI for download bar
    def __init__(dl, master, inp):
        # Create a tkinter frame
        dl.master = master

        # store user link input in main screen
        dl.inp = inp
        print("the user input in main screen passed into class download:  " + dl.inp + "\n")

        dl.frame = Frame(dl.master)

        # Insert icon and title
        dl.master.title("Downloading....")
        dl.master.wm_iconbitmap("./image/download_icon.ico")

        # Set the geometry of frame and background
        dl.master.geometry("500x400")
        dl.master.configure(bg="#ffffff")
        dl.canvas = Canvas(
            dl.master,
            bg="#ffffff",
            height=400,
            width=500,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        dl.canvas.place(x=0, y=0)

        dl.background_img = PhotoImage(file=f"./image/download_bg.png")
        dl.background = dl.canvas.create_image(
            250.0, 199.0,
            image=dl.background_img)

        # Download bar process
        dl.bar = Progressbar(dl.master, orient='horizontal',
                             length=300, mode='determinate')
        dl.bar.pack(pady=35)

        # MP4 has sound button
        dl.img3 = PhotoImage(file=f"./image/mp4_has_sound_btt.png")
        dl.b3 = Button(
            dl.master,
            image=dl.img3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: dl.dl_mp4_has_sound(dl.inp),
            relief="flat")

        dl.b3.place(
            x=110, y=136,
            width=267,
            height=47)

        # MP4 video no sound button
        dl.img2 = PhotoImage(file=f"./image/mp4_no_sound_btt.png")
        dl.b2 = Button(
            dl.master,
            image=dl.img2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: dl.dl_mp4_no_sound(dl.inp),
            relief="flat")

        dl.b2.place(
            x=110, y=201,
            width=267,
            height=47)

        # MP3 button
        dl.img1 = PhotoImage(file=f"./image/mp3_btt.png")
        dl.b1 = Button(
            dl.master,
            image=dl.img1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: dl.dl_mp3(dl.inp),
            relief="flat")

        dl.b1.place(
            x=110, y=266,
            width=267,
            height=47)

        # Exit button
        dl.img0 = PhotoImage(file=f"./image/exit_btt.png")
        dl.b0 = Button(
            dl.master,
            image=dl.img0,
            borderwidth=0,
            highlightthickness=0,
            command=dl.master.destroy,
            relief="flat")

        dl.b0.place(
            x=393, y=341,
            width=79,
            height=36)

        dl.master.resizable(False, False)

    # ========== Finished for interface ===========

    # Define action for button when user click on it. it will call the download in system.

    # function for downloading mp4 has sound, when user click on mp4 has sound button

    def dl_mp4_has_sound(self, inp):

        flag = 1
        print("MP4 has sound button clicked")
        print("value button:", flag, "\n\n")
        utype = str(flag)
        url = inp

        print("============")
        # print(video_size)
        print("============")

        if re.findall(bilibili_checkurl, inp):

            if utype == "1":
                if not checkVideoExit.bilibilivideo(inp):

                    headers = {
                        'referer': 'https://www.bilibili.com/',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'

                    }
                    response = requests.get(url=url, headers=headers)
                    # print(response.text) #get the web data

                    title = re.findall('<h1 title="(.*?)"', response.text)[0]
                    s = ['\n', '，', '。', ' ', '—', '”', '？', '“', '（', '）', '、', '|', '/', '\\', '"', '【', '】', '&',
                         ';', '.']
                    for i in s:
                        title = title.replace(i, '')
                    print(f'Video Title："{title}"')
                    # print("Downloading")

                    playinfo = re.findall(
                        '<script>window.__playinfo__=(.*?)</script>', response.text)[0]

                    # print(playinfo)
                    # print(type(playinfo))

                    # trun playinfo type to dict
                    json_playinfo = json.loads(playinfo)
                    # print(type(json_playinfo))
                    # pprint.pprint(json_playinfo) #formating output

                    audio_url = json_playinfo['data']['dash']['audio'][0]['baseUrl']
                    video_url = json_playinfo['data']['dash']['video'][0]['baseUrl']

                    # print(audio_url)
                    # print(video_url)

                    # audio_content = requests.get(url=audio_url, headers=headers, stream=True).content
                    # video_content = requests.get(url=video_url, headers=headers, stream=True).content

                    # Download video
                    video = requests.get(
                        url=video_url, headers=headers, stream=True)
                    video_size = int(video.headers.get('Content-Length'))
                    self.bar['value'] = 0
                    chunk_size = 1024 * 1024 * 2
                    self.bar['maximum'] = video_size

                    with open(title + '.mp4', mode='wb') as f:
                        for video_chunk in video.iter_content(chunk_size=chunk_size):
                            f.write(video_chunk)
                            print(len(video_chunk))
                            print(video_size)
                            self.bar['value'] += len(video_chunk)
                            self.bar.update()

                    # Download audio
                    audio = requests.get(
                        url=audio_url, headers=headers, stream=True)
                    audio_size = int(audio.headers.get('Content-Length'))
                    self.bar['value'] = 0
                    chunk_size = 1024 * 1024 * 2
                    self.bar['maximum'] = audio_size

                    with open(title + '.mp3', mode='wb') as f:
                        for audio_chunk in audio.iter_content(chunk_size=chunk_size):
                            f.write(audio_chunk)
                            print(len(audio_chunk))
                            print(audio_size)
                            self.bar['value'] += len(audio_chunk)
                            self.bar.update()

                    # combine video and audio
                    try:
                        cmd1 = f"ffmpeg -i {title}.mp3 -f mp3 comp{title}.mp3"
                        os.system(cmd1)

                        cmd2 = f' ffmpeg  -i {title}.mp4 -i comp{title}.mp3 -acodec copy -vcodec copy bilibili_{title}.mp4'
                        os.system(cmd2)
                        tm.sleep(1)
                        # clip = VideoFileClip(f"bilibili{title}.mp4")
                        # newclip = clip.volumex(1)
                        # newclip.write_videofile(f"bilibili_{title}.mp4")
                        shutil.move(
                            f'.\\bilibili_{title}.mp4', '.\\Download\\Video')
                        tm.sleep(1)

                        # delete the video amd audio that not join
                        os.remove(title + '.mp4')
                        os.remove(title + '.mp3')
                        os.remove("comp" + title + ".mp3")

                        print('Download completed')

                        # this code for displaying a downloaded notification
                        self.bar['value'] = 0
                        self.top = Toplevel()
                        windown_download = download_complete(self.top)
                    except:
                        os.remove(title + '.mp4')
                        os.remove(title + '.mp3')
                else:
                    self.top = Toplevel()
                    windown_Exit = invalue_input_file_exist(self.top)

        # Download YouTube
        elif re.findall(youtube_checkurl, inp):
            if not checkVideoExit.youtube(inp):

                headers = {
                    'cookie': 'VISITOR_INFO1_LIVE=En-lfqNNXQw; PREF=tz=Asia.Hong_Kong&f4=4000000&f5=30000; GPS=1; YSC=o1EVGXJ0H7I',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36',
                    'referer': 'https://www.youtube.com'
                }
                respons = requests.get(url=url, headers=headers)
                print(respons)
                json_str = re.findall(
                    'var ytInitialPlayerResponse = (.*?);var', respons.text)[0]
                # print(json_str)
                json_data = json.loads(json_str)
                video_url = json_data['streamingData']['adaptiveFormats'][0]['url']
                audio_url = json_data['streamingData']['adaptiveFormats'][-1]['url']

                # print(video_url)
                # print(audio_url)

                title = json_data['videoDetails']['title']
                s = ['\n', '，', '。', ' ', '—', '”', '？', '“', '（', '）', '、', '|', '/', '\\', '"', '【', '】', '&',
                     ';', '.']
                for i in s:
                    title = title.replace(i, '')
                print(f'Video Title："{title}"')

                cmd = f"yt-dlp -o, --output {title} -P, --paths \Download\Video {inp}"
                os.system(cmd)

                print('Download completed')

                self.top = Toplevel()
                windown_download = download_complete(self.top)

            else:
                self.top = Toplevel()
                windown_Exit = invalue_input_file_exist(self.top)

        # Download Douyin video
        elif re.findall(douyin_checkurl, inp):
            if not checkVideoExit.douyin(inp):
                headers = {

                    'cookie': 'ttwid=1%7CierYIogGd1GwG83kmIkHxy9RrtQaf2QxGK7oMYvME-U%7C1657091868%7Ccd3bdbc32c8e356620009da92d6cdb53c1d9108099049eec06ab702302c72d73; douyin.com; strategyABtestKey=1657091870.704; s_v_web_id=verify_l599pqqx_64Mimpua_nCsC_45zg_A4rU_QVYN1FuQuCs5; passport_csrf_token=263e588f55bb28153ca04cc6d4d5bc85; passport_csrf_token_default=263e588f55bb28153ca04cc6d4d5bc85; AVATAR_FULL_LOGIN_GUIDE_TIMESTAMP=%221657091870547%22; AVATAR_FULL_LOGIN_GUIDE_COUNT=%221%22; ttcid=5309b3fadf864e64818d6983043536b229; THEME_STAY_TIME=%22299503%22; IS_HIDE_THEME_CHANGE=%221%22; odin_tt=c36d086199f1a2101a1e3522cc7305ffdf3e7149791e0f712f2e7952936cf96e3b953e063856a90e0e62b1fc2a96e306f9e0c0961d5883295acc2a0bc149963f; pwa_guide_count=%223%22; __ac_nonce=062c53f2e004c2041b128; __ac_signature=_02B4Z6wo00f01NKTQxwAAIDBsZmDdSSq6dDSs0eAAFZnQH1gq-dJxLNLyH7l3Pw4qvVrx8Xye-olHZPOonKcXRVsGRLsFddQhG6jLMgEgtaDHNUK0DNvO8zYVygde9sJZuE.T-sqGHcE4XY4f4; home_can_add_dy_2_desktop=%221%22; msToken=bzaNQ7UA4cOtSNjxa5dAv4Ia0p24m6xbD7SOyGX680T6UTbc_GUwC-xIPjs67loKa97h4Y_0Gjtwt0Y58NncCEdm-e78w23EBhsS3beWQuZGAQ92Lrnpk6FAHdLeU5o=; tt_scid=iDCSeh.J0Ips3kRPB0YSQGAS5nE4Y.cRKWxQFikmRQC6gktnDKROBQuWMkm0PYMa2f37; msToken=mK-fNgB8xg2xEEq3W04mFCNsZJmWy7f9mlN_ymgWqRqOqTcP7i_-kAta7yh0nKRtRp7qi-xQymjGEDY0HoYEqdwKwHQhDByjUXG_P-ZoZZBrp8YcPy5J7KFtJ4FerLA=',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

                }
                response = requests.get(url=url, headers=headers)
                # print(response.text)

                title = \
                    re.findall('<meta data-react-helmet="true" name="lark:url:video_title" content=(.*?)/>',
                               response.text)[
                        0]
                s = ['\n', '，', '。', ' ', '—', '”', '？', '“', '（', '）', '、', '|', '/', '\\', '"', '【', '】', '&', ';',
                     '.']
                for i in s:
                    title = title.replace(i, '')
                print(f'Video Title："{title}"')

                # print(response.text)
                video_url = re.findall('src(.*?)src%22%3A%', response.text)[0]
                video_url = requests.utils.unquote(
                    video_url).replace('":"', 'http:')

                # print(video_url)
                # video_content = requests.get(url=video_url, headers=headers).content

                video = requests.get(
                    url=video_url, headers=headers, stream=True)
                video_size = int(video.headers.get('Content-Length'))
                self.bar['value'] = 0
                chunk_size = 1024 * 1024 * 2
                self.bar['maximum'] = video_size

                with open("douyin_" + title + '.mp4', mode='wb') as f:
                    for video_chunk in video.iter_content(chunk_size=chunk_size):
                        f.write(video_chunk)
                        print(len(video_chunk))
                        print(video_size)
                        self.bar['value'] += len(video_chunk)
                        self.bar.update()
                # move the video into Download folder
                shutil.move(f'.\\douyin_{title}.mp4', '.\\Download\\Video')
                self.top = Toplevel()
                windown_download = download_complete(self.top)
            else:
                self.top = Toplevel()
                windown_Exit = invalue_input_file_exist(self.top)

    #
    # # function for downloading mp4 no sound, when user click on mp4 no sound button
    #
    def dl_mp4_no_sound(self, inp):
        url = inp
        flag = 2
        print("MP4 no sound button clicked")
        print("value button:", flag, "\n\n")

        if re.findall(bilibili_checkurl, inp):
            if not checkVideoExit.bilibilinosvideo(inp):

                headers = {
                    'referer': 'https://www.bilibili.com/',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'

                }
                response = requests.get(url=url, headers=headers)
                # print(response.text) #get the web data

                title = re.findall('<h1 title="(.*?)"', response.text)[0]
                s = ['\n', '，', '。', ' ', '—', '”', '？', '“', '（', '）', '、', '|', '/', '\\', '"', '【', '】', '&',
                     ';', '.']
                for i in s:
                    title = title.replace(i, '')
                print(f'Video Title："{title}"')
                # print("Downloading")

                playinfo = re.findall(
                    '<script>window.__playinfo__=(.*?)</script>', response.text)[0]

                # print(playinfo)
                # print(type(playinfo))

                # trun playinfo type to dict
                json_playinfo = json.loads(playinfo)
                # print(type(json_playinfo))
                # pprint.pprint(json_playinfo) #formating output

                audio_url = json_playinfo['data']['dash']['audio'][0]['baseUrl']
                video_url = json_playinfo['data']['dash']['video'][0]['baseUrl']

                # print(audio_url)
                # print(video_url)

                # audio_content = requests.get(url=audio_url, headers=headers, stream=True).content
                # video_content = requests.get(url=video_url, headers=headers, stream=True).content

                video = requests.get(
                    url=video_url, headers=headers, stream=True)
                video_size = int(video.headers.get('Content-Length'))
                self.bar['value'] = 0
                chunk_size = 1024 * 1024 * 2
                self.bar['maximum'] = video_size

                with open("bilibili_NoS" + title + '.mp4', mode='wb') as f:
                    for video_chunk in video.iter_content(chunk_size=chunk_size):
                        f.write(video_chunk)
                        print(len(video_chunk))
                        print(video_size)
                        self.bar['value'] += len(video_chunk)
                        self.bar.update()
                # move the video into Download folder
                shutil.move(
                    f'.\\bilibili_NoS{title}.mp4', '.\\Download\\VideoNoSound')
                self.bar['value'] = 0
                self.top = Toplevel()
                windown_download = download_complete(self.top)

            else:
                self.top = Toplevel()
                windown_Exit = invalue_input_file_exist(self.top)

        elif re.findall(youtube_checkurl, inp):
            if not checkVideoExit.youtubenosvideo(inp):
                headers = {
                    'cookie': 'VISITOR_INFO1_LIVE=En-lfqNNXQw; PREF=tz=Asia.Hong_Kong&f4=4000000&f5=30000; GPS=1; YSC=o1EVGXJ0H7I',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36',
                    'referer': 'https://www.youtube.com'
                }
                respons = requests.get(url=url, headers=headers)
                # print(respons)
                json_str = re.findall(
                    'var ytInitialPlayerResponse = (.*?);var', respons.text)[0]
                # print(json_str)
                json_data = json.loads(json_str)
                video_url = json_data['streamingData']['adaptiveFormats'][0]['url']
                audio_url = json_data['streamingData']['adaptiveFormats'][-2]['url']

                # print(video_url)
                # print(audio_url)

                title = json_data['videoDetails']['title']
                s = ['\n', '，', '。', ' ', '—', '”', '？', '“', '（', '）', '、', '|', '/', '\\', '"', '【', '】', '&', ';',
                     '.']
                for i in s:
                    title = title.replace(i, '')
                print(f'Video Title："{title}"')

                print("Downloading...")
                # audio_content = requests.get(url=audio_url, headers=headers, stream=True).content
                # video_content = requests.get(url=video_url, headers=headers, stream=True).content

                cmd = f"yt-dlp -o, --output {title} {inp}"
                os.system(cmd)

                cmd2 = f"ffmpeg -i {title}.webm -c:v copy -an youtubeNos{title}.webm"
                os.system(cmd2)
                os.remove(f"{title}.webm")
                shutil.move(f"youtubeNos{title}.webm", "Download/VideoNoSound")

                self.top = Toplevel()
                windown_download = download_complete(self.top)

            else:
                self.top = Toplevel()
                windown_Exit = invalue_input_file_exist(self.top)
        #
        elif re.findall(douyin_checkurl, inp):
            headers = {

                'cookie': 'ttwid=1%7CierYIogGd1GwG83kmIkHxy9RrtQaf2QxGK7oMYvME-U%7C1657091868%7Ccd3bdbc32c8e356620009da92d6cdb53c1d9108099049eec06ab702302c72d73; douyin.com; strategyABtestKey=1657091870.704; s_v_web_id=verify_l599pqqx_64Mimpua_nCsC_45zg_A4rU_QVYN1FuQuCs5; passport_csrf_token=263e588f55bb28153ca04cc6d4d5bc85; passport_csrf_token_default=263e588f55bb28153ca04cc6d4d5bc85; AVATAR_FULL_LOGIN_GUIDE_TIMESTAMP=%221657091870547%22; AVATAR_FULL_LOGIN_GUIDE_COUNT=%221%22; ttcid=5309b3fadf864e64818d6983043536b229; THEME_STAY_TIME=%22299503%22; IS_HIDE_THEME_CHANGE=%221%22; odin_tt=c36d086199f1a2101a1e3522cc7305ffdf3e7149791e0f712f2e7952936cf96e3b953e063856a90e0e62b1fc2a96e306f9e0c0961d5883295acc2a0bc149963f; pwa_guide_count=%223%22; __ac_nonce=062c53f2e004c2041b128; __ac_signature=_02B4Z6wo00f01NKTQxwAAIDBsZmDdSSq6dDSs0eAAFZnQH1gq-dJxLNLyH7l3Pw4qvVrx8Xye-olHZPOonKcXRVsGRLsFddQhG6jLMgEgtaDHNUK0DNvO8zYVygde9sJZuE.T-sqGHcE4XY4f4; home_can_add_dy_2_desktop=%221%22; msToken=bzaNQ7UA4cOtSNjxa5dAv4Ia0p24m6xbD7SOyGX680T6UTbc_GUwC-xIPjs67loKa97h4Y_0Gjtwt0Y58NncCEdm-e78w23EBhsS3beWQuZGAQ92Lrnpk6FAHdLeU5o=; tt_scid=iDCSeh.J0Ips3kRPB0YSQGAS5nE4Y.cRKWxQFikmRQC6gktnDKROBQuWMkm0PYMa2f37; msToken=mK-fNgB8xg2xEEq3W04mFCNsZJmWy7f9mlN_ymgWqRqOqTcP7i_-kAta7yh0nKRtRp7qi-xQymjGEDY0HoYEqdwKwHQhDByjUXG_P-ZoZZBrp8YcPy5J7KFtJ4FerLA=',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

            }
            response = requests.get(url=url, headers=headers)
            # print(response.text)

            title = \
                re.findall('<meta data-react-helmet="true" name="lark:url:video_title" content=(.*?)/>', response.text)[
                    0]
            s = ['\n', '，', '。', ' ', '—', '”', '？', '“', '（', '）',
                 '、', '|', '/', '\\', '"', '【', '】', '&', ';', '.']
            for i in s:
                title = title.replace(i, '')
            print(f'Video Title："{title}"')

            # print(response.text)
            video_url = re.findall('src(.*?)src%22%3A%', response.text)[0]
            video_url = requests.utils.unquote(
                video_url).replace('":"', 'http:')

            if not checkVideoExit.douyinnosvideo(inp):

                video = requests.get(
                    url=video_url, headers=headers, stream=True)
                video_size = int(video.headers.get('Content-Length'))
                self.bar['value'] = 0
                chunk_size = 1024 * 1024 * 2
                self.bar['maximum'] = video_size

                with open(title + '.mp4', mode='wb') as f:
                    for video_chunk in video.iter_content(chunk_size=chunk_size):
                        f.write(video_chunk)
                        print(len(video_chunk))
                        print(video_size)
                        self.bar['value'] += len(video_chunk)
                        self.bar.update()

                cmd1 = f"ffmpeg -i {title}.mp4 -c:v copy -an douyin_NoS{title}.mp4"
                os.system(cmd1)

                shutil.move(f'.\\douyin_NoS{title}.mp4',
                            '.\\Download\\VideoNoSound')
                cmd = "taskkill /f /t /im ffmpeg-win64-v4.2.2.exe"
                os.system(cmd)
                tm.sleep(1)
                os.remove(title + '.mp4')

                self.bar['value'] = 0
                self.top = Toplevel()
                windown_download = download_complete(self.top)
            else:
                self.top = Toplevel()
                windown_Exit = invalue_input_file_exist(self.top)

    # function for downloading mp3, when user click on mp3 button
    def dl_mp3(self, inp):

        url = inp

        print("the user input in main screen passed into button function:  " + inp + "\n\n")

        flag = 3
        print("MP3 button clicked")
        print("value button:", flag, "\n\n")

        if re.findall(bilibili_checkurl, inp):

            headers = {
                'referer': 'https://www.bilibili.com/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'

            }
            response = requests.get(url=url, headers=headers)
            # print(response.text) #get the web data

            title = re.findall('<h1 title="(.*?)"', response.text)[0]
            s = ['\n', '，', '。', ' ', '—', '”', '？', '“', '（', '）', '、', '|', '/', '\\', '"', '【', '】', '&',
                 ';', '.']
            for i in s:
                title = title.replace(i, '')
            print(f'Video Title："{title}"')
            # print("Downloading")

            playinfo = re.findall(
                '<script>window.__playinfo__=(.*?)</script>', response.text)[0]

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

            if not checkVideoExit.bilibiliaudio(inp):

                # Download audio
                audio = requests.get(
                    url=audio_url, headers=headers, stream=True)
                audio_size = int(audio.headers.get('Content-Length'))
                self.bar['value'] = 0
                chunk_size = 1024 * 1024 * 2
                self.bar['maximum'] = audio_size

                with open(title + '.mp3', mode='wb') as f:
                    for audio_chunk in audio.iter_content(chunk_size=chunk_size):
                        f.write(audio_chunk)
                        print(len(audio_chunk))
                        print(audio_size)
                        self.bar['value'] += len(audio_chunk)
                        self.bar.update()

                try:
                    cmd1 = f"ffmpeg -i {title}.mp3 -f mp3 bilibili_{title}.mp3"
                    os.system(cmd1)
                    # move the video into Download folder
                    shutil.move(
                        f'.\\bilibili_{title}.mp3', '.\\Download\\Audio')
                    os.remove(title + ".mp3")
                    print("Completed Download")
                    self.bar['value'] = 0
                    self.top = Toplevel()
                    windown_download = download_complete(self.top)
                except:
                    os.remove(title + '.mp3')

            else:
                self.top = Toplevel()
                windown_Exit = invalue_input_file_exist(self.top)

        # Download Youtube Audio
        elif re.findall(youtube_checkurl, inp):
            headers = {
                'cookie': 'VISITOR_INFO1_LIVE=En-lfqNNXQw; PREF=tz=Asia.Hong_Kong&f4=4000000&f5=30000; GPS=1; YSC=o1EVGXJ0H7I',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36',
                'referer': 'https://www.youtube.com'
            }
            respons = requests.get(url=url, headers=headers)
            # print(respons)
            json_str = re.findall(
                'var ytInitialPlayerResponse = (.*?);var', respons.text)[0]
            # print(json_str)
            json_data = json.loads(json_str)
            video_url = json_data['streamingData']['adaptiveFormats'][0]['url']
            audio_url = json_data['streamingData']['adaptiveFormats'][-2]['url']

            # print(video_url)
            # print(audio_url)

            title = json_data['videoDetails']['title']
            s = ['\n', '，', '。', ' ', '—', '”', '？', '“', '（', '）',
                 '、', '|', '/', '\\', '"', '【', '】', '&', ';', '.']
            for i in s:
                title = title.replace(i, '')
            print(f'Video Title："{title}"')

            print("Downloading...")
            # audio_content = requests.get(url=audio_url, headers=headers, stream=True).content
            # video_content = requests.get(url=video_url, headers=headers, stream=True).content

            if not checkVideoExit.youtubeaudio(inp):
                # Download audio
                cmd = f"yt-dlp -o, --output {title} {inp}"
                os.system(cmd)

                cmd1 = f"ffmpeg -i {title}.webm -acodec libmp3lame {title}.mp3"
                os.system(cmd1)
                shutil.move(f"{title}.mp3","Download/Audio")
                os.remove(f"{title}.webm")

                self.top = Toplevel()
                windown_download = download_complete(self.top)

            else:
                self.top = Toplevel()
                windown_Exit = invalue_input_file_exist(self.top)

        # Download Douyin Audio
        elif re.findall(douyin_checkurl, inp):

            headers = {

                'cookie': 'ttwid=1%7CierYIogGd1GwG83kmIkHxy9RrtQaf2QxGK7oMYvME-U%7C1657091868%7Ccd3bdbc32c8e356620009da92d6cdb53c1d9108099049eec06ab702302c72d73; douyin.com; strategyABtestKey=1657091870.704; s_v_web_id=verify_l599pqqx_64Mimpua_nCsC_45zg_A4rU_QVYN1FuQuCs5; passport_csrf_token=263e588f55bb28153ca04cc6d4d5bc85; passport_csrf_token_default=263e588f55bb28153ca04cc6d4d5bc85; AVATAR_FULL_LOGIN_GUIDE_TIMESTAMP=%221657091870547%22; AVATAR_FULL_LOGIN_GUIDE_COUNT=%221%22; ttcid=5309b3fadf864e64818d6983043536b229; THEME_STAY_TIME=%22299503%22; IS_HIDE_THEME_CHANGE=%221%22; odin_tt=c36d086199f1a2101a1e3522cc7305ffdf3e7149791e0f712f2e7952936cf96e3b953e063856a90e0e62b1fc2a96e306f9e0c0961d5883295acc2a0bc149963f; pwa_guide_count=%223%22; __ac_nonce=062c53f2e004c2041b128; __ac_signature=_02B4Z6wo00f01NKTQxwAAIDBsZmDdSSq6dDSs0eAAFZnQH1gq-dJxLNLyH7l3Pw4qvVrx8Xye-olHZPOonKcXRVsGRLsFddQhG6jLMgEgtaDHNUK0DNvO8zYVygde9sJZuE.T-sqGHcE4XY4f4; home_can_add_dy_2_desktop=%221%22; msToken=bzaNQ7UA4cOtSNjxa5dAv4Ia0p24m6xbD7SOyGX680T6UTbc_GUwC-xIPjs67loKa97h4Y_0Gjtwt0Y58NncCEdm-e78w23EBhsS3beWQuZGAQ92Lrnpk6FAHdLeU5o=; tt_scid=iDCSeh.J0Ips3kRPB0YSQGAS5nE4Y.cRKWxQFikmRQC6gktnDKROBQuWMkm0PYMa2f37; msToken=mK-fNgB8xg2xEEq3W04mFCNsZJmWy7f9mlN_ymgWqRqOqTcP7i_-kAta7yh0nKRtRp7qi-xQymjGEDY0HoYEqdwKwHQhDByjUXG_P-ZoZZBrp8YcPy5J7KFtJ4FerLA=',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

            }
            response = requests.get(url=url, headers=headers)
            # print(response.text)

            title = \
                re.findall('<meta data-react-helmet="true" name="lark:url:video_title" content=(.*?)/>', response.text)[
                    0]
            s = ['\n', '，', '。', ' ', '—', '”', '？', '“', '（', '）',
                 '、', '|', '/', '\\', '"', '【', '】', '&', ';', '.']
            for i in s:
                title = title.replace(i, '')
            print(f'Video Title："{title}"')

            # print(response.text)
            video_url = re.findall('src(.*?)src%22%3A%', response.text)[0]
            video_url = requests.utils.unquote(
                video_url).replace('":"', 'http:')

            if not checkVideoExit.douyinaudio(inp):

                video = requests.get(
                    url=video_url, headers=headers, stream=True)
                video_size = int(video.headers.get('Content-Length'))
                self.bar['value'] = 0
                chunk_size = 1024 * 1024 * 2
                self.bar['maximum'] = video_size

                with open(title + '.mp4', mode='wb') as f:
                    for video_chunk in video.iter_content(chunk_size=chunk_size):
                        f.write(video_chunk)
                        print(len(video_chunk))
                        print(video_size)
                        self.bar['value'] += len(video_chunk)
                        self.bar.update()

                try:
                    cmd1 = f"ffmpeg -i {title}.mp4 -f mp3 douyin_{title}.mp3"
                    os.system(cmd1)
                    shutil.move(f'.\\douyin_{title}.mp3', '.\\Download\\Audio')
                    os.remove(title + '.mp4')
                    self.bar['value'] = 0
                    self.top = Toplevel()
                    windown_download = download_complete(self.top)

                except:
                    os.remove(title + '.mp4')
            else:
                self.top = Toplevel()
                windown_Exit = invalue_input_file_exist(self.top)

        return flag
