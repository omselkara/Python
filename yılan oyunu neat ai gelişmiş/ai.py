from tkinter import *
import time,random,neat,os,pickle
from tkinter import messagebox
def renk_belirle(rgb):
    return '#%02x%02x%02x' % rgb
pencere = Tk()
canvas = Canvas(pencere,width=1366,height=768,bg="black",highlightthickness=0)
canvas.pack()
pencere.attributes("-fullscreen",1)
xkafayer = 1
ykafayer = 0
öl = 0
an = time.time()
meyve = 0
meyveboşluk = 0
listeisim = []
sayı = 0
harita = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
harita[ykafayer][xkafayer] = -1
canvas.create_rectangle(7,8,1359,760,outline="gray",fill="black")
xkafa = 8+1*50
yön = "sağ"
ykafa = 9+0*50
def keya(event):
    global yön,xkafa,ykafa,listeisim
    if event == "d" and yön != "sol":
        yön = "sağ"
        for a in listeisim:
            a[0].yapılacak.append([xkafa,ykafa,yön])
    if event == "a" and yön != "sağ":
        yön = "sol"
        for a in listeisim:
            a[0].yapılacak.append([xkafa,ykafa,yön])
    if event == "w" and yön != "aşağı":
        yön = "yukarı"
        for a in listeisim:
            a[0].yapılacak.append([xkafa,ykafa,yön])
    if event == "s" and yön != "yukarı":
        yön = "aşağı"
        for a in listeisim:
            a[0].yapılacak.append([xkafa,ykafa,yön])
#pencere.bind("<Key>", lambda event:keya(event.keysym))
class meyves:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.haritayerx = int((x-8)/50)
        self.haritayery = int((y-9)/50)
def meyve_oluştur():
    global meyve,meyveboşluk,sayı,meyveisim,harita
    canvas.delete(meyve)
    canvas.delete(meyveboşluk)
    liste = []
    for y in range(0,27):
        for x in range(0,15):
            if harita[x][y] == 0:
                liste.append([y*50+8,x*50+9])
    seçilen = random.randint(0,len(liste)-1)
    x = liste[seçilen][0]
    y = liste[seçilen][1]
    points = [[x+20,y+20],[x+20,y+5],[x+30,y+5],[x+30,y+20],[x+45,y+20],[x+45,y+30],[x+30,y+30],[x+30,y+45],[x+20,y+45],[x+20,y+30],[x+5,y+30],[x+5,y+20],[x+20,y+20]]
    harita[int((y-9)/50)][int((x-8)/50)] = 100
    meyveisim = meyves(x,y)
    meyve = canvas.create_polygon(points,fill=renk_belirle((0,100,0)))
    meyveboşluk = canvas.create_rectangle(x+21,y+21,x+29,y+29,fill=renk_belirle((0,0,0)))
    
def meyve_yendi():
    if listeisim[-1][0].yön == "sağ":
        yılan_oluştur(listeisim[-1][0].x-50,listeisim[-1][0].y,listeisim[-1][0].yön)
    if listeisim[-1][0].yön == "sol":
        yılan_oluştur(listeisim[-1][0].x+50,listeisim[-1][0].y,listeisim[-1][0].yön)
    if listeisim[-1][0].yön == "yukarı":
        yılan_oluştur(listeisim[-1][0].x,listeisim[-1][0].y+50,listeisim[-1][0].yön)
    if listeisim[-1][0].yön == "aşağı":
        yılan_oluştur(listeisim[-1][0].x,listeisim[-1][0].y-50,listeisim[-1][0].yön)
    meyve_oluştur()
class yılan:
    def __init__(self,x,y,yön):
        self.x = x
        self.y = y
        self.haritayerx = int((x-8)/50)
        self.haritayery = int((y-9)/50)
        self.yön = yön
        self.yapılacak = []
        if len(listeisim) > 0:
            for i in listeisim[-1][0].yapılacak:
                self.yapılacak.append(i)
