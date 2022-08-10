from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import winsound
import time,os,neat,pickle
def keya(event):
    global öl,derece,yedekoyuncuresim,oyuncuresim,oyuncu,oyuncux,oyuncuy,basma,oyuncuxyer,oyuncuyyer,harita,listeisim,bomba1resim,bomba2resim,bomba3resim,bomba5resim,bomba6resim,bomba7resim,bomba8resim,bomba9resim,bomba10resim,skor,yazı,listeyoket
    yapma = 0
    ışınlanma = 0
    if (event == "s" or event == "S" or event == "Down") and (not basma):
        basma = 1
        yapma = 1
        derece = 90
        oyuncuresim = ImageTk.PhotoImage(yedekoyuncuresim.rotate(derece))
        canvas.delete(oyuncu)
        oyuncu = canvas.create_image(oyuncux,oyuncuy,image=oyuncuresim)
        for i in range(0,120):
            canvas.move(oyuncu,0,0.5)
            canvas.update()
            oyuncuy += 0.5
            if oyuncuy == 569+30:
                canvas.move(oyuncu,0,179-599)
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
        oyuncuresim = ImageTk.PhotoImage(yedekoyuncuresim.rotate(derece))
        canvas.delete(oyuncu)
        oyuncu = canvas.create_image(oyuncux,oyuncuy,image=oyuncuresim)
        for i in range(0,120):
            canvas.move(oyuncu,0,-0.5)
            canvas.update()
            oyuncuy -= 0.5
            if oyuncuy == 179:
                canvas.move(oyuncu,0,599-179)
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
        oyuncuresim = ImageTk.PhotoImage(yedekoyuncuresim.rotate(derece))
        canvas.delete(oyuncu)
        oyuncu = canvas.create_image(oyuncux,oyuncuy,image=oyuncuresim)
        for i in range(0,120):
            canvas.move(oyuncu,0.5,0)
            canvas.update()
            oyuncux += 0.5
            if oyuncux == 899:
                oyuncux = 509-30
                canvas.move(oyuncu,509-30-899,0)
                harita[oyuncuyyer][oyuncuxyer] = 0
                ışınlanma = 1
                oyuncuxyer = -1
        oyuncuxyer += 1
        basma = 0
    if (event == "a" or event == "A" or event == "Left") and (not basma):
        basma = 1
        yapma = 1
        derece = 0
        oyuncuresim = ImageTk.PhotoImage(yedekoyuncuresim.rotate(derece))
        canvas.delete(oyuncu)
        oyuncu = canvas.create_image(oyuncux,oyuncuy,image=oyuncuresim)
        for i in range(0,120):
            canvas.move(oyuncu,-0.5,0)
            canvas.update()
            oyuncux -= 0.5
            if oyuncux == 509-30:
                oyuncux = 899
                canvas.move(oyuncu,899-479,0)
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
                    canvas.delete(yazı) 
                    skor += i[0].sayı
                    yazı = canvas.create_text(851,34,text=skor,font=("italic",30))
                    canvas.delete(i[1])
                    harita[i[0].y][i[0].x] = 0
                    listeisim.remove(i)
                    canvas.update()
                else:
                    canvas.delete(i[1])
                    x = i[0].x
                    y = i[0].y
                    exec("i[1] = canvas.create_image(480+x*56+x*4+29,180+y*56+y*4+29,image=bomba{}resim)".format(i[0].sayı))
                    harita[y][x] = i[0].sayı                    
        for a in listeölü:
            i = a
            canvas.delete(i[1])
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
            canvas.update()
        ihtimal = random.randint(0,3)
        if ihtimal == 1:
            seç = []
            for y in range(0,7):
                for x in range(0,7):
                    if harita[y][x] == 0:
                        seç.append([y,x])
            a = random.randint(0,len(seç)-1)
            bomba_oluştur(seç[a][1],seç[a][0])
    canvas.update()
class patlama:
    def __init__(self,x):
        self.süre = 0
        self.x = x
