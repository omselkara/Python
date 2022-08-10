from tkinter import *
pencere = Tk()
işlem_sayısı = -1
kontrol = 0
işlem = []
sayılar = []
cevap = 0
yapım = 0
artı_eksi = 0
def sil():
    uzunluk = len(ekran.get()) - 1
    ekran.delete(uzunluk)
    
def ce():
    global işlem_sayısı, kontrol, işlem, sayılar, cevap, yapım
    temizle()
    işlem_sayısı = -1
    kontrol = 0
    işlem = []
    sayılar = []
    cevap = 0
    yapım = 0
def sayı_ekle(sayı):
    sayaç = 0
    global yapım
    if yapım == 1:
        temizle()
        yapım = 0
    for i in ekran.get():
        sayaç += 1
    ekran.insert(sayaç, sayı)
def temizle():
    sayaç = 0
    for i in ekran.get():
        sayaç += 1
    while sayaç != -1:
        ekran.delete(sayaç)
        sayaç -= 1
def topla():
    global işlem, sayılar, işlem_sayısı
    if not ekran.get():
        pass
    else:
        işlem.append("+")
        sayı = ekran.get()
        sayılar.append(sayı)
        temizle()
        işlem_sayısı += 1
def çıkar():
    global işlem, sayılar, işlem_sayısı
    if not ekran.get():
        pass
    else:
        işlem.append("-")
        sayı = ekran.get()
        sayılar.append(sayı)
        temizle()
        işlem_sayısı += 1
def böl():
    global işlem, sayılar, işlem_sayısı
    if not ekran.get():
        pass
    else:
        işlem.append("/")
        sayı = ekran.get()
        sayılar.append(sayı)
        temizle()
        işlem_sayısı += 1
def çarp():
    global işlem, sayılar, işlem_sayısı
    if not ekran.get():
        pass
    else:
        işlem.append("*")
        sayı = ekran.get()
        sayılar.append(sayı)
        temizle()
        işlem_sayısı += 1
def artıeksi():
    global artı_eksi
    if not artı_eksi:
        ekran.insert(0, "-")
        artı_eksi = 1
    else:
        yazı = ekran.get()
        if str(yazı)[0] == "-":
            ekran.delete(0)
            artı_eksi = 0
def eşittir():
    global işlem_sayısı, işlem, sayılar, cevap, kontrol, yapım
    if not ekran.get():
        pass
    else:
        sayı2 = ekran.get()
        while işlem_sayısı != -1:
            if işlem[işlem_sayısı] == "+":
                if not kontrol:
                    cevap = float(sayılar[işlem_sayısı]) + cevap + float(sayı2)    
                    kontrol += 1
                else:
                    cevap = float(sayılar[işlem_sayısı]) + cevap
            if işlem[işlem_sayısı] == "*":
                if not cevap:
                    cevap = 1
                if not kontrol:
                    cevap = float(sayılar[işlem_sayısı]) * cevap * float(sayı2)
                    kontrol += 1
                else:
                    cevap = float(sayılar[işlem_sayısı]) * cevap
            if işlem[işlem_sayısı] == "-":
                if not kontrol:
                    cevap = float(sayılar[işlem_sayısı]) - cevap - float(sayı2)
                    kontrol += 1
                else:
                    cevap = cevap - float(sayılar[işlem_sayısı])    
            if işlem[işlem_sayısı] == "/":
                if not cevap:
                    cevap = 1
                if not kontrol:
                    cevap = float(sayılar[işlem_sayısı]) / cevap / float(sayı2)
                    kontrol += 1
                else:
                    cevap = float(sayılar[işlem_sayısı]) / cevap
            işlem_sayısı -= 1
        temizle()
        noktalımı = str(cevap)[-1]
        if type(cevap) == float and noktalımı == "0":
            cevap = int(cevap)
        if type(cevap) == float:
            cevap = round(cevap, 5)
        ekran.insert(0, cevap)
        işlem = []
        sayılar = []
        kontrol = 0
        cevap = 0
        yapım = 1
            
