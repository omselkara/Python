from tkinter import *
from tkinter import messagebox
import keyboard,os,neat,pickle
import time,random
from math import cos,sin,radians
pencere = Tk()
pencere.title("Ping Pong ai")
canvas = Canvas(width=600,height=400,highlightthickness=0,bg="black")
canvas.pack()
def eval_genomes(genomes,config):
    ge = []
    nets = []
    for genome_id,genome in genomes:
        genome.fitness = 0
        net = neat.nn.recurrent.RecurrentNetwork.create(genome,config)
        nets.append(net)
        ge.append(genome)
        xtop = 300
        ytop = 200
        derece = 1
        top = canvas.create_oval(xtop-10,ytop-10,xtop+10,ytop+10,fill="white",width=0)
        xkendi = 40
        ykendi = 200
        oyuncu = canvas.create_rectangle(xkendi-15,ykendi-50,xkendi+15,ykendi+50,fill="white",width=0)
        xrakip = 560
        yrakip = 200
        rakip = canvas.create_rectangle(xrakip-15,yrakip-50,xrakip+15,yrakip+50,fill="white",width=0)
        an = time.time()
        yaptepe = 0
        yapaşağı = 0
        canvas.update()
        keyboard.wait("w")
        while 1:
            if time.time()-an >= 1/30:
                if int(xtop-10) == xkendi+15 and ytop > ykendi-50 and ytop < ykendi +50:
                    derece = (random.randint(110,250))
                if int(xtop+10) == xrakip-15 and ytop > yrakip-50 and ytop < yrakip+50:
                    derece = (random.randint(1,359))
                    while (derece > 70 and derece < 290):
                        derece = (random.randint(1,359))
                if ytop-10 < 0 and yaptepe == 0:
                    yaptepe = 1
                    derece = 360-derece
                elif yaptepe != 0:
                    yaptepe = 0
                if ytop+10 >= 400 and yapaşağı == 0:
                    yapaşağı = 1
                    derece = 360-derece
                elif yapaşağı != 0:
                    yapaşağı = 0
                x = (xtop-(10*cos(radians(derece))+xtop))*0.009
                y = (ytop-(10*sin(radians(derece))+ytop))*0.009
                xtop += x
                ytop += y
                canvas.move(top,x,y)
                if (keyboard.is_pressed("w") and keyboard.is_pressed("W")) and ykendi-50 >=0:
                    ykendi -= 0.1
                    canvas.move(oyuncu,0,-0.1)
                if (keyboard.is_pressed("s") and keyboard.is_pressed("S")) and ykendi+50 <= 400:
                    ykendi += 0.1
                    canvas.move(oyuncu,0,0.1)
                output = nets[len(nets)-1].activate((ytop,yrakip))
                if derece >= 90 and derece <= 270:
                    if output[0] > 0.5 and yrakip-50 >= 0:
                        yrakip -= 0.2
                        canvas.move(rakip,0,-0.2)
                    if output[1] > 0.5 and yrakip+50 <= 400:
                        yrakip += 0.2
                        canvas.move(rakip,0,0.2)
                if xtop-10 <= 0:
                    messagebox.showerror("Kaybettin","Kaybettin")
                    break
                if xtop+10 >= 600:
                    messagebox.showerror("Kazandın","Kazandın")
                    break
                canvas.update()
        canvas.delete(rakip,oyuncu,top)
def run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    #p.add_reporter(neat.StdOutReporter(True))
    #stats = neat.StatisticsReporter()
    #p.add_reporter(stats)
    #config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_file)
    with open("bests.pkl", "rb") as f:
        genome = pickle.load(f)
    genomes = [(1,genome)]
    while 1:
        eval_genomes(genomes,config)
local_dir = os.path.dirname(__file__)
config_path = os.path.join(local_dir, 'config-feedforward.txt')
run(config_path)
pencere.mainloop()
