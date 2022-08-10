from tkinter import *
import random
import time
import math
import os
import neat
import pickle
listekareisim = [[[],[],[],[]],
                 [[],[],[],[]],
                 [[],[],[],[]],
                 [[],[],[],[]]]
kare_renk = {"2":(238,228,218),"4":(237,224,200),"8":(245, 149, 99),"16":(245, 149, 99),"32":(246,124,95),"64":(246,94,59),"128":(237,207,114),"256":(237, 204, 97),"512":(236, 200, 80),"1024":(236, 195, 63),"2048":(237, 193, 45),"4096":(255, 61, 61)}
sayı_renk = {"2":(114,105,96), "4":(118,109,100),"8":(249, 246, 242),"16":(249, 246, 242),"32":(249,246,242),"64":(249,246,242),"128":(246, 237, 215),"256":(247, 243, 232),"512":(252, 245, 237),"1024":(251, 246, 240),"2048":(246, 247, 241),"4096":(248, 248, 246)}
def renk(renkler):
    r = renkler[0]
    g = renkler[1]
    b = renkler[2]
    return "#%02x%02x%02x" %(int(r),int(g),int(b))
def kenarsız_kare(x1,y1,x2,y2,çap=25,**diğer):
    noktalar = [
        [x1+çap,y1],
        [x2-çap,y1],
        [x2,y1],
        [x2,y1+çap],
        [x2,y2-çap],
        [x2,y2],
        [x2-çap,y2],
        [x1+çap,y2],
        [x1,y2],
        [x1,y2-çap],
        [x1,y1+çap],
        [x1,y1]]
    return canvas.create_polygon(noktalar,**diğer,smooth=1)
