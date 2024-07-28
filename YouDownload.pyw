import os 
import tkinter
import customtkinter
from pytube import YouTube
from pytubefix import YouTube
from pytubefix.cli import on_progress
from PIL import Image

user_home = os.path.expanduser("~")
download_path = os.path.join(user_home, 'Downloads')


def startDownload():
    try:
        url = link.get()
        yt = YouTube(url, on_progress_callback=on_progress)
        ys = yt.streams.get_highest_resolution()
        ys.download(download_path, mp3=False)
        title.configure(text=ys.title)    
        finishLabel.configure(text="Download Finished Successfully", text_color="green")
    except:
        finishLabel.configure(text = "Invalid Link", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    progress.configure(text=per + '%')
    progress.update

    bar.set(float(percentage_of_completion) /100)

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("720x480")
root.title("YouDownload")

title = customtkinter.CTkLabel(root, text="Insert Video Link")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(root, width=350, height=50)
link.pack()

finishLabel = customtkinter.CTkLabel(root, text=" ")
finishLabel.pack()

progress = customtkinter.CTkLabel(root, text="0%")
progress.pack()

bar = customtkinter.CTkProgressBar(root, width = 400)
bar.set(0)
bar.pack(padx=10, pady=10)

download = customtkinter.CTkButton(root, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

image_path = os.path.join(os.path.dirname(__file__), 'Images/python.png' )
image = customtkinter.CTkImage(light_image = Image.open(image_path), size=(70, 70))
image_label = customtkinter.CTkLabel(root, image = image, text="")
image_label.place(x=650, y = 410)

label = customtkinter.CTkLabel(root,font=("Arial", 20), text="Made in Python")
label.place(x=500, y = 430)

root.resizable(width=False, height=False)


root.mainloop()