import pyaudio,time
import numpy as np
from tkinter import *
import warnings
from PIL import Image
    
warnings.filterwarnings("ignore",category=DeprecationWarning)

RATE = 44100
RES = 1080*16
CHUNK = int(RATE/RES)
limit = 30
wait = RES/2

def listen():
    p=pyaudio.PyAudio()
    stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
                  frames_per_buffer=CHUNK)
    
    liste = []
    started = False
    sayaç = 0
    frame = 0
    while 1:
        data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
        freq = np.average(np.abs(data))/10
        if not started:
            if frame>wait:
                if frame==wait+1:
                    print("started")
                if freq>limit:
                    started = True
                    liste.append(freq)            
            frame += 1
        else:
            if freq<limit:
                sayaç += 1
                if sayaç>RES/2:
                    break
            else:
                sayaç = 0
                liste.append(freq)
    del(liste[-1:-int(wait)])
    stream.stop_stream()
    stream.close()
    p.terminate()
    return liste

def generate_image(liste,name):
    img = np.ones((2000,len(liste)))
    for i in range(len(liste)):
        freq = int(liste[i])
        y = int((len(img)-freq)/2)
        img[y:len(img)-y,i]*=0
    img *= 255
    img = np.array(img,dtype=np.uint8)
    img = Image.fromarray(img)
    img.save(name)
    img.close()

def split_characters(liste):
    pass
    
a = listen()
generate_image(a,"a.png")
