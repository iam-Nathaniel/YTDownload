import tkinter
import customtkinter
from pytubefix import YouTube
from pytubefix.cli import on_progress



def startDownload():
  try:
    ytLink = link.get()
    ytObject = YouTube(ytLink, on_progress_callback = on_progress)
    video = ytObject.streams.get_highest_resolution()

    title.configure(text=ytObject.title, text_color='white')
    finishLabel.configure(text='')
    video.download()
    finishLabel.configure(text='Successfully Downloaded', text_color='green')
  except:
    finishLabel.configure(text='Download Error', text_color='red')
  

def on_progress(stream, chunk, bytes_remaining):
  total_size = stream.filesize
  bytes_downloaded = total_size - bytes_remaining
  completionRate = bytes_downloaded / total_size * 100
  rate = str(int(completionRate))
  downloadRate.configure(text=rate + '%')
  downloadRate.update()
  # print(completionRate)
  progessBar.set(float(completionRate) / 100)



#System Settings
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')


#App Frame
app = customtkinter.CTk()
app.geometry('720x480')
app.title('YouTube Downloader')



#adding ui Components
title = customtkinter.CTkLabel(app, text='Insert YT Link',text_color='yellow')
title.pack(padx=20, pady=20)


# link input
url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=500, height=35, textvariable=url)
link.pack()

# finished downloading
finishLabel = customtkinter.CTkLabel(app, text='')
finishLabel.pack()


# progress percentage
downloadRate = customtkinter.CTkLabel(app, text='0%')
downloadRate.pack()

progessBar = customtkinter.CTkProgressBar(app, width=400)
progessBar.set(0)
progessBar.pack(padx=10, pady=10)


# download
download = customtkinter.CTkButton(app, text='Download', command=startDownload)
download.pack(padx=20, pady=20)


# Run App
app.mainloop()