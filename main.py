import CheckVideo
from libraries import *
from notification_screen import *
from download_bar import *
from undownload import del_file


if __name__ == '__main__':
    class Application(Frame, object):
        def __init__(self, master):
            super(Application, self). \
                __init__(master)

            master.title("The Universal Video Platform Downloader")
            master.wm_iconbitmap("./image/interface.ico")
            master.geometry("1000x600")
            master.configure(bg="#ffffff")

            self.create_widgets()

        def create_widgets(self):
            self.canvas = Canvas(
                self.master,
                bg="#ffffff",
                height=600,
                width=1000,
                bd=0,
                highlightthickness=0,
                relief="ridge")
            self.canvas.place(x=0, y=0)

            # Background for GUI
            self.background_img = PhotoImage(file=f"./image/main_page_bg.png")
            self.background = self.canvas.create_image(
                500.0, 300.0,
                image=self.background_img)

            # Creat a textbox
            self.textbox_img = PhotoImage(
                file=f"./image/main_page_textBox.png")
            self.textbox_bg = self.canvas.create_image(
                683.0, 210.5,
                image=self.textbox_img)

            self.textbox = Entry(
                bd=0,
                bg="#e4edf3",
                highlightthickness=0)

            self.textbox.place(
                x=460.0, y=190,
                width=446.0,
                height=39)

            # Open Download file
            self.img = Image.open('./image/btt_open_folder.png')
            self.img_temp = self.img.resize((49, 40), Image.ANTIALIAS)
            self.folder_img = ImageTk.PhotoImage(self.img_temp)

            self.folder_btt = Button(
                image=self.folder_img,
                bg="#ffffff",
                borderwidth=0,
                highlightthickness=0,
                command=self.btn_open_download_clicked,
                relief="flat")

            self.folder_btt.place(
                x=931, y=191,
                width=49,
                height=40)

            # Download button
            self.download_img = PhotoImage(
                file=f"./image/main_page_download_btt.png")
            self.download_btt = Button(
                image=self.download_img,
                bg="#ffffff",
                borderwidth=0,
                highlightthickness=0,
                command=self.btn_download_clicked,
                relief="flat")

            self.download_btt.place(
                x=445, y=256,
                width=115,
                height=50)

            # Exit button
            self.open_img = PhotoImage(file=f"./image/main_page_exit_btt.png")
            self.open_btt = Button(
                image=self.open_img,
                bg="#ffffff",
                borderwidth=0,
                highlightthickness=0,
                command=self.master.destroy,
                relief="flat")

            self.open_btt.place(
                x=806, y=256,
                width=115,
                height=50)

            #Instant Download Button
            self.instant_download_img = PhotoImage(file=f"btt_instant_download.png")
            self.instant_download_btt = Button(
                image=self.instant_download_img,
                bg="#ffffff",
                borderwidth=0,
                highlightthickness=0,
                command="", #@Jian-Tao please add the function in this line
                relief="flat")

            self.instant_download_btt.place(
                x=594, y=306,
                width=187,
                height=50)

            # Bilibili button
            self.Bilibili_img = PhotoImage(file=f"./image/btt_bilibili.png")
            self.Bilibili_btt = Button(
                image=self.Bilibili_img,
                borderwidth=0,
                highlightthickness=0,
                command=self.btn_bilibili_clicked,
                relief="flat")

            self.Bilibili_btt.place(
                x=417, y=459,
                width=171,
                height=65)

            # Douyin platform button
            self.douyin_img = PhotoImage(file=f"./image/btt_douyin.png")
            self.douyin_btt = Button(
                image=self.douyin_img,
                borderwidth=0,
                highlightthickness=0,
                command=self.btn_douyin_clicked,
                relief="flat")

            self.douyin_btt.place(
                x=613, y=459,
                width=171,
                height=65)

            # Youtube platform button
            self.youtube_img = PhotoImage(file=f"./image/btt_youtube.png")
            self.youtube_btt = Button(
                image=self.youtube_img,
                borderwidth=0,
                highlightthickness=0,
                command=self.btn_youtube_clicked,
                relief="flat")

            self.youtube_btt.place(
                x=809, y=459,
                width=171,
                height=65)

        def btn_download_clicked(self):

            bilibili_checkurl = "www.bilibili.com"
            youtube_checkurl = "www.youtube.com"
            douyin_checkurl = "www.douyin.com"

            self.top = Toplevel()
            inp = self.textbox.get()
            if re.findall(bilibili_checkurl, inp):
                try:
                    CheckVideo.checkbilibili(inp)
                    windown_download = download(self.top, inp)
                except:
                    window_load = invalue_input_bilibili_exist(self.top)

            elif re.findall(youtube_checkurl, inp):
                try:
                    CheckVideo.checkyoutube(inp)
                    windown_download = download(self.top, inp)
                except:
                    window_load = invalue_input_youtube_exist(self.top)

            elif re.findall(douyin_checkurl, inp):
                try:
                    CheckVideo.checkdouyin(inp)
                    windown_download = download(self.top, inp)
                except:
                    window_load = invalue_input_douyin_exist(self.top)

            else:
                windown_download = invalue_input(self.top)

        # Open bilibili website when user clicked
        def btn_bilibili_clicked(self):
            inp = self.textbox.get()
            if inp == "":
                webbrowser.open('https://www.bilibili.com/')
            elif re.findall(bilibili_checkurl, inp):
                webbrowser.open(inp)
            else:
                webbrowser.open(f'https://search.bilibili.com/all?keyword={inp}')

        # Open youtube website when user clicked
        def btn_youtube_clicked(self):
            inp = self.textbox.get()
            if inp == "":
                webbrowser.open('https://www.youtube.com/')
            elif re.findall(youtube_checkurl, inp):
                webbrowser.open(inp)
            else:
                webbrowser.open(f'https://www.youtube.com/results?search_query={inp}')


        # Open douyin website when user clicked
        def btn_douyin_clicked(self):
            inp = self.textbox.get()
            if inp == "":
                webbrowser.open('https://www.douyin.com/discover')
            elif re.findall(douyin_checkurl, inp):
                webbrowser.open(inp)
            else:
                webbrowser.open(f'https://www.douyin.com/search/{inp}')


        # Open Download document when user clicked
        def btn_open_download_clicked(self):
            os.system('explorer .\\Download')

    del_file()
    test_ff()
    root = Tk()
    root.resizable(False, False)
    app = Application(root)
    app.mainloop()
