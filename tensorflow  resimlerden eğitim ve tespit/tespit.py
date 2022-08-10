from tkinter import *
import tensorflow as tf
from tensorflow import keras
import cv2
import numpy as np
from PIL import Image,ImageTk
model = tf.keras.models.load_model('saved_model/my_model')
dosya = open("saved_model/classes.txt","r",encoding="utf-8")
dosya = dosya.readlines()
for i in dosya:
    exec(i)
cam = cv2.VideoCapture(0)
pencere = Tk()
pencere.title("Kamera")
pencere.resizable(0,0)
pencere.geometry("+0+0")
canvas = Canvas(width=400,height=550,bg="white",highlightthickness=0)
canvas.pack()
while 1:
    _,img = cam.read()
    img = cv2.resize(img,(400,400))
    img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    resim = canvas.create_image(200,200,image=img)
    img2 = cv2.resize(img2,(224,224))
    probability_model = tf.keras.Sequential([model,tf.keras.layers.Softmax()])
    predictions = probability_model.predict(np.array([img2],np.uint8))
    a = sınıf[np.argmax(predictions[0])]
    b = round((predictions[0][np.argmax(predictions[0])]/1)*100,0)
    b = "%"+str(b)
    yazı = canvas.create_text(200,450,text=str(a),font=("italic",15))
    yazı2 = canvas.create_text(200,500,text=str(b),font=("italic",15))
    canvas.update()
    canvas.delete(yazı)
    canvas.delete(yazı2)
    canvas.delete(resim)
cam.release()
pencere.destroy()
pencere.mainloop()