def yılan_oluştur(x,y,yön):
    global sayı,listeisim,harita
    harita[int((y-9)/50)][int((x-8)/50)] = -100
    exec("yılan{}isim = yılan(x,y,yön)".format(sayı))
    if yön == "sağ":
        exec("yılan{} = canvas.create_rectangle(x,y+2,x+50,y+48,fill=renk_belirle((0,200,0)),width=0)".format(sayı))
    if yön == "sol":
        exec("yılan{} = canvas.create_rectangle(x,y+2,x+50,y+48,fill=renk_belirle((0,200,0)),width=0)".format(sayı))
    if yön == "aşağı":
        exec("yılan{} = canvas.create_rectangle(x+2,y,x+48,y,fill=renk_belirle((0,200,0)),width=0)".format(sayı))
    if yön == "yukarı":
        exec("yılan{} = canvas.create_rectangle(x+2,y,x+48,y,fill=renk_belirle((0,200,0)),width=0)".format(sayı))
    exec("listeisim.append([yılan{}isim,yılan{}])".format(sayı,sayı))
    sayı += 1
def func(y,x):
    global harita
    if harita[y][x] == 100:
        return 1
    if harita[y][x] == -100:
        return -1
    if harita[y][x] == 0:
        return 0
def eval_genomes(genomes,config):
    global xkafayer,ykafayer,öl,an,meyve,meyveboşluk,listeisim,sayı,harita,xkafa,ykafa,oyuncu,yön
    ge = []
    nets = []
    for genome_id,genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        ge.append(genome)
        xkafayer = 1
        ykafayer = 0
        öl = 0
        an = time.time()
        meyve = 0
        meyveboşluk = 0
        listeisim = []
        sayı = 0
        harita = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        harita[ykafayer][xkafayer] = -1
        canvas.create_rectangle(7,8,1359,760,outline="gray",fill="black")
        xkafa = 8+1*50
        yön = "sağ"
        ykafa = 9+0*50
        yılan_oluştur(xkafa-50,ykafa,"sağ")
        oyuncu = canvas.create_rectangle(xkafa,ykafa,xkafa+50,ykafa+50,fill=renk_belirle((0,200,0)),width=0)
        meyve_oluştur()
        while 1:
            if time.time()-an >= 1/7.5:
                an = time.time()
                if meyveisim.x == xkafa and meyveisim.y == ykafa:
                    meyve_yendi()
                liste = [[-1,-1,-1,-1,-1],
                         [-1,-1,-1,-1,-1],
                         [-1,-1, 0,-1,-1],
                         [-1,-1,-1,-1,-1],
                         [-1,-1,-1,-1,-1]]
                for y in range(ykafayer-2,ykafayer+3):
                    for x in range(xkafayer-2,xkafayer+3):
                        hata = 0
                        if y < 0:
                            hata = 1
                            asdf = -100
                        if y > 14:
                            hata = 1
                            asdf = -100
                        if x < 0:
                            hata = 1
                            asdf = -100
                        if x > 26:
                            hata = 1
                            asdf = -100
                        if not hata:
                            if harita[y][x] == -100:
                                if (y == ykafayer and x == xkafayer):
                                    asdf = 0
                                else:
                                    asdf = -100
                            if harita[y][x] == 100:
                                asdf = 100
                            if harita[y][x] == 0:
                                asdf = 0
                            if harita[y][x] == -1:
                                asdf = 0
                        y2 = y-(ykafayer-2)
                        x2 = x-(xkafayer-2)
                        liste[y2][x2] = asdf
                liste2 = []
                for a in liste:
                    for i in a:
                        liste2.append(i)
                liste2.append(meyveisim.x-xkafa)
                liste2.append(meyveisim.y-ykafa)
                output = nets[-1].activate(liste2)
                if output[0] > 0.5:
                    if yön == "sağ":
                        if not liste[1][2]:
                            keya("w")
                        if not liste[3][2]:
                            keya("s")
                    else:
                        keya("a")
                elif output[1] > 0.5:
                    if yön == "sol":
                        if not liste[1][2]:
                            keya("w")
                        if not liste[3][2]:
                            keya("s")
                    else:
                        keya("d")
                elif output[2] > 0.5:
                    if yön == "yukarı":
                        if not liste[2][1]:
                            keya("a")
                        if not liste[2][3] == -1:
                            keya("d")
                    else:
                        keya("s")
                elif output[3] > 0.5:
                    if yön == "aşağı":
                        if not liste[2][1]:
                            keya("a")
                        if not liste[2][3] == -1:
                            keya("d")
                    else:
                        keya("w")
                canvas.delete(oyuncu)
                harita[ykafayer][xkafayer] = 0
                if yön == "sağ":
                    oyuncu = canvas.create_rectangle(xkafa,ykafa+2,xkafa+50,ykafa+48,fill=renk_belirle((0,200,0)),width=0)
                    xkafayer += 1
                    xkafa += 50
                    canvas.move(oyuncu,50,0)
                if yön == "aşağı":
                    oyuncu = canvas.create_rectangle(xkafa+2,ykafa,xkafa+48,ykafa+50,fill=renk_belirle((0,200,0)),width=0)
                    ykafa += 50
                    ykafayer += 1
                    canvas.move(oyuncu,0,50)
                if yön == "sol":
                    oyuncu = canvas.create_rectangle(xkafa,ykafa+2,xkafa+50,ykafa+48,fill=renk_belirle((0,200,0)),width=0)
                    xkafa -= 50
                    xkafayer -= 1
                    canvas.move(oyuncu,-50,0)
                if yön == "yukarı":
                    oyuncu = canvas.create_rectangle(xkafa+2,ykafa,xkafa+48,ykafa+50,fill=renk_belirle((0,200,0)),width=0)
                    ykafayer -= 1
                    ykafa -= 50
                    canvas.move(oyuncu,0,-50)
                if xkafayer < 0 or xkafayer > 26 or ykafayer < 0 or ykafayer > 14:
                    öl = 1
                for a in listeisim:
                    if a[0].haritayerx == xkafayer and a[0].haritayery == ykafayer:
                        öl = 1
                        break
                if öl == 1:
                    canvas.delete(ALL)
                    #messagebox.showerror("öldün","öldün")
                    break
                else:
                    harita[ykafayer][xkafayer] = -1
                for a in listeisim:
                    harita[a[0].haritayery][a[0].haritayerx] = 0
                    if len(a[0].yapılacak) > 0 and a[0].yapılacak[0][0] == a[0].x and a[0].yapılacak[0][1] == a[0].y:
                        a[0].yön = a[0].yapılacak[0][2]
                        a[0].yapılacak.remove(a[0].yapılacak[0])
                    if a[0].yön == "sağ":
                        a[0].haritayerx += 1
                        x1 = 0
                        x2 = 2
                        y1 = 2
                        y2 = 0
                        canvas.delete(a[1])
                        if len(a[0].yapılacak)>0 and a[0].yapılacak[0][0] == a[0].x+50 and a[0].yapılacak[0][1] == a[0].y:
                            if a[0].yapılacak[0][2] == "yukarı":
                                if len(listeisim) > 1:
                                    x1 = 0
                                    x2 = 0
                                    y1 = 0
                                    y2 = 0
                                else:
                                    x1 = 2
                                    x2 = 0
                                    y1 = 0
                                    y2 = 0
                            if a[0].yapılacak[0][2] == "aşağı":
                                if len(listeisim) > 1:
                                    x1 = 0
                                    x2 = 0
                                    y1 = 2
                                    y2 = 2
                                else:
                                    x1 = 2
                                    x2 = 0
                                    y1 = 2
                                    y2 = 2
                        exec("a[1] = canvas.create_rectangle(a[0].x+x1,a[0].y+y1,a[0].x+48+x2,a[0].y+48+y2,fill=renk_belirle((0,200,0)),width=0)")
                        a[0].x += 50
                        canvas.move(a[1],50,0)
                    if a[0].yön == "sol":
                        a[0].haritayerx -= 1
                        x1 = 0
                        x2 = 2
                        y1 = 2
                        y2 = 0
                        canvas.delete(a[1])
                        if len(a[0].yapılacak)>0 and a[0].yapılacak[0][0] == a[0].x-50 and a[0].yapılacak[0][1] == a[0].y:
                            if a[0].yapılacak[0][2] == "yukarı":
                                if len(listeisim) > 1:
                                    x1 = 2
                                    x2 = 2
                                    y1 = 0
                                    y2 = 0
                                else:
                                    x1 = 2
                                    x2 = 0
                                    y1 = 0
                                    y2 = 0
                            if a[0].yapılacak[0][2] == "aşağı":
                                if len(listeisim) > 1:
                                    x1 = 2
                                    x2 = 2
                                    y1 = 2
                                    y2 = 2
                                else:
                                    x1 = 2
                                    x2 = 0
                                    y1 = 2
                                    y2 = 2
                        exec("a[1] = canvas.create_rectangle(a[0].x+x1,a[0].y+y1,a[0].x+48+x2,a[0].y+48+y2,fill=renk_belirle((0,200,0)),width=0)")
                        a[0].x -= 50
                        canvas.move(a[1],-50,0)
                    if a[0].yön == "yukarı":
                        a[0].haritayery -= 1
                        x1 = 2
                        x2 = 0
                        y1 = 0
                        y2 = 2
                        canvas.delete(a[1])
                        if len(a[0].yapılacak)>0 and a[0].yapılacak[0][0] == a[0].x and a[0].yapılacak[0][1] == a[0].y-50:
                            if a[0].yapılacak[0][2] == "sol":
                                if len(listeisim) > 1:
                                    x1 = 0
                                    x2 = 0
                                    y1 = 2
                                    y2 = 2
                                else:
                                    x1 = 0
                                    x2 = 0
                                    y1 = 2
                                    y2 = 0
                            if a[0].yapılacak[0][2] == "sağ":
                                if len(listeisim) > 1:
                                    x1 = 2
                                    x2 = 2
                                    y1 = 2
                                    y2 = 2
                                else:
                                    x1 = 2
                                    x2 = 2
                                    y1 = 2
                                    y2 = 0
                        exec("a[1] = canvas.create_rectangle(a[0].x+x1,a[0].y+y1,a[0].x+48+x2,a[0].y+48+y2,fill=renk_belirle((0,200,0)),width=0)")
                        a[0].y -= 50
                        canvas.move(a[1],0,-50)
                    if a[0].yön == "aşağı":
                        a[0].haritayery += 1
                        x1 = 2
                        x2 = 0
                        y1 = 0
                        y2 = 2
                        canvas.delete(a[1])
                        if len(a[0].yapılacak)>0 and a[0].yapılacak[0][0] == a[0].x and a[0].yapılacak[0][1] == a[0].y+50:
                            if a[0].yapılacak[0][2] == "sol":
                                if len(listeisim) > 1:
                                    x1 = 0
                                    x2 = 0
                                    y1 = 0
                                    y2 = 0
                                else:
                                    x1 = 0
                                    x2 = 0
                                    y1 = 2
                                    y2 = 0
                            if a[0].yapılacak[0][2] == "sağ":
                                if len(listeisim) > 1:
                                    x1 = 2
                                    x2 = 2
                                    y1 = 0
                                    y2 = 0
                                else:
                                    x1 = 2
                                    x2 = 2
                                    y1 = 2
                                    y2 = 0
                        exec("a[1] = canvas.create_rectangle(a[0].x+x1,a[0].y+y1,a[0].x+48+x2,a[0].y+48+y2,fill=renk_belirle((0,200,0)),width=0)")
                        a[0].y += 50
                        canvas.move(a[1],0,50)
                    harita[a[0].haritayery][a[0].haritayerx] = -100
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
    while 1:
        winner = eval_genomes(genomes,config)
    
if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)
pencere.destroy()
pencere.mainloop()
