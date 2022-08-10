from pyautogui import *
from time import sleep
import os
from tkinter import *
def geç():
    exit()
liste = [60, 120, 180, 300, 600, 900, 1200, 1500, 1800, 2700, 3600, 7200, 10800, 14400, 18000]
sıra = ["1 Dakika", "2 Dakika", "3 Dakika", "5 Dakika", "10 Dakika", "15 Dakika", "20 Dakika", "25 Dakika", "30 Dakika", "45 Dakika", "1 Saat", "2 Saat", "3 Saat", "4 Saat", "5 Saat"]
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
seçenek = OptionMenu(pencere, seçilen,"1 Dakika", "2 Dakika", "3 Dakika", "5 Dakika", "10 Dakika", "15 Dakika", "20 Dakika", "25 Dakika", "30 Dakika", "45 Dakika", "1 Saat", "2 Saat", "3 Saat", "4 Saat", "5 Saat").pack()
hazır = Button(pencere, text="Hazır", padx=19, pady=10 , command=lambda :bitti()).pack()
pencere.mainloop()
saniye = 0
eski = 0
def kapat():
    os.system("shutdown /s /hybrid /t 0")
while 1:
    a = position()
    if a == eski and saniye == hedef:
        kapat()
    if a == eski:
        saniye += 1
    elif a != eski:
        saniye = 0
        eski = a
    sleep(1)
