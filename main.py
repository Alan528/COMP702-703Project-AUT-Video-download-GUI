import BilibiliSP
import YoutubeSp
import re
import tkinter as tk

from importlib.resources import path
from tkinter import *


def btn_clicked():
    bilibili_checkurl = "www.bilibili.com"
    youtube_checkurl = "www.youtube.com"

    value = var_link.get()
    # utype = var_type.get()
    utype = '1'

    # userinput = input("1. MP4(Has Sound) 2. MP4(No Sound) 3. MP3: ")

    if re.findall(bilibili_checkurl, value):
        BilibiliSP.bilibili(value, utype)
    elif re.findall(youtube_checkurl, value):
        YoutubeSp.youtube(value, utype)
    else:
        print("Please input a Bilibili or Youtube link")


if __name__ == '__main__':
    interface = Tk()
    interface.title("The Universal Video Platform Downloader")
    interface.wm_iconbitmap("./image/interface.ico")

    interface.geometry("1000x600")
    interface.configure(bg="#ffffff")
    canvas = Canvas(
        interface,
        bg="#ffffff",
        height=600,
        width=1000,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"./image/bilibili-platform-bg.png")
    background = canvas.create_image(
        500.0, 300.0,
        image=background_img)

    # entry place
    entry0_img = PhotoImage(file=f"./image/bilibili_textBox.png")
    entry0_bg = canvas.create_image(
        737.0, 260.5,
        image=entry0_img)

    var_link = tk.StringVar()
    entry0 = tk.Entry(
        textvariable=var_link,
        bd=0,
        bg="#e4edf3",
        highlightthickness=0)

    entry0.place(
        x=514.0, y=241,
        width=446.0,
        height=39)

    # button Download
    img0 = PhotoImage(file=f"./image/bilibili-download-button.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")
    b0.place(
        x=613, y=308,
        width=115,
        height=50)

    img1 = PhotoImage(file=f"./image/bilibili-cancel-button.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        # command=btn_clicked(),
        relief="flat")

    b1.place(
        x=778, y=308,
        width=115,
        height=50)

    interface.resizable(False, False)
    interface.mainloop()