evet = 1
def keya(event):
    global listekareisim,skor,evet
    w = 1
    s = 1
    d = 1
    a = 1
    event = event.lower()
    if event == "w" and evet == 1:
        evet = 0
        hamle = 0
        for y in range(1,4):
            for x in range(0,4):
                sahtex = x
                sahtey = y
                run = 1
                while run == 1:
                    if len(listekareisim[sahtey][sahtex]) > 0 and sahtey != 0:
                        if len(listekareisim[sahtey-1][sahtex]) < 1:
                            sayı = 0
                            while sayı != 120:    
                                canvas.move(listekareisim[sahtey][sahtex][1],0,-5)
                                canvas.move(listekareisim[sahtey][sahtex][2],0,-5)
                                listekareisim[sahtey][sahtex][0].y -= 5
                                sayı += 5
                                canvas.update()
                            listekareisim[sahtey][sahtex],listekareisim[sahtey-1][sahtex] = listekareisim[sahtey-1][sahtex],listekareisim[sahtey][sahtex]
                            sahtey -= 1
                            hamle += 1
                        else:
                            if listekareisim[sahtey-1][sahtex][0].tip == listekareisim[sahtey][sahtex][0].tip:
                                canvas.delete(listekareisim[sahtey-1][sahtex][1])
                                canvas.delete(listekareisim[sahtey-1][sahtex][2])
                                canvas.delete(listekareisim[sahtey][sahtex][1])
                                canvas.delete(listekareisim[sahtey][sahtex][2])
                                skor += int(listekareisim[sahtey-1][sahtex][0].tip)
                                kare_oluştur((sahtex+1)*120-50,(sahtey+1)*120-50,"{}".format(str(int(listekareisim[sahtey-1][sahtex][0].tip)+int(listekareisim[sahtey][sahtex][0].tip))))
                                listekareisim[sahtey-1][sahtex] = []
                            else:
                                run = 0
                    else:
                        run = 0
        
        if listekareisim[2][0] != [] and listekareisim[2][1] != [] and listekareisim[2][2] != [] and listekareisim[2][3] != [] and listekareisim[1][0] != [] and listekareisim[1][1] != [] and listekareisim[1][2] != [] and listekareisim[1][3] != [] and listekareisim[3][0] != [] and listekareisim[3][1] != [] and listekareisim[3][2] != [] and listekareisim[3][3] != []:
            pass
        else:
            if random.randint(1,3) == 2:
                while 1:
                    x = random.randint(0,3)
                    y = random.randint(1,3)
                    if listekareisim[y][x] == []:
                        break
                x = (x+1)*120-50
                y = (y+1)*120-50
                tip = random.randint(1,10)
                if tip == 1:
                    kare_oluştur(x,y,"4")
                else:
                    kare_oluştur(x,y,"2")
        if hamle == 0:
            w = 0
        evet = 1
    if event == "s" and evet == 1:
        evet = 0
        hamle = 0
        for y in range(0,3):
            for x in range(0,4):
                sahtex = x
                sahtey = 2-y
                run = 1
                while run == 1:
                    if len(listekareisim[sahtey][sahtex]) > 0 and sahtey != 3:
                        if len(listekareisim[sahtey+1][sahtex]) < 1:
                            sayı = 0
                            while sayı != 120:
                                canvas.move(listekareisim[sahtey][sahtex][1],0,5)
                                canvas.move(listekareisim[sahtey][sahtex][2],0,5)
                                listekareisim[sahtey][sahtex][0].y += 5
                                sayı += 5
                                canvas.update()
                            listekareisim[sahtey][sahtex],listekareisim[sahtey+1][sahtex] = listekareisim[sahtey+1][sahtex],listekareisim[sahtey][sahtex]
                            sahtey += 1
                            hamle += 1
                        else:
                            if listekareisim[sahtey+1][sahtex][0].tip == listekareisim[sahtey][sahtex][0].tip:
                                canvas.delete(listekareisim[sahtey+1][sahtex][1])
                                canvas.delete(listekareisim[sahtey+1][sahtex][2])
                                canvas.delete(listekareisim[sahtey][sahtex][1])
                                canvas.delete(listekareisim[sahtey][sahtex][2])
                                skor += int(listekareisim[sahtey+1][sahtex][0].tip)
                                kare_oluştur((sahtex+1)*120-50,(sahtey+1)*120-50,"{}".format(str(int(listekareisim[sahtey+1][sahtex][0].tip)+int(listekareisim[sahtey][sahtex][0].tip))))
                                listekareisim[sahtey+1][sahtex] = []
                            else:
                                run = 0                  
                    else:
                        run = 0
        if listekareisim[2][0] != [] and listekareisim[2][1] != [] and listekareisim[2][2] != [] and listekareisim[2][3] != [] and listekareisim[1][0] != [] and listekareisim[1][1] != [] and listekareisim[1][2] != [] and listekareisim[1][3] != [] and listekareisim[0][0] != [] and listekareisim[0][1] != [] and listekareisim[0][2] != [] and listekareisim[0][3] != []:
            pass
        else:
            if random.randint(1,3) == 2:
                while 1:
                    x = random.randint(0,3)
                    y = random.randint(0,2)
                    if listekareisim[y][x] == []:
                        break
                x = (x+1)*120-50
                y = (y+1)*120-50
                tip = random.randint(1,10)
                if tip == 1:
                    kare_oluştur(x,y,"4")
                else:
                    kare_oluştur(x,y,"2")
        if hamle == 0:
            s = 0
        evet = 1
    if event == "d" and evet == 1:
        evet = 0
        hamle = 0
        for x in range(0,3):
            for y in range(0,4):
                sahtex = 2-x
                sahtey = y
                run = 1
                while run == 1:
                    if len(listekareisim[sahtey][sahtex]) > 0 and sahtex != 3:
                        if len(listekareisim[sahtey][sahtex+1]) < 1:
                            sayı = 0
                            while sayı != 120:
                                canvas.move(listekareisim[sahtey][sahtex][1],5,0)
                                canvas.move(listekareisim[sahtey][sahtex][2],5,0)
                                listekareisim[sahtey][sahtex][0].x += 5
                                sayı += 5
                                canvas.update()
                            listekareisim[sahtey][sahtex],listekareisim[sahtey][sahtex+1] = listekareisim[sahtey][sahtex+1],listekareisim[sahtey][sahtex]
                            sahtex += 1
                            hamle += 1
                        else:
                            if listekareisim[sahtey][sahtex+1][0].tip == listekareisim[sahtey][sahtex][0].tip:
                                canvas.delete(listekareisim[sahtey][sahtex+1][1])
                                canvas.delete(listekareisim[sahtey][sahtex+1][2])
                                canvas.delete(listekareisim[sahtey][sahtex][1])
                                canvas.delete(listekareisim[sahtey][sahtex][2])
                                skor += int(listekareisim[sahtey][sahtex+1][0].tip)
                                kare_oluştur((sahtex+1)*120-50,(sahtey+1)*120-50,"{}".format(str(int(listekareisim[sahtey][sahtex+1][0].tip)+int(listekareisim[sahtey][sahtex][0].tip))))
                                listekareisim[sahtey][sahtex+1] = []
                            else:
                                run = 0                     
                    else:
                        run = 0
        if listekareisim[2][0] != [] and listekareisim[2][1] != [] and listekareisim[2][2] != [] and listekareisim[1][0] != [] and listekareisim[1][1] != [] and listekareisim[1][2] != [] and listekareisim[3][0] != [] and listekareisim[3][1] != [] and listekareisim[3][2] != [] and listekareisim[0][0] != [] and listekareisim[0][1] != [] and listekareisim[0][2] != []:
            pass
        else:
            if random.randint(1,3) == 2:
                while 1:
                    x = random.randint(0,2)
                    y = random.randint(0,3)
                    if listekareisim[y][x] == []:
                        break
                x = (x+1)*120-50
                y = (y+1)*120-50
                tip = random.randint(1,10)
                if tip == 1:
                    kare_oluştur(x,y,"4")
                else:
                    kare_oluştur(x,y,"2")
        if hamle == 0:
            d = 0
        evet = 1
    if event == "a" and evet == 1:
        evet = 0
        hamle = 0
        for x in range(1,4):
            for y in range(0,4):
                sahtex = x
                sahtey = y
                run = 1
                while run == 1:
                    if len(listekareisim[sahtey][sahtex]) > 0 and sahtex != 0:
                        if len(listekareisim[sahtey][sahtex-1]) < 1:
                            sayı = 0
                            while sayı != 120:
                                canvas.move(listekareisim[sahtey][sahtex][1],-5,0)
                                canvas.move(listekareisim[sahtey][sahtex][2],-5,0)
                                listekareisim[sahtey][sahtex][0].x -= 5
                                sayı += 5
                                canvas.update()
                            listekareisim[sahtey][sahtex],listekareisim[sahtey][sahtex-1] = listekareisim[sahtey][sahtex-1],listekareisim[sahtey][sahtex]
                            sahtex -= 1
                            hamle += 1
                        else:
                            if listekareisim[sahtey][sahtex-1][0].tip == listekareisim[sahtey][sahtex][0].tip:
                                canvas.delete(listekareisim[sahtey][sahtex-1][1])
                                canvas.delete(listekareisim[sahtey][sahtex-1][2])
                                canvas.delete(listekareisim[sahtey][sahtex][1])
                                canvas.delete(listekareisim[sahtey][sahtex][2])
                                skor += int(listekareisim[sahtey][sahtex-1][0].tip)
                                kare_oluştur((sahtex+1)*120-50,(sahtey+1)*120-50,"{}".format(str(int(listekareisim[sahtey][sahtex-1][0].tip)+int(listekareisim[sahtey][sahtex][0].tip))))
                                listekareisim[sahtey][sahtex-1] = []
                            else:
                                run = 0                    
                    else:
                        run = 0
        if listekareisim[2][3] != [] and listekareisim[2][1] != [] and listekareisim[2][2] != [] and listekareisim[1][3] != [] and listekareisim[1][1] != [] and listekareisim[1][2] != [] and listekareisim[3][3] != [] and listekareisim[3][1] != [] and listekareisim[3][2] != [] and listekareisim[0][3] != [] and listekareisim[0][1] != [] and listekareisim[0][2] != []:
            pass
        else:
            if random.randint(1,3) == 2:
                while 1:
                    x = random.randint(1,3)
                    y = random.randint(0,3)
                    if listekareisim[y][x] == []:
                        break
                x = (x+1)*120-50
                y = (y+1)*120-50
                tip = random.randint(1,10)
                if tip == 1:
                    kare_oluştur(x,y,"4")
                else:
                    kare_oluştur(x,y,"2")
        if hamle == 0:
            a = 0
        evet = 1
