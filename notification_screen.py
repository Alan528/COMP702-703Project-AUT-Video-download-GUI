from libraries import *


class invalue_input(object):

    # Creat GUI for download bar
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)

        self.master.title("Error Notification!")
        self.master.wm_iconbitmap("./image/error_icon.ico")
        self.master.geometry("400x150")
        self.master.configure(bg="#ffffff")

        self.canvas = Canvas(
            self.master,
            bg="#ffffff",
            height=150,
            width=400,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        title_canvas = Canvas(self.master,
                              bg="#D51A22",
                              height=35,
                              width=400,
                              bd=0,
                              highlightthickness=0,
                              relief="ridge")
        title_canvas.place(x=0, y=5)
        title_canvas.create_text(200, 18, fill="#ffffff", font="Roboto 20 bold",
                                 text="Notification!")

        text_canvas = Canvas(self.master,
                             bg="#ffffff",
                             height=30,
                             width=400,
                             bd=0,
                             highlightthickness=0,
                             relief="ridge")
        text_canvas.place(x=0, y=50)
        text_canvas.create_text(200, 15, fill="#000000", font="Roboto 12 roman",
                                text="Please input a Bilibili,Youtube or Douyin link.")

        # exit button
        self.exit_img = PhotoImage(file=f"./image/exit_red_btt.png")
        self.exit_btt = Button(
            self.master,
            image=self.exit_img,
            bg="#ffffff",
            borderwidth=0,
            highlightthickness=0,
            command=self.onClick,
            relief="flat")

        self.exit_btt.place(
            x=142, y=91,
            width=115,
            height=50)

        self.master.resizable(False, False)

    # when user click on the exit button this function will be run
    def onClick(self):
        self.master.destroy()


# This is a class for the bilibili invalue input. When user input the bilibili link but a video doesn't exist
class invalue_input_bilibili_exist(object):

    # Creat GUI for download bar
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)

        self.master.title("Error Notification!")
        self.master.wm_iconbitmap("./image/error_icon.ico")
        self.master.geometry("400x150")
        self.master.configure(bg="#ffffff")

        self.canvas = Canvas(
            self.master,
            bg="#ffffff",
            height=150,
            width=400,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        title_canvas = Canvas(self.master,
                              bg="#D51A22",
                              height=35,
                              width=400,
                              bd=0,
                              highlightthickness=0,
                              relief="ridge")
        title_canvas.place(x=0, y=5)
        title_canvas.create_text(200, 18, fill="#ffffff", font="Roboto 20 bold",
                                 text="Notification!")

        text_canvas = Canvas(self.master,
                             bg="#ffffff",
                             height=30,
                             width=400,
                             bd=0,
                             highlightthickness=0,
                             relief="ridge")
        text_canvas.place(x=0, y=50)
        text_canvas.create_text(200, 15, fill="#000000", font="Roboto 12 roman",
                                text="Please input an exist Bilibili video link.")

        # exit button
        self.exit_img = PhotoImage(file=f"./image/exit_red_btt.png")
        self.exit_btt = Button(
            self.master,
            image=self.exit_img,
            bg="#ffffff",
            borderwidth=0,
            highlightthickness=0,
            command=self.onClick,
            relief="flat")

        self.exit_btt.place(
            x=142, y=91,
            width=115,
            height=50)

        self.master.resizable(False, False)

    # when user click on the exit button this function will be run
    def onClick(self):
        self.master.destroy()


class invalue_input_douyin_exist(object):

    # Creat GUI for download bar
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)

        self.master.title("Error Notification!")
        self.master.wm_iconbitmap("./image/error_icon.ico")
        self.master.geometry("400x150")
        self.master.configure(bg="#ffffff")

        self.canvas = Canvas(
            self.master,
            bg="#ffffff",
            height=150,
            width=400,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        title_canvas = Canvas(self.master,
                              bg="#D51A22",
                              height=35,
                              width=400,
                              bd=0,
                              highlightthickness=0,
                              relief="ridge")
        title_canvas.place(x=0, y=5)
        title_canvas.create_text(200, 18, fill="#ffffff", font="Roboto 20 bold",
                                 text="Notification!")

        text_canvas = Canvas(self.master,
                             bg="#ffffff",
                             height=30,
                             width=400,
                             bd=0,
                             highlightthickness=0,
                             relief="ridge")
        text_canvas.place(x=0, y=50)
        text_canvas.create_text(200, 15, fill="#000000", font="Roboto 12 roman",
                                text="Please input an exist Douyin video link.")

        # exit button
        self.exit_img = PhotoImage(file=f"./image/exit_red_btt.png")
        self.exit_btt = Button(
            self.master,
            image=self.exit_img,
            bg="#ffffff",
            borderwidth=0,
            highlightthickness=0,
            command=self.onClick,
            relief="flat")

        self.exit_btt.place(
            x=142, y=91,
            width=115,
            height=50)

        self.master.resizable(False, False)

    # when user click on the exit button this function will be run
    def onClick(self):
        self.master.destroy()


# This is a class for the youtube invalue input. When user input the youtube link but a video doesn't exist
class invalue_input_youtube_exist(object):

    # Creat GUI for download bar
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)

        self.master.title("Error Notification!")
        self.master.wm_iconbitmap("./image/error_icon.ico")
        self.master.geometry("400x150")
        self.master.configure(bg="#ffffff")

        self.canvas = Canvas(
            self.master,
            bg="#ffffff",
            height=150,
            width=400,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        title_canvas = Canvas(self.master,
                              bg="#D51A22",
                              height=35,
                              width=400,
                              bd=0,
                              highlightthickness=0,
                              relief="ridge")
        title_canvas.place(x=0, y=5)
        title_canvas.create_text(200, 18, fill="#ffffff", font="Roboto 20 bold",
                                 text="Notification!")

        text_canvas = Canvas(self.master,
                             bg="#ffffff",
                             height=50,
                             width=400,
                             bd=0,
                             highlightthickness=0,
                             relief="ridge")
        text_canvas.place(x=0, y=45)
        text_canvas.create_text(200, 13, fill="#000000", font="Roboto 12 roman",
                                text="Please input an exist youtube video link and ")
        text_canvas.create_text(200, 32, fill="#000000", font="Roboto 12 roman",
                                text="does not copyright infringements.")

        # exit button
        self.exit_img = PhotoImage(file=f"./image/exit_red_btt.png")
        self.exit_btt = Button(
            self.master,
            image=self.exit_img,
            bg="#ffffff",
            borderwidth=0,
            highlightthickness=0,
            command=self.onClick,
            relief="flat")

        self.exit_btt.place(
            x=142, y=91,
            width=115,
            height=50)

        self.master.resizable(False, False)

    # when user click on the exit button this function will be run
    def onClick(self):
        self.master.destroy()


# check file exit or not
class invalue_input_file_exist(object):

    # Creat GUI for download bar
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)

        self.master.title("Error Notification!")
        self.master.wm_iconbitmap("./image/error_icon.ico")
        self.master.geometry("400x150")
        self.master.configure(bg="#ffffff")

        self.canvas = Canvas(
            self.master,
            bg="#ffffff",
            height=150,
            width=400,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        title_canvas = Canvas(self.master,
                              bg="#D51A22",
                              height=35,
                              width=400,
                              bd=0,
                              highlightthickness=0,
                              relief="ridge")
        title_canvas.place(x=0, y=5)
        title_canvas.create_text(200, 18, fill="#ffffff", font="Roboto 20 bold",
                                 text="Notification!")

        text_canvas = Canvas(self.master,
                             bg="#ffffff",
                             height=30,
                             width=400,
                             bd=0,
                             highlightthickness=0,
                             relief="ridge")
        text_canvas.place(x=0, y=50)
        text_canvas.create_text(200, 15, fill="#000000", font="Roboto 12 roman",
                                text="The file exited, ")

        # exit button
        self.exit_img = PhotoImage(file=f"./image/exit_red_btt.png")
        self.exit_btt = Button(
            self.master,
            image=self.exit_img,
            bg="#ffffff",
            borderwidth=0,
            highlightthickness=0,
            command=self.onClick,
            relief="flat")

        self.exit_btt.place(
            x=142, y=91,
            width=115,
            height=50)

        self.master.resizable(False, False)

    # when user click on the exit button this function will be run
    def onClick(self):
        self.master.destroy()


# This is a class for the download complete
class download_complete(object):

    # Creat GUI for download bar
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)

        self.master.title("Process Notification!")
        self.master.wm_iconbitmap("./image/complete_icon.ico")
        self.master.geometry("400x150")
        self.master.configure(bg="#ffffff")

        self.canvas = Canvas(
            self.master,
            bg="#ffffff",
            height=150,
            width=400,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        title_canvas = Canvas(self.master,
                              bg="#036C70",
                              height=35,
                              width=400,
                              bd=0,
                              highlightthickness=0,
                              relief="ridge")
        title_canvas.place(x=0, y=5)
        title_canvas.create_text(200, 18, fill="#ffffff", font="Roboto 20 bold",
                                 text="Notification!")

        text_canvas = Canvas(self.master,
                             bg="#ffffff",
                             height=30,
                             width=400,
                             bd=0,
                             highlightthickness=0,
                             relief="ridge")
        text_canvas.place(x=0, y=50)
        text_canvas.create_text(200, 15, fill="#000000", font="Roboto 12 roman",
                                text="Your video is downloaded!")

        # exit button
        self.exit_img = PhotoImage(file=f"./image/exit_red_btt.png")
        self.exit_btt = Button(
            self.master,
            image=self.exit_img,
            bg="#ffffff",
            borderwidth=0,
            highlightthickness=0,
            command=self.onClick,
            relief="flat")

        self.exit_btt.place(
            x=142, y=91,
            width=115,
            height=50)

        self.master.resizable(False, False)

    # when user click on the exit button this function will be run
    def onClick(self):
        self.master.destroy()

class downloading_remid(object):

    # Creat GUI for download bar
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)

        self.master.title("Process Notification!")
        self.master.wm_iconbitmap("./image/complete_icon.ico")
        self.master.geometry("400x150")
        self.master.configure(bg="#ffffff")

        self.canvas = Canvas(
            self.master,
            bg="#ffffff",
            height=150,
            width=400,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        title_canvas = Canvas(self.master,
                              bg="#036C70",
                              height=35,
                              width=400,
                              bd=0,
                              highlightthickness=0,
                              relief="ridge")
        title_canvas.place(x=0, y=5)
        title_canvas.create_text(200, 18, fill="#ffffff", font="Roboto 20 bold",
                                 text="Notification!")

        text_canvas = Canvas(self.master,
                             bg="#ffffff",
                             height=30,
                             width=400,
                             bd=0,
                             highlightthickness=0,
                             relief="ridge")
        text_canvas.place(x=0, y=50)
        text_canvas.create_text(200, 15, fill="#000000", font="Roboto 12 roman",
                                text="File downloading")

        # exit button
        self.exit_img = PhotoImage(file=f"./image/exit_red_btt.png")
        self.exit_btt = Button(
            self.master,
            image=self.exit_img,
            bg="#ffffff",
            borderwidth=0,
            highlightthickness=0,
            command=self.onClick,
            relief="flat")

        self.exit_btt.place(
            x=142, y=91,
            width=115,
            height=50)

        self.master.resizable(False, False)

    # when user click on the exit button this function will be run
    def onClick(self):
        self.master.destroy()