def patlat(x,y):
    global listeyoket,patlamasayı
    exec("patlama{}isim = patlama(x)".format(patlamasayı))
    exec("patlama{} = canvas.create_rectangle(480+56*x+x*4,180+56*y+y*4,480+56*x+x*4+56,180+56*y+y*4+56,fill='#%02x%02x%02x'%(200,0,0))".format(patlamasayı))
    exec("listeyoket.append([patlama{}isim,patlama{}])".format(patlamasayı,patlamasayı))
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
    exec("bomba{} = canvas.create_image(480+x*56+x*4+29,180+y*56+y*4+29,image=isaretresim)".format(sayı))
    exec("listeisim.append([bomba{}isim,bomba{}])".format(sayı,sayı))
    sayı += 1
    harita[y][x] = 11
pencere = Tk()
canvas = Canvas(pencere,width=1366,height=768,bg="#%02x%02x%02x"%(198,182,182),highlightthickness=0)
canvas.pack()
yedekoyuncuresim = Image.open("resimler\oyuncu.png")
oyuncuresim = ImageTk.PhotoImage(yedekoyuncuresim.rotate(90))
haritaresim = ImageTk.PhotoImage(Image.open("resimler\\harita.png"))
isaretresim = ImageTk.PhotoImage(Image.open("resimler\\isaret.png"))
bomba1resim = ImageTk.PhotoImage(Image.open("resimler\\a1.png"))
bomba2resim = ImageTk.PhotoImage(Image.open("resimler\\a2.png"))
bomba3resim = ImageTk.PhotoImage(Image.open("resimler\\a3.png"))
bomba4resim = ImageTk.PhotoImage(Image.open("resimler\\a4.png"))
bomba5resim = ImageTk.PhotoImage(Image.open("resimler\\a5.png"))
bomba6resim = ImageTk.PhotoImage(Image.open("resimler\\a6.png"))
bomba7resim = ImageTk.PhotoImage(Image.open("resimler\\a7.png"))
bomba8resim = ImageTk.PhotoImage(Image.open("resimler\\a8.png"))
bomba9resim = ImageTk.PhotoImage(Image.open("resimler\\a9.png"))
bomba10resim = ImageTk.PhotoImage(Image.open("resimler\\a10.png"))
canvas.create_image(1366/2,768/2,image=haritaresim)
pencere.attributes("-fullscreen",1)
canvas.create_rectangle(688-208,388-208,688+208,388+208)
harita = []
for y in range(0,7):
    for x in range(0,7):
        canvas.create_rectangle(480+56*x+x*4,180+56*y+y*4,480+56*x+x*4+56,180+56*y+y*4+56,fill="#%02x%02x%02x"%(144,129,129))
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
    global oyuncu,yazı,harita,yap,öl,derece,yedekoyuncuresim,oyuncuresim,oyuncu,oyuncux,oyuncuy,basma,oyuncuxyer,oyuncuyyer,harita,listeisim,bomba1resim,bomba2resim,bomba3resim,bomba5resim,bomba6resim,bomba7resim,bomba8resim,bomba9resim,bomba10resim,skor,yazı,listeyoket
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
        yazı = canvas.create_text(851,34,text=skor,font=("italic",30))
        oyuncu = canvas.create_image(oyuncux,oyuncuy,image=oyuncuresim)
        harita[oyuncuyyer][oyuncuxyer] = -1
        #pencere.bind("<Key>",lambda event:keya(event.keysym))
        an = time.time()
        çık = 0
        while not çık:
            if çık == 1:
                break
            while basma == 0:
                for index,i in enumerate(listeyoket):
                    listeyoket[index][0].süre += 1
                    if i[0].süre >= 1:
                        canvas.delete(i[1])
                        listeyoket.remove(i)
                liste = []
                for asd in harita:
                    for asdf in asd:
                        liste.append(asdf)
                liste.append(oyuncuxyer)
                liste.append(oyuncuyyer)
                output = nets[0].activate(liste)
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
                if öl == 1:
                    for i in listeisim:
                        canvas.delete(i[1])
                    for i in listeyoket:
                        canvas.delete(i[1])
                    canvas.delete(oyuncu)
                    canvas.delete(yazı)
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
pencere.mainloop()
