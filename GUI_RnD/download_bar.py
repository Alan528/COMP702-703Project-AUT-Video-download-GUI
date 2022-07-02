# Import the libraries file
from libraries import *
from notification_screen import *

#purpose of this global variable is let the system know which button has been clicked 
# and called exactly that function for downloading
flag = 0

class download(object):

    # Creat GUI for download bar
    def __init__(dl, master):

        # Create a tkinter frame
        dl.master = master
        dl.frame = Frame(dl.master)
        
        #Insert icon and title
        dl.master.title("Downloading....")
        dl.master.wm_iconbitmap("./image/download_icon.ico")

        # Set the geometry of frame and background
        dl.master.geometry("500x400")
        dl.master.configure(bg = "#ffffff")
        dl.canvas = Canvas(
            dl.master,
            bg = "#ffffff",
            height = 400,
            width = 500,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        dl.canvas.place(x = 0, y = 0)

        dl.background_img = PhotoImage(file = f"./image/download_bg.png")
        dl.background = dl.canvas.create_image(
            250.0, 199.0,
            image=dl.background_img)

        #Download bar process
        dl.bar = Progressbar(dl.master, orient='horizontal', length=300)
        dl.bar.pack(pady=35)

        #MP4 has sound button
        dl.img3 = PhotoImage(file = f"./image/mp4_has_sound_btt.png")
        dl.b3 = Button(
            dl.master,
            image = dl.img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = dl.dl_mp4_has_sound,
            relief = "flat")

        dl.b3.place(
            x = 110, y = 136,
            width = 267,
            height = 47)

        #MP4 video no sound button
        dl.img2 = PhotoImage(file = f"./image/mp4_no_sound_btt.png")
        dl.b2 = Button(
            dl.master,
            image = dl.img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = dl.dl_mp4_no_sound,
            relief = "flat")

        dl.b2.place(
            x = 110, y = 201,
            width = 267,
            height = 47)

        #MP3 button
        dl.img1 = PhotoImage(file = f"./image/mp3_btt.png")
        dl.b1 = Button(
            dl.master,
            image = dl.img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = dl.dl_mp3,
            relief = "flat")

        dl.b1.place(
            x = 110, y = 266,
            width = 267,
            height = 47)

        #Exit button
        dl.img0 = PhotoImage(file = f"./image/exit_btt.png")
        dl.b0 = Button(
            dl.master,
            image = dl.img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = dl.master.destroy,
            relief = "flat")

        dl.b0.place(
            x = 393, y = 341,
            width = 79,
            height = 36)

        dl.master.resizable(False, False)

#========== Finished for interface ===========

    # Define action for button when user click on it. it will call the download in system.

    #function for downloading mp4 has sound, when user click on mp4 has sound button
    def dl_mp4_has_sound(self):
        
        flag = 1
        print("MP4 has sound button clicked")
        print("value button:", flag, "\n\n")

        #make download bar running
        task = 10
        x = 0
        while(x < task):
            tm.sleep(1)
            self.bar['value'] += 10
            x += 1
            self.master.update_idletasks()

        #this code for displaying a downloaded notification
        self.top = Toplevel()
        windown_download = download_complete(self.top)

        #Reset the download bar process
        self.bar['value'] = 0
        self.master.update_idletasks()

        return flag

    #function for downloading mp4 no sound, when user click on mp4 no sound button
    def dl_mp4_no_sound(self):
        
        flag = 2
        print("MP4 no sound button clicked")
        print("value button:", flag, "\n\n")

        
        #make download bar running
        task = 10
        x = 0
        while(x < task):
            tm.sleep(1)
            self.bar['value'] += 10
            x += 1
            self.master.update_idletasks()

        #this code for displaying a downloaded notification
        self.top = Toplevel()
        windown_download = download_complete(self.top)

        #Reset the download bar process
        self.bar['value'] = 0
        self.master.update_idletasks()

        return flag
        
    #function for downloading mp3, when user click on mp3 button
    def dl_mp3(self):
        
        flag = 3
        print("MP3 button clicked")
        print("value button:", flag, "\n\n")

        #make download bar running
        task = 10
        x = 0
        while(x < task):
            tm.sleep(1)
            self.bar['value'] += 10
            x += 1
            self.master.update_idletasks()

        #this code for displaying a downloaded notification
        self.top = Toplevel()
        windown_download = download_complete(self.top)

        #Reset the download bar process
        self.bar['value'] = 0
        self.master.update_idletasks()

        return flag
