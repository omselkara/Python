from tkinter import *
from time import sleep
import winsound
import os
def geç():
    exit()
liste = [1800, 3600, 7200]
sıra = ["30 Dakika", "1 Saat", "2 Saat"]
def bitti():
    global liste, sıra, seçilen, hedef, pencere
    seçilen = str(seçilen.get())
    for i in sıra:
        if i == seçilen:
            yeri = sıra.index(i)
            hedef = liste[yeri] + 1
            pencere.destroy()
pencere = Tk()
pencere.protocol('WM_DELETE_WINDOW', geç)
seçilen = StringVar()
seçilen.set("1 Saat")
seçenek = OptionMenu(pencere, seçilen,"30 Dakika", "1 Saat", "2 Saat").pack()
hazır = Button(pencere, text="Hazır", padx=19, pady=10 , command=lambda :bitti()).pack()
pencere.mainloop()
def kapatma():
    os.system("shutdown /s /hybrid /t 0")
def click(event):
    global çık,pencere,run
    if event.x >= 20 and event.x <= 90 and event.y >= 60 and event.y <= 90:
        kapatma()
        pencere.destroy()
        çık = 0
    if event.x >= 110 and event.x <= 180 and event.y >= 60 and event.y <= 90:
        pencere.destroy()
        çık = 0
while 1:
    süre = 0
    saat = hedef+1
    çık = 1
    while çık:
        if süre == saat:
            süre = 0
            winsound.Beep(400,1000)
            pencere = Tk()
            pencere.title("Kapat?")
            pencere.geometry("+583+304")
            canvas = Canvas(pencere, width=200,height=100)
            canvas.pack()
            canvas.create_text(100,10,text="Kapatılsınmı?",font=("italic",15))
            evet = canvas.create_rectangle(20,60,90,90,fill="red",width=2)
            canvas.create_text(55,75,text="Evet",font=("italic",15))
            hayır = canvas.create_rectangle(110,60,180,90,fill="green",width=2)
            canvas.create_text(145,75,text="Hayır",font=("italic",15))
            canvas.bind("<Button-1>", click)
            run = 1
            try:
                while run:
                    if int(süre) == 61:
                        run = 0
                        kapatma()
                    canvas.update()
                    sleep(0.1)
                    süre += 0.1
                pencere.mainloop()
            except:
                pass
        sleep(1)
        süre += 1
    
    
    
    
