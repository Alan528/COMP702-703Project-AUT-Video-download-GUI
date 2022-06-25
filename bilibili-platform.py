from importlib.resources import path
from tkinter import *

def btn_clicked():
    print("Button Clicked")


interface = Tk()
interface.title("The Universal Video Platform Downloader")
interface.wm_iconbitmap("./image/interface.ico")

interface.geometry("1000x600")
interface.configure(bg = "#ffffff")
canvas = Canvas(
    interface,
    bg = "#ffffff",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"./image/bilibili-platform-bg.png")
background = canvas.create_image(
    500.0, 300.0,
    image=background_img)

entry0_img = PhotoImage(file = f"./image/bilibili_textBox.png")
entry0_bg = canvas.create_image(
    737.0, 260.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#e4edf3",
    highlightthickness = 0)

entry0.place(
    x = 514.0, y = 240,
    width = 446.0,
    height = 39)

img0 = PhotoImage(file = f"./image/bilibili-download-button.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 613, y = 308,
    width = 115,
    height = 50)

img1 = PhotoImage(file = f"./image/bilibili-cancel-button.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 778, y = 308,
    width = 115,
    height = 50)

interface.resizable(False, False)
interface.mainloop()
