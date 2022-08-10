from PIL import Image
import numpy as np
from copy import deepcopy
from random import randint
def change(name,name2,startx,starty,renk,fark=100):
    img = np.array(Image.open(name))
    img = img.tolist()
    xrange = range
    gezilen = []
    for y in xrange(len(img)):
        gezilen.append([])
        for x in xrange(len(img[0])):
            gezilen[y].append(False)
    x = deepcopy(startx)
    y = deepcopy(starty)
    yapılanlar = []
    gezilen[y][x] = True
    yönler = ["a","d","w","s"]
    sözlük = ["d","a","s","w"]
    ara = [img[starty][startx][0],img[starty][startx][1],img[starty][startx][2]]
    while 1:
        sol = sağ = yukarı = aşağı = True
        if x>0:
            if not gezilen[y][x-1]:
                if (abs(img[y][x-1][0]-ara[0])+abs(img[y][x-1][1]-ara[1])+abs(img[y][x-1][2]-ara[2]))<fark:
                    sol = False
        if x<len(gezilen[y])-1:
            if not gezilen[y][x+1]:
                if (abs(img[y][x+1][0]-ara[0])+abs(img[y][x+1][1]-ara[1])+abs(img[y][x+1][2]-ara[2]))<fark:
                    sağ = False
        if y>0:
            if not gezilen[y-1][x]:
                if (abs(img[y-1][x][0]-ara[0])+abs(img[y-1][x][1]-ara[1])+abs(img[y-1][x][2]-ara[2]))<fark:
                    yukarı = False
        if y<len(gezilen)-1:
            if not gezilen[y+1][x]:
                if (abs(img[y+1][x][0]-ara[0])+abs(img[y+1][x][1]-ara[1])+abs(img[y+1][x][2]-ara[2]))<fark:
                    aşağı = False
        if ((sol and sağ and yukarı and aşağı) and (len(yapılanlar)==0)):
            break
        else:
            etraf = []
            if not sol:
                etraf.append("a")
            if not sağ:
                etraf.append("d")
            if not yukarı:
                etraf.append("w")
            if not aşağı:
                etraf.append("s")
            if len(etraf)!=0:
                yön = etraf[randint(0,len(etraf)-1)]
                if yön=="a":
                    x -= 1
                if yön=="d":
                    x += 1
                if yön=="w":
                    y -= 1
                if yön=="s":
                    y += 1
                gezilen[y][x] = True
                yapılanlar.append(yön)
            else:
                yön = sözlük[yönler.index(yapılanlar[-1])]
                if yön=="a":
                    x -= 1
                if yön=="d":
                    x += 1
                if yön=="w":
                    y -= 1
                if yön=="s":
                    y += 1
                yapılanlar.pop()
    liste = []
    for y in xrange(0,len(img)):
        print(y)
        liste.append([])
        for x in xrange(0,len(img[0])):
            r = 0
            g = 0
            b = 0
            if gezilen[y][x]:
                r = renk[0]+(img[y][x][0]-ara[0])
                g = renk[1]+(img[y][x][1]-ara[1])
                b = renk[2]+(img[y][x][2]-ara[2])
            else:
                r = img[y][x][0]
                g = img[y][x][1]
                b = img[y][x][2]
            if r<0:
                r = 0
            if r>255:
                r = 255
            if g<0:
                g = 0
            if g>255:
                g = 255
            if b<0:
                b = 0
            if b>255:
                b = 255
            liste[y].append([r,g,b])
    liste = np.asarray(liste,np.uint8)
    liste = Image.fromarray(liste)
    liste.save(name2)
change("s.png","s.png",8,750,[0,99,177],25)
