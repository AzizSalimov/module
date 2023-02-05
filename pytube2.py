from tkinter import *
import pytube
root = Tk()
root.geometry('600x400')
root.resizable(0,0)
root.title("You Tube video dowload")
Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()

link = StringVar()
Label(root, text = 'Paste Youtube Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)
def Downloader():
    url = pytube.YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    Label(root, text = ' VIDEO DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)
Button(root,text = 'DOWNLOAD VIDEO', font = 'arial 15 bold' ,bg = 'blue', padx = 2, command = Downloader).place(x=180 ,y = 150)
root.mainloop()
