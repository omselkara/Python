from tkinter import *
import os
import numpy as np
from PIL import ImageGrab
import time
import pyautogui as pag
import cv2
pag.failsafe = False
def kapatma():
    os.system("shutdown /s /hybrid /t 0")
class window:
    def __init__(self):
        self.pencere = Tk()
        self.pencere.geometry("+500+300")
        self.pencere.title("Kapanıyor")
        self.pencere.attributes("-topmost",1)
        self.canvas = Canvas(self.pencere,width=300,height=150)
        self.canvas.pack()
        self.canvas.bind("<Button>",self.click)
        self.sayaç = time.time()
        self.show()
        self.iptal = False
        self.check()
    def show(self):
        if 60-(int(time.time()-self.sayaç))<=0:
            self.pencere.destroy()
            if not self.iptal:
                kapatma()
                self.iptal = True
        else:
            self.canvas.delete("all")
            self.canvas.create_text(150,30,text=str(60-(int(time.time()-self.sayaç)))+" Saniye içinde kapanacak",anchor="center")
            self.canvas.create_rectangle(100,75,200,125)
            self.canvas.create_text(150,100,text="İptal et",anchor="center")
            self.canvas.update()
    def click(self,event):
        x = event.x
        y = event.y
        if x>100 and x<200 and y>75 and y<125:
            self.iptal = True
            self.pencere.destroy()
    def check(self):
        while 1:
            if self.iptal:
                break
            else:
                self.show()
gereken_saat = int(open("../Dakika.txt","r",encoding="utf-8").readline())*60
while 1:
    x = pag.position()[0]
    y = pag.position()[1]
    sayaç = 0
    while 1:
        hata = 0
        try:
            img = np.array(pag.screenshot())
        except:
            hata = 1
        if not hata:
            break
        time.sleep(2)
    img = cv2.resize(img,(25,25))
    img = img.tolist()
    time.sleep(2)
    while 1:
        if sayaç>=gereken_saat:
            window()
            break
        try:
            img2 = np.array(pag.screenshot())
            img2 = cv2.resize(img2,(25,25))
            img2 = img2.tolist()
        except:
            pass
        x2 = pag.position()[0]
        y2 = pag.position()[1]
        if img!=img2 or abs(x2-x)>=25 or abs(y2-y)>=25:
            sayaç = 0
        img = img2
        x = x2
        y = y2
        time.sleep(2)
        sayaç += 2


