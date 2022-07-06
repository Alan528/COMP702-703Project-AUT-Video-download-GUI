# Import the libraries file
import BilibiliSP as bs
import YoutubeSp as ys
from libraries import *
from notification_screen import *
import shutil
import requests
import re
import json
import os
from tqdm import tqdm

# purpose of this global variable is let the system know which button has been clicked
# and called exactly that function for downloading
flag = 0
bilibili_checkurl = "www.bilibili.com"
youtube_checkurl = "www.youtube.com"


class download(object):

    # Creat GUI for download bar
    def __init__(dl, master):

        # Create a tkinter frame
        dl.master = master
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
        dl.bar = Progressbar(dl.master, orient='horizontal', length=300)
        dl.bar.pack(pady=35)

        # MP4 has sound button
        dl.img3 = PhotoImage(file=f"./image/mp4_has_sound_btt.png")
        dl.b3 = Button(
            dl.master,
            image=dl.img3,
            borderwidth=0,
            highlightthickness=0,
            command=dl.dl_mp4_has_sound,
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
            command=dl.dl_mp4_no_sound,
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
            command=dl.dl_mp3,
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
    def dl_mp4_has_sound(self):

            url = 'https://www.bilibili.com/video/BV1RZ4y1e7nc?spm_id_from=333.1007.tianma.4-1-9.click&vd_source=9866f89ed141513a41b93ec0c8d956ef'

            flag = 1
            print("MP4 has sound button clicked")
            print("value button:", flag, "\n\n")

            # if re.findall(bilibili_checkurl, inp):
            #     bs.bilibili(inp, str(flag))  # make sure that where is the link value
            # elif re.findall(youtube_checkurl, inp):
            #     ys.youtube(inp, str(flag))  # make sure that where is the link value

            headers = {
                'referer': 'https://www.bilibili.com/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'

            }
            response = requests.get(url=url, headers=headers)
            # print(response.text) #get the web data

            title = re.findall('<h1 title="(.*?)"', response.text)[0]
            s = ['\n', '，', '。', ' ', '—', '”', '？', '“', '（', '）', '、', '|']
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

            # print("Downloading...")
            # audio_content = requests.get(url=audio_url, headers=headers, stream=True).content
            # video_content = requests.get(url=video_url, headers=headers, stream=True).content

            video = requests.get(url=video_url, headers=headers, stream=True)
            video_size = int(video.headers.get('Content-Length'))
            # video_pbar = tqdm(total=video_size)

            with open(title + '.mp4', mode='wb') as f:

                # make download bar running
                task = 10
                x = 0
                while (x < task):
                    tm.sleep(1)
                    self.bar['value'] += 10
                    x += 1
                    self.master.update_idletasks()

                # for video_chunk in video.iter_content(1024 * 1024 * 2):
                #     f.write(video_chunk)
                #     video_pbar.set_description('Downloading video...')
                #     video_pbar.update(1024 * 1024 * 2)
                # video_pbar.set_description('Completed download video')
                # video_pbar.close()




            # audio = requests.get(url=audio_url, headers=headers, stream=True)
            # audio_size = int(audio.headers.get('Content-Length'))
            # audio_pbar = tqdm(total=audio_size)
            #
            # with open(title + '.mp3', mode='wb') as f:
            #     for audio_chunk in audio.iter_content(1024 * 1024 * 2):
            #         f.write(audio_chunk)
            #         audio_pbar.set_description('Downloading audio...')
            #         audio_pbar.update(1024 * 1024 * 2)
            #     audio_pbar.set_description('Completed download audio')
            #     audio_pbar.close()
            #
            # cmd = f' ffmpeg  -i {title}.mp4 -i {title}.mp3 -acodec copy -vcodec copy bili_{title}.mp4'
            # # use cmd run ffmpeg join video and video
            # os.system(cmd)
            #
            # # move the video into Download folder
            # shutil.move(f'.\\youtube_{title}.mp4', '.\\Download')
            #
            # # delete the video amd audio that not join
            # os.remove(title + '.mp4')
            # os.remove(title + '.mp3')
            #
            # print('Download completed')



            # this code for displaying a downloaded notification
            self.top = Toplevel()
            windown_download = download_complete(self.top)

            # Reset the download bar process
            self.bar['value'] = 0
            self.master.update_idletasks()

            return flag

        # function for downloading mp4 no sound, when user click on mp4 no sound button
    def dl_mp4_no_sound(self):
        inp = 'https://www.bilibili.com/video/BV1RZ4y1e7nc?spm_id_from=333.1007.tianma.4-1-9.click&vd_source=9866f89ed141513a41b93ec0c8d956ef'

        flag = 2
        print("MP4 no sound button clicked")
        print("value button:", flag, "\n\n")

        if re.findall(bilibili_checkurl, inp):
            bs.bilibili(inp, str(flag))  # make sure that where is the link value
        elif re.findall(youtube_checkurl, inp):
            ys.youtube(inp, str(flag))  # make sure that where is the link value

        # make download bar running
        task = 10
        x = 0
        while (x < task):
            tm.sleep(1)
            self.bar['value'] += 10
            x += 1
            self.master.update_idletasks()

        # this code for displaying a downloaded notification
        self.top = Toplevel()
        windown_download = download_complete(self.top)

        # Reset the download bar process
        self.bar['value'] = 0
        self.master.update_idletasks()

        return flag

    # function for downloading mp3, when user click on mp3 button
    def dl_mp3(self):

        inp = 'https://www.bilibili.com/video/BV1RZ4y1e7nc?spm_id_from=333.1007.tianma.4-1-9.click&vd_source=9866f89ed141513a41b93ec0c8d956ef'

        flag = 3
        print("MP3 button clicked")
        print("value button:", flag, "\n\n")

        if re.findall(bilibili_checkurl, inp):
            bs.bilibili(inp, str(flag))  # make sure that where is the link value
        elif re.findall(youtube_checkurl, ):
            ys.youtube(inp, str(flag))  # make sure that where is the link value

        # make download bar running
        task = 10
        x = 0
        while (x < task):
            tm.sleep(1)
            self.bar['value'] += 10
            x += 1
            self.master.update_idletasks()

        # this code for displaying a downloaded notification
        self.top = Toplevel()
        windown_download = download_complete(self.top)

        # Reset the download bar process
        self.bar['value'] = 0
        self.master.update_idletasks()

        return flag
