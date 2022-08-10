from tkinter import *
from PIL import ImageTk,Image

cevap = []
sayaç = 0
sonuç = 0

pencere = Tk()
pencere.title("Aklındaki sayıyı okuyacağım")

kart1 = ImageTk.PhotoImage(Image.open("kart1.png"))
kart2 = ImageTk.PhotoImage(Image.open("kart2.png"))
kart3 = ImageTk.PhotoImage(Image.open("kart3.png"))
kart4 = ImageTk.PhotoImage(Image.open("kart4.png"))
kart5 = ImageTk.PhotoImage(Image.open("kart5.png"))
kart6 = ImageTk.PhotoImage(Image.open("kart6.png"))

liste = [kart1, kart2, kart3, kart4, kart5, kart6]

ekran = Label(image=liste[sayaç])
ekran.grid(row=1, column=0, columnspan=3)

def ileri(gelen):
    global sayaç
    global ekran
    global evet
    global yok
    global cevap
    global sonuç
    cevap.append(gelen)
    if sayaç == 5:
        ekran.grid_forget()
        evet = Button(text="Var", state=DISABLED, padx=20, pady=5)
        evet.grid(row=2, column=2)
        yok = Button(pencere, text="Yok", state=DISABLED, padx=20, pady=5)
        yok.grid(row=2, column=0)
        çıkış = Button(pencere, text="Çıkmak için bas", pady=5, command=quit)
        çıkış.grid(row=2, column=1)
        if cevap[0]== "evet":
            sonuç += 1
        if cevap[1]== "evet":
            sonuç += 2
        if cevap[2] == "evet":
            sonuç += 4
        if cevap[3] == "evet":
            sonuç += 8
        if cevap[4] == "evet":
            sonuç += 16
        if cevap[5] == "evet":
            sonuç += 32
        e = Label(text=("Aklından tuttuğun sayı:{}".format(sonuç)))
        e.grid(row=0, column=1)
    else:
        e = Label(text="Tuttuğun sayı burda varmı")
        e.grid(row=0, column=1)
        sayaç += 1
        ekran.grid_forget()
        ekran = Label(image=liste[sayaç])
        ekran.grid(row=1, column=0, columnspan=3)
        evet = Button(pencere, text="Var", padx=20, pady=5, command=lambda :ileri("evet"))
        evet.grid(row=2, column=2)
        yok = Button(pencere, text="Yok", padx=20, pady=5, command=lambda :ileri("yok"))
        yok.grid(row=2, column=0)
        çıkış = Button(pencere, text="Çıkmak için bas", state=DISABLED, pady=5)
        çıkış.grid(row=2, column=1)    
e = Label(text="Tuttuğun sayı burda varmı")
e.grid(row=0, column=1)
evet = Button(pencere, text="Var", padx=20, pady=5, command=lambda :ileri("evet"))
evet.grid(row=2, column=2)
yok = Button(pencere, text="Yok", padx=20, pady=5, command=lambda :ileri("yok"))
yok.grid(row=2, column=0)
çıkış = Button(pencere, text="Çıkmak için bas", pady=5, command=quit)
çıkış.grid(row=2, column=1)
pencere.mainloop()
        
