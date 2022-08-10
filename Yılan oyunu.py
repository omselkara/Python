from tkinter import *
from tkinter import messagebox
from time import sleep
import random
from datetime import *
from PIL import Image
import winsound
xkafa = 72
başla = 0
ykafa = 2
sayı = 1
yer = 37
skor = 0
an1 = datetime.now()
listeisim = []
kafayön = "sağ"
def keya(event):
    global kafayön, başla, xkafa,ykafa,kafayön,listeisim, an1
    if not başla:
        başla = 1
    key = event.char
    an2 = datetime.now()
    if an2.microsecond - an1.microsecond >= 200000 or an2.second-an1.second >= 1:
        if key == "w" and kafayön != "yukarı" and kafayön != "aşağı":
            kafayön = "yukarı"
        if key == "s" and kafayön != "aşağı" and kafayön != "yukarı":
            kafayön = "aşağı"
        if key == "d" and kafayön != "sağ" and kafayön != "sol":
            kafayön = "sağ"
        if key == "a" and kafayön != "sol" and kafayön != "sağ":
            kafayön = "sol"
        for isim in listeisim:
            if [xkafa,ykafa,kafayön] not in isim[0].dönüş:
                isim[0].dönüş.append([xkafa,ykafa,kafayön])
        an1 = datetime.now()
def ölme():
    global skor, yazı
    messagebox.showerror("Öldün", "Yaptığın Skor:{}".format(skor))
    quit()
def hareket():
    global xkafa, ykafa, kafayön, başla,listeisim
    if başla:
        if kafayön == "yukarı":
            ykafa -= 70
            canvas.move(kafa, 0, -70)
        if kafayön == "aşağı":
            ykafa += 70
            canvas.move(kafa, 0, 70)
        if kafayön == "sol":
            xkafa -= 70
            canvas.move(kafa, -70, 0)
        if kafayön == "sağ":
            xkafa += 70
            canvas.move(kafa, 70, 0)
        for isim in listeisim:
            for dönüşyer in isim[0].dönüş:
                if isim[0].x == dönüşyer[0] and isim[0].y == dönüşyer[1]:
                    isim[0].yön = dönüşyer[2]
                    isim[0].dönüş.remove(isim[0].dönüş[isim[0].dönüş.index(dönüşyer)])
            if isim[0].yön == "sağ":
                isim[0].x += 70
                canvas.move(isim[1], 70, 0)
            if isim[0].yön == "sol":
                isim[0].x -= 70
                canvas.move(isim[1], -70, 0)
            if isim[0].yön == "yukarı":
                isim[0].y -= 70
                canvas.move(isim[1], 0, -70)
            if isim[0].yön == "aşağı":
                isim[0].y += 70
                canvas.move(isim[1], 0, 70)
    for i in listeisim:
        if xkafa == i[0].x and ykafa == i[0].y:
            ölme()
    if xkafa < 2 or xkafa > 1262:
        ölme()
    if ykafa < 2 or ykafa > 762:
        ölme()
class yılan():
    def __init__(self):
        if len(listeisim) >= 1:
            son = len(listeisim)-1
            self.dönüş = []
            for asd in listeisim[son][0].dönüş:
                if asd not in self.dönüş:
                    self.dönüş.append(asd)
            self.yön = listeisim[son][0].yön
            if listeisim[son][0].yön == "sol":
                self.x = listeisim[son][0].x + 70
                self.y = listeisim[son][0].y
            if listeisim[son][0].yön == "sağ":
                self.x = listeisim[son][0].x - 70
                self.y = listeisim[son][0].y
            if listeisim[son][0].yön == "yukarı":
                self.x = listeisim[son][0].x 
                self.y = listeisim[son][0].y + 70
            if listeisim[son][0].yön == "aşağı":
                self.x = listeisim[son][0].x
                self.y = listeisim[son][0].y - 70
        else:
            self.dönüş = []
            self.yön = kafayön
            if kafayön == "sol":
                self.x = xkafa + 70
                self.y = ykafa
            if kafayön == "sağ":
                self.x = xkafa - 70
                self.y = ykafa
            if kafayön == "yukarı":
                self.x = xkafa 
                self.y = ykafa + 70
            if kafayön == "aşağı":
                self.x = xkafa 
                self.y = ykafa - 70
def meyveyendi():
    global eski_satır,eski_sütun,satır,sütun, meyve, skor,yazı, yer,listeisim
    skor += 1
    canvas.delete(yazı)
    if skor == 10:
        yer = 47
    if skor == 100:
        yer = 57
    if skor == 1000:
        yer = 67
    yazı = canvas.create_text(yer,15, text="Skor:{}".format(skor),font=("italic", 18), fill="blue")
    run = 1
    while run == 1:
        run = 0 
        while satır == eski_satır:
            satır = random.randint(0,9)*70 + 2
        while sütun == eski_sütun:
            sütun = random.randint(0,17)*70 + 2
        for i in listeisim:
            if i[0].x == sütun and i[0].y == satır:
                run = 1
    canvas.delete(meyve)
    meyve = canvas.create_rectangle(sütun,satır,sütun+70,satır+70,fill="red")
    eski_satır = satır
    eski_sütun = sütun
    yılanoluştur()
def yılanoluştur():
    global sayı,listeisim
    exec("kare{} = yılan()".format(sayı))
    exec("kare{}isim = canvas.create_rectangle(kare{}.x, kare{}.y, kare{}.x+70, kare{}.y+70, fill='green')".format(sayı,sayı,sayı,sayı,sayı))
    exec("listeisim.append([kare{}, kare{}isim])".format(sayı, sayı))
    sayı += 1
pencere = Tk()
pencere.title("Yılan Oyunu")
canvas = Canvas(pencere, width=1262, height=722, bg="white")
canvas.pack()
yazı = canvas.create_text(37,15, text="Skor:{}".format(skor),font=("italic", 18),fill="blue")
sıra_sayısı = 0
for y in range(2, 762,70):
    sıra_sayısı += 1
    for x in range(2, 1262, 70):
        if pow(sıra_sayısı, 1, 2) == 1:
            renk = "#aad751"
        else:
            renk = "#a2d149"
        sıra_sayısı += 1
        canvas.create_rectangle(x, y, x+70, y+70, fill=renk,outline=renk)
yılanoluştur()
satır = random.randint(0,9)*70 + 2
eski_satır = satır
sütun = random.randint(0,17)*70 + 2
eski_sütun = sütun
kafa = canvas.create_rectangle(xkafa,ykafa,xkafa+70,ykafa+70, fill="black")
meyve = canvas.create_rectangle(sütun,satır,sütun+70,satır+70,fill="red")
pencere.bind("<Key>", lambda a : keya(a))
while 1:
    canvas.update()
    hareket()
    if ykafa == satır and xkafa == sütun:
        meyveyendi()
    sleep(0.2)
pencere.mainloop()
