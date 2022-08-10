from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import winsound
import time
import neat,pickle,os
def keya(event):
    global öl,derece,yedekoyuncuresim,oyuncuresim,oyuncu,oyuncux,oyuncuy,basma,oyuncuxyer,oyuncuyyer,harita,listeisim,skor,yazı,listeyoket
    yapma = 0
    ışınlanma = 0
    if (event == "s" or event == "S" or event == "Down") and (not basma):
        basma = 1
        yapma = 1
        derece = 90
        for i in range(0,120):
            oyuncuy += 0.5
            if oyuncuy == 569+30:
                oyuncuy = 179
                harita[oyuncuyyer][oyuncuxyer] = 0
                oyuncuyyer = -1
                ışınlanma = 1
        oyuncuyyer += 1
        basma = 0
    if (event == "w" or event == "W" or event == "Up") and (not basma):
        basma = 1
        yapma = 1
        derece = -90
        for i in range(0,120):
            oyuncuy -= 0.5
            if oyuncuy == 179:
                oyuncuy = 599
                harita[oyuncuyyer][oyuncuxyer] = 0
                oyuncuyyer = 7
                ışınlanma = 1
        oyuncuyyer -= 1
        basma = 0
    if (event == "d" or event == "D" or event == "Right") and (not basma):
        basma = 1
        yapma = 1
        derece = 180
        for i in range(0,120):
            oyuncux += 0.5
            if oyuncux == 899:
                oyuncux = 509-30
                harita[oyuncuyyer][oyuncuxyer] = 0
                ışınlanma = 1
                oyuncuxyer = -1
        oyuncuxyer += 1
        basma = 0
    if (event == "a" or event == "A" or event == "Left") and (not basma):
        basma = 1
        yapma = 1
        derece = 0
        for i in range(0,120):
            oyuncux -= 0.5
            if oyuncux == 509-30:
                oyuncux = 899
                ışınlanma = 1
                harita[oyuncuyyer][oyuncuxyer] = 0
                oyuncuxyer = 7
        oyuncuxyer -= 1
        basma = 0
    if yapma == 1:
        listeölü = []
        for index,i in enumerate(listeisim):
            i[0].sayı -= 1
            if i[0].sayı == 0:
                listeölü.append(i)
            else:
                if i[0].x == oyuncuxyer and i[0].y == oyuncuyyer:
                    skor += i[0].sayı
                    harita[i[0].y][i[0].x] = 0
                    listeisim.remove(i)
                else:
                    x = i[0].x
                    y = i[0].y
                    harita[y][x] = i[0].sayı                    
        for a in listeölü:
            i = a
            patlat(i[0].x,i[0].y)
            if i[0].y > 0:
                patlat(i[0].x,i[0].y-1)
            if i[0].y < 6:
                patlat(i[0].x,i[0].y+1)
            if i[0].x > 0:
                patlat(i[0].x-1,i[0].y)
                if i[0].y > 0:
                    patlat(i[0].x-1,i[0].y-1)
                if i[0].y < 6:
                    patlat(i[0].x-1,i[0].y+1)
            if i[0].x < 6:
                patlat(i[0].x+1,i[0].y)
                if i[0].y > 0:
                    patlat(i[0].x+1,i[0].y-1)
                if i[0].y < 6:
                    patlat(i[0].x+1,i[0].y+1)
            if (oyuncuxyer >= i[0].x-1 and oyuncuxyer <= i[0].x+1) and (oyuncuyyer >= i[0].y-1 and oyuncuyyer <= i[0].y+1):
                öl = 1
                #messagebox.showerror("Öldün","Öldün")#ölme
            harita[i[0].y][i[0].x] = 0
            listeisim.remove(i)
        seç = []
        for y in range(0,7):
            for x in range(0,7):
                if harita[y][x] == 0:
                    seç.append([y,x])
        a = random.randint(0,len(seç)-1)
        bomba_oluştur(seç[a][1],seç[a][0])
class patlama:
    def __init__(self,x):
        self.süre = 0
        self.x = x
def patlat(x,y):
    global listeyoket,patlamasayı
    exec("patlama{}isim = patlama(x)".format(patlamasayı))
    exec("listeyoket.append([patlama{}isim])".format(patlamasayı))
    patlamasayı += 1
class bomba:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.sayı = 11
listeisim = []
sayı = 0
def bomba_oluştur(x,y):
    global listeisim,sayı,harita
    exec("bomba{}isim = bomba(x,y)".format(sayı))
    exec("listeisim.append([bomba{}isim])".format(sayı))
    sayı += 1
    harita[y][x] = 11
harita = []
for y in range(0,7):
    harita.append([])
    for x in range(0,7):
        harita[y].append(0)
derece = 90
basma = 0
öl = 0
skor = 0
listeyoket = []
patlamasayı = 0
oyuncux = 509
oyuncuy = 209
oyuncuyyer = 0
oyuncuxyer = 0
def eval_genomes(genomes,config):
    global harita,yap,öl,derece,oyuncux,oyuncuy,basma,oyuncuxyer,oyuncuyyer,harita,listeisim,skor,listeyoket
    ge = []
    nets = []
    for genome_id,genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        ge.append(genome)
        harita = []
        for y in range(0,7):
            harita.append([])
            for x in range(0,7):
                harita[y].append(0)
        derece = 90
        basma = 0
        öl = 0
        skor = 0
        listeyoket = []
        patlamasayı = 0
        oyuncux = 509
        oyuncuy = 209
        oyuncuyyer = 0
        oyuncuxyer = 0
        harita[oyuncuyyer][oyuncuxyer] = -1
        #pencere.bind("<Key>",lambda event:keya(event.keysym))
        an = time.time()
        çık = 0
        while not çık:
            if çık == 1:
                break
            while basma == 0:
                for index,i in enumerate(listeyoket):
                    listeyoket[index][0].süre += 0.5
                    if i[0].süre >= 1:
                        listeyoket.remove(i)
                liste = []
                eskiskor = skor
                for asd in harita:
                    for asdf in asd:
                        liste.append(asdf)
                liste.append(oyuncuxyer)
                liste.append(oyuncuyyer)
                output = nets[len(nets)-1].activate(liste)
                if output[0] <= 0.5 and output[1] <= 0.5 and output[2] <= 0.5 and output[3] <= 0.5:
                    öl = 1
                if output[0] > 0.5:
                    keya("w")
                while basma:
                    time.sleep(0.1)
                if output[1] > 0.5:
                    keya("s")
                while basma:
                    time.sleep(0.1)
                if output[2] > 0.5:
                    keya("d")
                while basma:
                    time.sleep(0.1)
                if output[3] > 0.5:
                    keya("a")
                if skor != eskiskor:
                    ge[len(ge)-1].fitness += skor-eskiskor
                #ge[len(ge)-1].fitness += 0.1
                if time.time()-an >= 1/100:
                    if öl == 1:
                        ge[len(ge)-1].fitness -= 5
                        yap = 1
                        çık = 1
                        listeisim = []
                        listeyoket = []
                        harita = []
                        for y in range(0,7):
                            harita.append([])
                        for x in range(0,7):
                            harita[y].append(0) 
                        break
                    an = time.time()
def run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    
    winner = p.run(eval_genomes, 500)
    with open("bests.pkl", "wb") as f:
        pickle.dump(winner, f)
        f.close()
    
if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)
