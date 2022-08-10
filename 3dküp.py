from math import cos,sin,radians
from tkinter import *
import time,random
from renk_belirle import *
def matrixmul(a,b):
    rowa,cola,rowb,colb = len(a),len(a[0]),len(b),len(b[0])
    if cola!=rowb:
        print("a sütunu b satırına eşit değil")
        return None
    liste = []
    for i in range(0,rowa):
        liste.append([])
        for j in range(0,colb):
            liste[i].append([])
    b2 = []
    for x in range(0,colb):
        b2.append([])
    for y in range(0,rowb):
        for x in range(0,colb):
            b2[x].append(b[y][x])
    b = b2
    del b2
    rowb,colb = colb,rowb
    for i in range(0,rowa):
        for j in range(0,rowb):
            toplam = 0
            for k in range(0,colb):
                toplam += b[j][k]*a[i][k]
            liste[i][j] = toplam
    return liste
def rotatez(x,y,z,derece):
    b = [[x],[y],[z]]
    a = [[cos(radians(derece)),-sin(radians(derece)),0],
         [sin(radians(derece)),cos(radians(derece)),0],
         [0,0,1]]
    x,y,z = matrixmul(a,b)
    x = x[0]
    y = y[0]
    z = z[0]
    return (x,y,z)
def rotatex(x,y,z,derece):
    b = [[x],[y],[z]]
    a = [[1,0,0],
         [0,cos(radians(derece)),-sin(radians(derece))],
         [0,sin(radians(derece)),cos(radians(derece))]]
    x,y,z = matrixmul(a,b)
    x = x[0]
    y = y[0]
    z = z[0]
    return (x,y,z)
def rotatey(x,y,z,derece):
    b = [[x],[y],[z]]
    a = [[cos(radians(derece)),0,-sin(radians(derece))],
         [0,1,0],
         [sin(radians(derece)),0,cos(radians(derece))]]
    x,y,z = matrixmul(a,b)
    x = x[0]
    y = y[0]
    z = z[0]
    return (x,y,z)
def project(x,y,z):
    b = [[x],[y],[z]]
    x,y = matrixmul(yansıt,b)
    x,y = x[0],y[0]
    return (x,y)
eski = 0
def motion(event):
    global eski,derecex,derecey,derecez
    if eski != 0:
        derecey += event.x-eski[0]
        derecex += event.y-eski[1]
    eski = [event.x,event.y]
def release(event):
    global eski
    eski = 0
pencere = Tk()
canvas = Canvas(pencere,width=600,height=400,bg="black",highlightthickness=0)
canvas.pack()
canvas.bind("<B1-Motion>",motion)
canvas.bind("<ButtonRelease-1>",release)
an = time.time()
points = [[-50,-50,50],[50,-50,50],[50,50,50],[-50,50,50],[-50,-50,-50],[50,-50,-50],[50,50,-50],[-50,50,-50]]
yansıt = [[1,0,0],[0,1,0]]
derecex = 0
derecey = 0
derecez = 0
bağla = [[0,1,2,3],[4,5,6,7],[0,3,7,4],[1,2,6,5],[0,1,5,4],[3,2,6,7]]
while 1:
    if time.time()-an >= 1/60:
        an = time.time()
        liste = []
        for i in points:
            x,y,z = rotatex(i[0],i[1],i[2],derecex)
            x,y,z = rotatey(x,y,z,derecey)
            x,y = project(x,y,z)
            x += 300
            y += 200
            liste.append([x,y])
            canvas.create_oval(x-10,y-10,x+10,y+10,fill="white",width=0)
        for i in range(0,4):
            canvas.create_line(liste[i],liste[(i+1)%4],fill="white")
            canvas.create_line(liste[i+4],liste[((i+1)%4)+4],fill="white")
            canvas.create_line(liste[i],liste[i+4],fill="white")
        if 0==1:
            for i in bağla:
                list = []
                for a in i:
                    list.append(liste[a])
                canvas.create_polygon(list,fill="white")
        canvas.update()
        canvas.delete(ALL)
pencere.mainloop()
        
        
