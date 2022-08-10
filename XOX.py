from tkinter import *
from tkinter import messagebox
from time import sleep
import pyautogui as pag
import random
import keyboard
import os
from datetime import *
from copy import deepcopy
kazanan = ""
yazı = 123
x_durum = []
o_durum = []
tahta = [["___", "___", "___"],
         ["___", "___", "___"],
         ["___", "___", "___"]]
cevaplar = [[[0, 0], [0, 1], [0, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[2, 0], [2, 1], [2, 2]],
            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]],
            [[0, 0], [1, 1], [2, 2]],
            [[0, 2], [1, 1], [2, 0]]]
sıra_sayısı = 0
def sıra_belirle():
    global sıra_sayısı
    mod = pow(sıra_sayısı,1,2)
    if mod == 0:
        return " X "
    else:
        return " O "
def kazanma(tahta):
    kazanan = 0
    for i in cevaplar:
        liste = []
        for y,x in i:
            if tahta[y][x] == " X ":
                liste.append(1)
        if len(liste) == 3:
            kazanan = -1
        liste = []
        for y,x in i:
            if tahta[y][x] == " O ":
                liste.append(1)
        if len(liste) == 3:
            kazanan = 1
        if kazanan != 0:
            break
    return kazanan
def ihtimal(tahta,uzunluk):
    liste = [[tahta,[]]]
    for sıra in range(0,uzunluk):
        if sıra%2 == 1:
            işaret = " X "
        if sıra%2 == 0:
            işaret = " O "
        liste2 = []
        for i in liste:
            run = 1
            if (kazanma(i[0]) == 1 or kazanma(i[0]) == -1):
                run = 0
                liste2.append(i)
            if run:
                for y in range(0,3):
                    for x in range(0,3):
                        if i[0][y][x] == "___":
                            sahte = deepcopy(i[0])
                            sahte[y][x] = işaret
                            sahte2 = deepcopy(i[1])
                            sahte2.append([y,x])
                            liste2.append([sahte,sahte2])
        liste = liste2
    for index,i in enumerate(liste):
        liste[index].append(kazanma(i[0]))
    return liste
def minmax(liste):
    cevaplar = [d for a,s,d in liste]

    for index,i in enumerate(cevaplar):
        if i == 1:
            yer = index
            break
    return liste[yer][1][0]

def bas(event):
    global kazanan, x_durum,o_durum,tahta,cevaplar,sıra_sayısı, yazı
    try:
        x = event.x
        y = event.y    
        if x > 2 and x < 401 and y > 2 and y < 401:
            if x < 135 and x > 2:   
                sütun = 0
            if x > 135 and x < 268:
                sütun = 1
            if x > 268 and x < 401:
                sütun = 2
            if y < 135 and y > 2:   
                satır = 0
            if y > 135 and y < 268:
                satır = 1
            if y > 268 and y < 401:
                satır = 2
    except:
        satır = event[0]
        sütun = event[1]
    sıra = sıra_belirle()
    canvas.delete(yazı)
    if sıra == "O":
        yazı = canvas.create_text(30, 10, text="Sıra X'de")
    else:
        yazı = canvas.create_text(30, 10, text="Sıra O'da")
    if tahta[satır][sütun] == "___":
        sıra_sayısı += 1
        if sıra == " X ":
            x = sütun*133+2
            y = satır*133+2
            canvas.create_line(x, y, x+133, y+133, fill="red")
            canvas.create_line(x+133, y, x, y+133, fill="red")
        if sıra == " O ":
            x = sütun*133+2
            y = satır*133+2
            canvas.create_oval(x, y, x+133, y+133, outline="blue")

        tahta[satır][sütun] = sıra
        if sıra == " X ":
            x_durum.append([sütun, satır])
        else:
            o_durum.append([sütun,satır])
    for cevap_satır in cevaplar:
        kontrol = 0
        for cevap_eleman in cevap_satır:
            for yapılan_eleman in x_durum:
                if yapılan_eleman == cevap_eleman:
                    kontrol += 1
        if kontrol == 3:
            kazanan = " X "
    for cevap_satır in cevaplar:
        kontrol = 0
        for cevap_eleman in cevap_satır:
            for yapılan_eleman in o_durum:
                if yapılan_eleman == cevap_eleman:
                    kontrol += 1
        if kontrol == 3:
            kazanan = "O"
    if kazanan == "O":
        messagebox.showinfo("O kazandı", "O kazandı")
        quit()
    if kazanan == "X":
        messagebox.showinfo("X kazandı", "X kazandı")
        quit()
    if len(x_durum) + len(o_durum) == 9:
        messagebox.showerror("Beraber", "Berabere")
        quit()
    canvas.update()
    
pencere = Tk()
pencere.title("XOX")
canvas = Canvas(pencere, width=400,height=400, bg="white")
canvas.create_line(2, 2, 2, 402,fill="black")
canvas.create_line(135, 2, 135, 402,fill="black")
canvas.create_line(268, 2, 268, 402,fill="black")
canvas.create_line(401, 2, 401, 402,fill="black")
canvas.create_line(2, 2, 402, 2,fill="black")
canvas.create_line(2, 135, 402, 135,fill="black")
canvas.create_line(2, 268, 402, 268, fill="black")
canvas.create_line(2, 401, 402, 401, fill="black")
canvas.bind("<Button-1>", lambda a: bas(a))
canvas.pack()
while 1:
    canvas.update()
    sıra = sıra_belirle()
    if sıra == " O ":
        hepsi = ihtimal(tahta,9-sıra_sayısı)
        print(len(hepsi))
        yer = minmax(hepsi)
        bas(yer)
pencere.mainloop()

