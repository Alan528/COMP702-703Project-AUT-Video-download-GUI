import re
import tkinter as tk
from urllib import parse
import tkinter.messagebox as msgbox
import webbrowser


class App:

    def __init__(self, width=500, height=300):
        self.w = width
        self.h = height

        # App title
        self.title = 'Universal Video Platform downloader GUI'
        self.root = tk.Tk(className=self.title)

        # user input link
        self.url = tk.StringVar()

        # Identify play source
        self.v = tk.IntVar()
        self.v.set(1)

        # App space  classification
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)

        # App space content set
        group = tk.Label(frame_1, text='Play Channel:', padx=10, pady=10)
        tb = tk.Radiobutton(frame_1, text='Channel 1', variable=self.v, value=1, width=10, height=3)

        label = tk.Label(frame_2, text='Please input the link:')
        entry = tk.Entry(frame_2, textvariable=self.url, highlightthickness=1, width=35)
        play = tk.Button(frame_2, text='Play', font=12, width=2, height=1, command='')

        # Control Layout
        frame_1.pack()
        frame_2.pack()

        # Confirm location
        group.grid(row=0, column=0)
        tb.grid(row=0, column=1)

        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        play.grid(row=0, column=2, ipadx=10, ipady=10)

    def loop(self):
        self.root.resizable(True, True)
        self.root.mainloop()

if __name__=='__main__':
    app=App()
    app.loop()



