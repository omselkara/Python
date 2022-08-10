from math import cos,sin,radians,pi
from tkinter import *
import time,random
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
def rotatexw(x,y,z,w,derece):
    a = [[cos(radians(derece)),0,0,-sin(radians(derece))],
         [0,1,0,0],
         [0,0,1,0],
         [sin(radians(derece)),0,0,cos(radians(derece))]]
    b = [[x],[y],[z],[w]]
    x,y,z,w = matrixmul(a,b)
    x,y,z,w = x[0],y[0],z[0],w[0]
    return (x,y,z,w)
def rotatewz(x,y,z,w,derece):
    a = [[1,0,0,0],
         [0,1,0,0],
         [0,0,cos(radians(derece)),-sin(radians(derece))],
         [0,0,sin(radians(derece)),cos(radians(derece))]]
    b = [[x],[y],[z],[w]]
    x,y,z,w = matrixmul(a,b)
    x,y,z,w = x[0],y[0],z[0],w[0]
    return (x,y,z,w)
def rotatexy(x,y,z,w,derece):
    a = [[cos(radians(derece)),-sin(radians(derece)),0,0],
         [sin(radians(derece)),cos(radians(derece)),0,0],
         [0,0,1,0],
         [0,0,0,1]]
    b = [[x],[y],[z],[w]]
    x,y,z,w = matrixmul(a,b)
    x,y,z,w = x[0],y[0],z[0],w[0]
    return (x,y,z,w)
def rotatexz(x,y,z,w,derece):
    a = [[cos(radians(derece)),0,-sin(radians(derece)),0],
         [0,1,0,0],
         [sin(radians(derece)),0,cos(radians(derece)),0],
         [0,0,0,1]]
    b = [[x],[y],[z],[w]]
    x,y,z,w = matrixmul(a,b)
    x,y,z,w = x[0],y[0],z[0],w[0]
    return (x,y,z,w)
distance = 2
def project3d(x,y,z):
    b = [[x],[y],[z]]
    a = [[1,0,0],
         [0,1,0]]
    x,y = matrixmul(a,b)
    x,y = x[0],y[0]
    return (x,y)
def project4d(x,y,z,w):
    b = [[x],[y],[z],[w]]
    f = 1/(distance-w)
    a = [[f,0,0,0],
         [0,f,0,0],
         [0,0,f,0]]
    x,y,z = matrixmul(a,b)
    x,y,z = x[0],y[0],z[0]
    x *= 100
    y *= 100
    z *= 100
    return (x,y,z)
pencere = Tk()
canvas = Canvas(pencere,width=1366,height=768,bg="black",highlightthickness=0)
canvas.pack()
pencere.attributes("-fullscreen",1)
an = time.time()
points = [[-1,-1,-1,-1],[1,-1,-1,-1],[1,1,-1,-1],[-1,1,-1,-1],[-1,-1,1,-1],[1,-1,1,-1],[1,1,1,-1],[-1,1,1,-1],
          [-1,-1,-1,1],[1,-1,-1,1],[1,1,-1,1],[-1,1,-1,1],[-1,-1,1,1],[1,-1,1,1],[1,1,1,1],[-1,1,1,1]]
derece = 0
derecex = 0
while 1:
    if time.time()-an >= 1/60:
        an = time.time()
        liste = []
        for x,y,z,w in points:
            x,y,z,w = rotatewz(x,y,z,w,derece)
            x,y,z,w = rotatexy(x,y,z,w,derece)
            x,y,z = project4d(x,y,z,w)
            x,y,z = rotatex(x,y,z,100)
            x,y = project3d(x,y,z)
            x,y = x+1366/2,y+768/2
            liste.append([x,y])
            canvas.create_oval(x-10,y-10,x+10,y+10,fill="white",width=0)
        for i in range(0,4):
            canvas.create_line(liste[i],liste[(i+1)%4],fill="white",width=5)
            canvas.create_line(liste[i+4],liste[((i+1)%4)+4],fill="white",width=5)
            canvas.create_line(liste[i],liste[i+4],fill="white",width=5)
            canvas.create_line(liste[i+8],liste[((i+1)%4)+8],fill="white",width=5)
            canvas.create_line(liste[i+12],liste[((i+1)%4)+12],fill="white",width=5)
            canvas.create_line(liste[i+8],liste[i+12],fill="white",width=5)
        for i in range(0,8):
            canvas.create_line(liste[i],liste[i+8],fill="white",width=5)
        canvas.update()
        canvas.delete(ALL)
        derece += 1
pencere.mainloop()
        
        
