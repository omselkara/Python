from tkinter import *
import time
pencere = Tk()
canvas = Canvas(pencere,width=800,height=400,bg="white")
canvas.pack()
liste = []
class sayı:
    def __init__(self,number,yer,x,y):
        self.sayı = number
        self.yer = yer
        self.x = x
        self.y = y
    def add(yer):
        liste[yer][0].sayı += 1
        if liste[yer][0].sayı == 10:
            liste[yer][0].sayı = 0
            sayı.add(yer-1)
        canvas.itemconfigure(liste[yer][1], text=str(liste[yer][0].sayı))
    @classmethod
    def create(cls,number,x,y):
        cls.isim = sayı(number,len(liste),x,y)
        cls.canv = canvas.create_text(x,y,text=str(number),font=("italic",15))
        liste.append([cls.isim,cls.canv])
for i in range(0,7):
    exec("a{} = sayı.create(0,i*20+100,100)".format(i))
an = time.time()
while 1:
    if 1:
        sayı.add(len(liste)-1)
    canvas.update()
pencere.mainloop()
