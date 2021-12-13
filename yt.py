from pytube import YouTube
from tkinter import *  

link, yt = '', ''
i=2

def pegaentry(link):
    link = entry.get()
    return faz(link)


def contador():
    global i
    i += 1
    return i-1
    
    
root = Tk()
root.title('YouTube Downloader')

janela = Label(root, bg='pink')
janela.grid()

entry = Entry(janela, width = 30,textvariable = link, bg='white', font=("Arial", 20))
entry.bind('<Return>',pegaentry)
entry.grid(row=1)

texto = Text(janela, height = 1, bg='white', width = 30, font=("Arial", 20))
texto.tag_configure("tag_name", justify='center')
texto.insert("1.0", "Digite sua URL: ")
texto.tag_add("tag_name", "1.0", "end")
texto.grid(row=0)

def criabtn(x,stream):
    botao = Button(janela,text=stream,bg='white',font=("Arial", 20), command = lambda: baixar(x))
    botao.grid(row=contador())

    
def baixar(x):
    ys = yt.streams.get_by_itag(x)
    print(x)
    ys.download('C:/Users/pdv/desktop/')

    
def sep(i, types):
    i = str(i)
    lista = i.split('"')
    if types == 'audio':
        importante = lista[1:6:2]
        print(importante)
        criabtn(importante[0],importante[1:])
    else:
        importante = lista[1:8:2]
        print(importante)
        criabtn(importante[0],importante[1:])
        

def tempo(length):
    if length >= 60:
        if length % 60 != 0:
            return f"Tamanho do vídeo: {length // 60} minutos e {length % 60} segundos"
        else:
            return f"Tamanho do vídeo: {length // 60} minutos"
    else:
        return f"Tamanho do vídeo: {length} segundos"  
    
    
def faz(link):
    global yt
    yt = YouTube(link)
    #Título do Vídeo
    print("Título do vídeo: ",yt.title)
    #Número de views
    print("Números de views: ",yt.views)
    #Tamanho do Vídeo
    print(tempo(yt.length))
    #Nota
    print("Porcentagem Likes: ",f"{(yt.rating*20):.2f}", "%")
    #All Streams
    print()
    print("Video streams avaliable: \n")
    for i in yt.streams.filter(only_video=True, mime_type="video/mp4"):
        sep(i, 'video')
        
    texto = Text(janela, height = 1, bg='white', width = 30, font=("Arial", 20))
    texto.tag_configure("tag_name", justify='center')
    texto.insert("1.0", "Apenas audio")
    texto.tag_add("tag_name", "1.0", "end")
    texto.grid(row=contador())
    
    print()
    print("Audio streams avaliable: \n")
    for i in yt.streams.filter(only_audio=True, mime_type="audio/mp4"):
        sep(i, 'audio')
    
root.mainloop()
