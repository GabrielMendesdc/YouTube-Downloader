from pytube import YouTube
from tkinter import *  
import urllib.request as url
from PIL import Image, ImageTk
from urllib.request import urlopen
import io

def pegaentry(link):
    global img
    link = entry.get()
    ind = link.index('=') + 1
    try:
        letra = link.index('&')
        imgUrl = f'https://i.ytimg.com/vi/{link[ind:letra]}/hqdefault.jpg'
    except:
         imgUrl = f'https://i.ytimg.com/vi/{link[ind:]}/hqdefault.jpg'
            
    url.urlretrieve(imgUrl, "C:/Users/pdv/desktop/thumb.png")
    img = ImageTk.PhotoImage(file = "C:/Users/pdv/desktop/thumb.png")
    frame = Label(janela)
    bt = Canvas(frame)
    bt.create_image(0, 0, image=img, anchor=NW)
    bt.grid(row=contador())
    frame.grid()
    return faz(link)


link, yt = '', ''
i=2

root = Tk()
root.title('YouTube Downloader')

janela = Label(root, bg='pink')
janela.grid()

entry = Entry(janela, width = 25,textvariable = link, bg='white', font=("Arial", 18))
entry.bind('<Return>',pegaentry)
entry.grid(row=1)

texto = Text(janela, height = 1, bg='white', width = 25, font=("Arial", 18))
texto.tag_configure("tag_name", justify='center')
texto.insert("1.0", "Digite sua URL: ")
texto.tag_add("tag_name", "1.0", "end")
texto.grid(row=0)


def contador():
    global i
    i += 1
    return i-1

    
def criabtn(x,stream):
    botao = Button(janela,text=stream,bg='white',font=("Arial", 18), command = lambda: baixar(x))
    botao.grid(row=contador())
    
    
def baixar(x):
    ys = yt.streams.get_by_itag(x)
    ys.download('C:/Users/pdv/desktop/')
    init()

    
def sep(i, types, length):
    i = str(i)
    lista = i.split('"')
    if types == 'audio':
        importante = lista[1:6:2]
        importante.append(str(length))
        print(importante)
        importante[1] = importante[1].replace('/mp4', '')
        criabtn(importante[0],importante[1:])
    else:
        importante = lista[1:8:2]
        importante.append(length)
        print(importante)
        importante[1] = importante[1].replace('/mp4', '')
        criabtn(importante[0],importante[1:])
        
    
def gigas(length):
    print('tamanho', length)
    listo = ['','bytes', 'KB', 'MB', 'GB', 'TB', 'YB']
    for i in range(8):
        if length <= 1024 ** i:
            tam = length / (1024 ** (i-1))
            tam = round(tam)
            stri = str(f'{tam}{listo[i]}')
            return stri
            

def faz(link):
    global yt
    yt = YouTube(link)
    j=0
    for i in yt.streams.filter(only_video=True, mime_type="video/mp4"):
        tam = gigas(i.filesize_approx)
        if not j >= 5:
            sep(i, 'video', tam)
        j+=1    
    for i in yt.streams.filter(only_audio=True, mime_type="audio/mp4"):
        tam = gigas(i.filesize_approx)
        sep(i, 'audio', tam)

        
root.mainloop()
