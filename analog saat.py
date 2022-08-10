from tkinter import *
from math import cos,sin,radians
import time,datetime
pencere = Tk()
canvas = Canvas(pencere,width=600,height=600,bg="white",highlightthickness=0)
canvas.pack()
pencere.geometry("+0+0")
canvas.create_oval(50,50,550,550)
def x_y(radius,degree,x,y):
    return (radius*cos(radians(degree))+x,radius*sin(radians(degree))+y)
for i in range(270,270+361,6):
    list1 = x_y(225,i,300,300)
    list2 = x_y(250,i,300,300)
    if i%30 == 0:
        canvas.create_line(list1,list2,width=5)
    else:
        canvas.create_line(list1,list2)
for i in range(1,13):
    list1 = x_y(200,i*30+270,300,300)
    canvas.create_text(list1,text=str(i),font=("italic",30))
a = datetime.datetime.now()
derecesaniye = 270+a.second*6
derecedakika = (270+a.minute*6)+(a.second/2)/6
if a.hour > 12:
    derecesaat = 270+(a.hour-12)*30
else:
    derecesaat = 270+a.hour*6
derecesaat += a.minute/2
list1 = x_y(150,derecesaat,300,300)
saat = canvas.create_line(300,300,list1,width=3)
list1 = x_y(175,derecedakika,300,300)
dakika = canvas.create_line(300,300,list1,width=3)
list1 = x_y(200,derecesaniye,300,300)
saniye = canvas.create_line(300,300,list1,width=3,fill="red")
while 1:
    canvas.delete(saat)
    canvas.delete(dakika)
    canvas.delete(saniye)
    a = datetime.datetime.now()
    derecesaniye = 270+a.second*6
    derecedakika = (270+a.minute*6)+(a.second/2)/6
    if a.hour > 12:
        derecesaat = 270+(a.hour-12)*30
    else:
        derecesaat = 270+a.hour*6
    derecesaat += a.minute/2
    list1 = x_y(150,derecesaat,300,300)
    saat = canvas.create_line(300,300,list1,width=3)
    list1 = x_y(175,derecedakika,300,300)
    dakika = canvas.create_line(300,300,list1,width=3)
    list1 = x_y(200,derecesaniye,300,300)
    saniye = canvas.create_line(300,300,list1,width=3,fill="red")
    canvas.update()
pencere.mainloop()
