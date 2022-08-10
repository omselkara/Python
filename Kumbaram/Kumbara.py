from tkinter import *
from tkinter import ttk
from tkinter import messagebox
dosya  = open("kayıt.txt", "r", encoding="utf-8")
dosya = dosya.readlines()
for i in dosya:
    exec(i)

def artıekle():
    global değer, e, hedef, pencere2, pencere, param
    değer += (float(e.get())*100)/hedef
    param += float(e.get())
    dosya = open("kayıt.txt", "w", encoding="utf-8")
    dosya.write("değer={}".format(değer))
    dosya.write("\n")
    dosya.write("hedef={}".format(hedef))
    dosya.write("\n")
    dosya.write("param={}".format(param))
    pencere2.destroy()
    pencere.destroy()
    aç()
    if değer >= 100:
        messagebox.showinfo("Tebrikler!", "Tebrikler hedefinizi tamamladınız")
        pencere.destroy()
        quit()
def eksiekle():
    global değer, e, hedef, pencere2, pencere, param
    değer -= (float(e.get())*100)/hedef
    param -= float(e.get())
    dosya = open("kayıt.txt", "w", encoding="utf-8")
    dosya.write("değer={}".format(değer))
    dosya.write("\n")
    dosya.write("hedef={}".format(hedef))
    dosya.write("\n")
    dosya.write("param={}".format(param))
    pencere2.destroy()
    pencere.destroy()
    aç()
        
def artı():
    global değer, e, pencere2
    pencere2 = Tk()
    pencere2.title("Kumbaraya para ekle")
    e = Entry(pencere2, width=30)
    e.grid(row=0, column=0, columnspan=3)
    ekle = Button(pencere2, text="Arttır", padx=20,pady=10,command=lambda :artıekle())
    ekle.grid(row=1,column=1)
    pencere2.mainloop()
def eksi():
    global değer, e, pencere2
    pencere2 = Tk()
    pencere.title("kumbaradan para azalt")
    e = Entry(pencere2, width=30)
    e.grid(row=0, column=0, columnspan=3)
    ekle = Button(pencere2, text="Azalt", padx=20,pady=10,command=lambda :eksiekle())
    ekle.grid(row=1,column=1)
    pencere2.mainloop()

def aç():
    global değer, pencere
    pencere = Tk()
    pencere.title("Kumbara")
    pb = ttk.Progressbar(pencere, orient="horizontal", length=300, value=değer)
    pb.grid(row=0, column=0, columnspan=3)
    yüzde = Label(pencere, text="%{}({}TL)".format(round(değer, 2), param))
    yüzde.grid(row=1,column=1)
    artı_düğme = Button(pencere, text="+", bg="green", padx=10, pady=5, font=("italic", 15), command=lambda :artı())
    artı_düğme.grid(row=2, column=2)
    eksi_düğme = Button(pencere, text="-", bg="red", padx=13, pady=5, font=("italic", 15), command=lambda :eksi())
    eksi_düğme.grid(row=3, column=2)
    pencere.mainloop()
aç()