class kare:
    def __init__(self,x,y,tip):
        self.x = x
        self.y = y
        self.tip = tip
def kare_oluştur(x,y,tip):
    global kare_renk,sayı_renk,sayı,listekareisim
    exec("kare{}isim = kare({},{},{})".format(sayı,x,y,tip))
    exec("kare{} = kenarsız_kare({},{},{}+100,{}+100,fill=renk(kare_renk['{}']))".format(sayı,x,y,x,y,tip))
    exec("kare{}sayı = canvas.create_text({}+50,{}+50,text={},fill=renk(sayı_renk['{}']),font=('italic',25))".format(sayı,x,y,tip,tip))
    exec("listekareisim[int((y+50)/120)-1][int((x+50)/120)-1] = [kare{}isim,kare{},kare{}sayı]".format(sayı,sayı,sayı))
    sayı += 1
def kontrol():
    global listekareisim,öl
    yapma = 0
    for a in listekareisim:
        for i in a:
            if i == []:
                yapma = 1
    if not yapma:
        hamle_sayısı = 0
        for y in range(1,3):
            for x in range(0,4):
                if listekareisim[y][x] != [] and listekareisim[y-1][x] != []:
                    if listekareisim[y][x][0].tip == listekareisim[y-1][x][0].tip:
                        hamle_sayısı += 1
                if listekareisim[y][x] != [] and listekareisim[y+1][x] != []:
                    if listekareisim[y][x][0].tip == listekareisim[y+1][x][0].tip:
                        hamle_sayısı += 1
        for x in range(1,3):
            for y in range(0,4):
                if listekareisim[y][x] != [] and listekareisim[y][x-1] != []:
                    if listekareisim[y][x][0].tip == listekareisim[y][x-1][0].tip:
                        hamle_sayısı += 1
                if listekareisim[y][x] != [] and listekareisim[y][x+1] != []:
                    if listekareisim[y][x][0].tip == listekareisim[y][x+1][0].tip:
                        hamle_sayısı += 1
        if hamle_sayısı == 0:
            öl = 1