pencere.title("Hesap Makinesi")
pencere.geometry("323x361")
ekran = Entry(pencere, width=16, font=("italic",27), bg="#dbdbdb")
ekran.grid(row=0,ipady=19,column=0, columnspan=4)
düğme7 = Button(pencere, text="7", padx=27, pady=9, bg="white", font=("italic",14), command=lambda :sayı_ekle(7))
düğme7.grid(row=3, column=0)
düğme8 = Button(pencere, text="8", padx=27, pady=9, bg="white", font=("italic",14), command=lambda :sayı_ekle(8))
düğme8.grid(row=3, column=1)
düğme9 = Button(pencere, text="9", padx=27, pady=9, bg="white", font=("italic",14), command=lambda :sayı_ekle(9))
düğme9.grid(row=3, column=2)
düğme4 = Button(pencere, text="4", padx=27, pady=9, bg="white", font=("italic",14), command=lambda :sayı_ekle(4))
düğme4.grid(row=4, column=0)
düğme5 = Button(pencere, text="5", padx=27, pady=9, bg="white", font=("italic",14), command=lambda :sayı_ekle(5))
düğme5.grid(row=4, column=1)
düğme6 = Button(pencere, text="6", padx=27, pady=9, bg="white", font=("italic",14), command=lambda :sayı_ekle(6))
düğme6.grid(row=4, column=2)
düğme1 = Button(pencere, text="1", padx=27, pady=9, bg="white", font=("italic",14), command=lambda :sayı_ekle(1))
düğme1.grid(row=5, column=0)
düğme2= Button(pencere, text="2", padx=27, pady=9, bg="white", font=("italic",14), command=lambda :sayı_ekle(2))
düğme2.grid(row=5, column=1)
düğme3 = Button(pencere, text="3", padx=27, pady=9, bg="white", font=("italic",14), command=lambda :sayı_ekle(3))
düğme3.grid(row=5, column=2)
düğme0 = Button(pencere, text="0", padx=27, pady=9.5, bg="white", font=("italic",14), command=lambda :sayı_ekle(0))
düğme0.grid(row=6, column=1)
düğmeX = Button(pencere, text="X", padx=29, pady=12, font=("italic", 12), command=lambda :çarp())
düğmeX.grid(row=3, column=3)
düğmeböl = Button(pencere, text="/", padx=30, pady=9, font=("italic", 15), command=lambda :böl())
düğmeböl.grid(row=2, column=3)
düğmeçık = Button(pencere, text="-", padx=30, pady=9, font=("italic", 15), command=lambda :çıkar())
düğmeçık.grid(row=4, column=3)
düğmetopla = Button(pencere, text="+", padx=27, pady=9, font=("italic", 15), command=lambda :topla())
düğmetopla.grid(row=5, column=3)
düğmeeşit= Button(pencere, text="=", padx=27, pady=8, bg="#80bdff", font=("italic",16), command=lambda :eşittir())
düğmeeşit.grid(row=6, column=3)
düğmesil= Button(pencere, text="Sil", padx=26, pady=13, font=("italic", 11), command=lambda :sil())
düğmesil.grid(row=2, column=2)
düğmeC= Button(pencere, text="C", padx=28, pady=13, font=("italic",11), command= lambda :temizle())
düğmeC.grid(row=2, column=1)
düğmeCE= Button(pencere, text="CE", padx=23, pady=13, font=("italic", 11), command=lambda :ce())
düğmeCE.grid(row=2, column=0)
düğmeartı_eksi= Button(pencere, text="+/-", padx=25, pady=12.9, bg="white", font=("italic",12), command=lambda :artıeksi())
düğmeartı_eksi.grid(row=6, column=0)
düğmenokta= Button(pencere, text=".", padx=25, pady=1, bg="white", font=("italic",20), command=lambda :sayı_ekle("."))
düğmenokta.grid(row=6, column=2)
pencere.mainloop()
