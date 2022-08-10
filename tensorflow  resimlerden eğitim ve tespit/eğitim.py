from tkinter import *
import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2
from PIL import Image,ImageTk
from tkinter.simpledialog import askstring
from tkinter import messagebox
cam = cv2.VideoCapture(0)
liste = [[],[]]
pencere = Tk()
r = IntVar()
sayı = 0
row = 3
sınıf = []
def sor():
    global r,sayı,row,sınıf
    if row == 6:
        messagebox.showerror("En fazla 3","En Fazla 3 Sınıf")
    else:
        cevap = askstring("Sınıf Adı","Sınıf Adı:")
        sınıf.append(cevap)
        exec("radiobutton{} = Radiobutton(pencere,text=cevap,variable=r,value={})".format(sayı,sayı))
        exec("radiobutton{}.grid(row=row,column=0)".format(sayı))
        row += 1
        sayı += 1
img = 0
def fotoğraf():
    global img2,r,sınıf,liste,row
    if row != 3:
        img2 = cv2.resize(img2,(224,224))
        liste[0].append(img2)
        liste[1].append(r.get())
    else:
        messagebox.showerror("Sınıf Eklenmedi","Sınıf Eklenmedi")
def yoket():
    global çık,liste
    if len(liste[0]) == 0:
        pass
    else:
        çık = 1
pencere.title("Kamera")
pencere.resizable(0,0)
pencere.geometry("+0+0")
canvas = Canvas(width=400,height=400,bg="white",highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)
düğme = Button(text="Fotoğraf çek",padx=20,pady=10,command=lambda : fotoğraf())
düğme.grid(row=1,column=0)
düğme2 = Button(text="Sınıf Ekle",padx=20,pady=10,command=lambda : sor())
düğme2.grid(row=1,column=1)
düğme3 = Button(text="Eğitimi Başlat",padx=20,pady=10,command=lambda : yoket())
düğme3.grid(row=2,column=0,columnspan=2)
çık = 0
while 1:
    if çık == 1:
        break
    _,img = cam.read()
    img = cv2.resize(img,(400,400))
    img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    resim = canvas.create_image(200,200,image=img)
    canvas.update()
    canvas.delete(resim)
cam.release()
pencere.destroy()
pencere.mainloop()
liste[0] = np.array(liste[0],np.uint8)
liste[1] = np.array(liste[1],np.uint8)
(train_images, train_labels) = liste
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(224, 224)),
    keras.layers.Dense(1000, activation='tanh'),
    keras.layers.Dense(len(sınıf))
])
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=120)
model.save('saved_model/my_model')
dosya = open("saved_model/classes.txt","w",encoding="utf-8")
dosya.write("sınıf = {}".format(sınıf))
dosya.close()