pencere = Tk()
pencere.title("2048")
pencere.geometry("+350+50")
canvas = Canvas(pencere,width=600,height=600,bg="white",highlightthickness=False)
canvas.pack()
def geç():
    global öl
    öl = 1
düğme = Button(pencere,text="Geç",padx=20,pady=10,command= geç)
düğme.pack()
#pencere.bind("<Key>", lambda a : keya(a.keysym))
kenarsız_kare(50,50,550,550,çap=25,fill=renk((187,173,160)))
for y in range(70,550,120):
    for x in range(70,550,120):
        kenarsız_kare(x,y,x+100,y+100,çap=25,fill=renk((204, 192, 179)))
w = 1
s = 1
d = 1
a = 1
en_büyük_taş = 0
en_büyük = canvas.create_text(300,575,text=en_büyük_taş,fill="black",font=("italic", 30))
def eval_genomes(genomes,config):
    global sayı,an,öl,skor,eskiskor,yazı,evet,listekareisim,canvas,kare_renk,sayı_renk,sayı,listekareisim,en_büyük_taş,en_büyük
    nets = []
    ge = []
    for genome_id,genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        ge.append(genome)
        listekareisim = [[[],[],[],[]],
                         [[],[],[],[]],
                         [[],[],[],[]],
                         [[],[],[],[]]]
        evet = 1
        x1 = random.randint(1,4)
        y1 = random.randint(1,4)
        while 1:
            x2 = random.randint(1,4)
            if x2 != x1:
                break
        while 1:    
            y2 = random.randint(1,4)
            if y2 != y1:
                break
        x1 = x1*120-50
        x2 = x2*120-50
        y1 = y1*120-50
        y2 = y2*120-50
        sayı = 0
        kare_oluştur(x1,y1,"2")
        kare_oluştur(x2,y2,"2")
        an = time.time()
        öl = 0
        skor = 0
        eskiskor = 0
        yazı = canvas.create_text(300,25,text=skor,fill="black",font=("italic", 30))
        while 1:
            if time.time()-an > 1/60:
                an = time.time()
                if listekareisim[0][0] != []:
                    yer1 = int(listekareisim[0][0][0].tip)
                else:
                    yer1 = 0
                if listekareisim[0][1] != []:
                    yer2 = int(listekareisim[0][1][0].tip)
                else:
                    yer2 = 0
                if listekareisim[0][2] != []:
                    yer3 = int(listekareisim[0][2][0].tip)
                else:
                    yer3 = 0
                if listekareisim[0][3] != []:
                    yer4 = int(listekareisim[0][3][0].tip)
                else:
                    yer4 = 0
                if listekareisim[1][0] != []:
                    yer5 = int(listekareisim[1][0][0].tip)
                else:
                    yer5 = 0
                if listekareisim[1][1] != []:
                    yer6 = int(listekareisim[1][1][0].tip)
                else:
                    yer6 = 0
                if listekareisim[1][2] != []:
                    yer7 = int(listekareisim[1][2][0].tip)
                else:
                    yer7 = 0
                if listekareisim[1][3] != []:
                    yer8 = int(listekareisim[1][3][0].tip)
                else:
                    yer8 = 0
                if listekareisim[2][0] != []:
                    yer9 = int(listekareisim[2][0][0].tip)
                else:
                    yer9 = 0
                if listekareisim[2][1] != []:
                    yer10 = int(listekareisim[2][1][0].tip)
                else:
                    yer10 = 0
                if listekareisim[2][2] != []:
                    yer11 = int(listekareisim[2][2][0].tip)
                else:
                    yer11 = 0
                if listekareisim[2][3] != []:
                    yer12 = int(listekareisim[2][3][0].tip)
                else:
                    yer12 = 0
                if listekareisim[3][0] != []:
                    yer13 = int(listekareisim[3][0][0].tip)
                else:
                    yer13 = 0
                if listekareisim[3][1] != []:
                    yer14 = int(listekareisim[3][1][0].tip)
                else:
                    yer14 = 0
                if listekareisim[3][2] != []:
                    yer15 = int(listekareisim[3][2][0].tip)
                else:
                    yer15 = 0
                if listekareisim[3][3] != []:
                    yer16 = int(listekareisim[3][3][0].tip)
                else:
                    yer16 = 0
                output = nets[len(nets)-1].activate((yer1,yer2,yer3,yer4,yer5,yer6,yer7,yer8,yer9,yer10,yer11,yer12,yer13,yer14,yer15,yer16))
                eskilistekareisim = listekareisim
                if output[0] > 0.5:
                    keya("w")
                while evet != 1:
                    time.sleep(0.1)
                if output[1] > 0.5:
                    keya("s")
                while evet != 1:
                    time.sleep(0.1)
                if output[2] > 0.5:
                    keya("d")
                while evet != 1:
                    time.sleep(0.1)
                if output[3] > 0.5:
                    keya("a")
                while evet != 1:
                    time.sleep(0.1)
                if output[0] <= 0.5 and output[1] <= 0.5 and output[2] <= 0.5 and output[3] <= 0.5:
                    öl = 1
                max_hata = 0
                for i in output:
                    if i > 0.5:
                        max_hata += 1
                hata = 0
                yapma = 0
                for a in listekareisim:
                    for i in a:
                        if i == []:
                            yapma = 1
                if not yapma:                        
                    if output[0] > 0.5:
                        hamle = 0
                        for y in range(1,4):
                            for x in range(0,4):
                                if listekareisim[y][x] != [] and listekareisim[y-1][x] != [] and listekareisim[y][x][0].tip == listekareisim[y-1][x][0].tip:
                                    hamle += 1
                        if hamle == 0:
                            hata += 1
                    if output[1] > 0.5:
                        hamle = 0
                        for y in range(0,3):
                            for x in range(0,4):
                                if listekareisim[(2-y)][x] != [] and listekareisim[(2-y)+1][x] != [] and listekareisim[2-y][x][0].tip == listekareisim[(2-y)+1][x][0].tip:
                                    hamle += 1
                        if hamle == 0:
                            hata += 1
                    if output[2] > 0.5:
                        hamle = 0
                        for x in range(0,3):
                            for y in range(0,4):
                                if listekareisim[y][2-x] != [] and listekareisim[y][(2-x)+1] != [] and listekareisim[y][2-x][0].tip == listekareisim[y][(2-x)+1][0].tip:
                                    hamle += 1
                        if hamle == 0:
                            hata += 1
                    if output[3] > 0.5:
                        hamle = 0
                        for x in range(1,4):
                            for y in range(0,4):
                                if listekareisim[y][x] != [] and listekareisim[y][x-1] != [] and listekareisim[y][x][0].tip == listekareisim[y][x-1][0].tip:
                                    hamle += 1
                        if hamle == 0:
                            hata += 1
                if hata == max_hata:
                    öl = 1
                kontrol()
                if öl == 1:
                    ge[len(ge)-1].fitness -= 1
                    evet = 0
                    for i in listekareisim:
                        for a in i:
                            if a != []:
                                canvas.delete(a[1])
                                canvas.delete(a[2])
                    canvas.delete(yazı)
                    skor = 0
                    listekareisim = [[[],[],[],[]],
                         [[],[],[],[]],
                         [[],[],[],[]],
                         [[],[],[],[]]]
                    break
                if skor != eskiskor:
                    canvas.delete(yazı)
                    for y in range(0,4):
                        for x in range(0,4):
                            if listekareisim[y][x] != []:
                                if int(listekareisim[y][x][0].tip) > en_büyük_taş:
                                    en_büyük_taş = int(listekareisim[y][x][0].tip)
                                    canvas.delete(en_büyük)
                                    en_büyük = canvas.create_text(300,575,text=en_büyük_taş,fill="black",font=("italic", 30))
                    yazı = canvas.create_text(300,25,text=skor,fill="black",font=("italic", 30))
                    ge[len(ge)-1].fitness += (skor-eskiskor)*0.1
                    eskiskor = skor
                canvas.update()
def run(config_file):

    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    with open("bests.pkl", "rb") as f:
        genome = pickle.load(f)
    genomes = [(1,genome)]
    for i in range(500):
        winner = eval_genomes(genomes,config)
    
if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)
pencere.mainloop()
