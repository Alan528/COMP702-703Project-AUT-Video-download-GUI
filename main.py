import re
import tkinter as tk
from urllib import parse
import tkinter.messagebox as msgbox
import webbrowser

class App:
    # 重写构造函数
    def __int__(self,width=500,height=300):
        self.w = width
        self.h =height

        self.title='Video GUI'
        self.root = tk.Tk(className=self.title)
        self.url = tk.StringVar()
        self.v=tk.IntVar()
        self.v.set(1)


        frame_1 = tk.Frame(self.root)
        fram_2 = tk.Frame(self.root)


        group = tk.Label(frame_1,text='play way',padx=10,pady=10)
        tb = tk.Radiobutton(frame_1,text='only way',variable=self.url, value=1, width=10,height=3)

        lable1 = tk.Label(fram_2,text='Please input the url')
        entry = tk.Entry(fram_2,textvariable=self.url, highlightcolor='Fuchsia',highli)