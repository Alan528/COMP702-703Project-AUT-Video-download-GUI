#Import the libraries
from tkinter import *
from tkinter.ttk import *
import time

#Create a tkinter frame
interface = Tk()
interface.title("Downloading....")
interface.wm_iconbitmap("./image/download_icon.ico")

#Set the geometry of frame
interface.geometry("400x150")

#Define a function
def start():
   task=10
   x=0
   while(x<task):
      time.sleep(1)
      bar['value']+=10
      x+=1
      interface.update_idletasks()

bar = Progressbar(interface, orient=HORIZONTAL, length=300)
bar.pack(pady=20)

#Create a button
Button(interface, text="Download", command=start).pack(pady=20)

# interface.mainloop()