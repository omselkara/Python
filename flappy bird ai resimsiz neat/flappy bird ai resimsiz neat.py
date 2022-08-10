from tkinter import *
import os
import neat
import time
import random
kuş_sıra = 0
birds = []
class kuşş():
    def __init__(self):
        self.x = 100
        self.y = 250
        self.zıpla = 0
        self.düş = 0
def kuş_oluştur():
    global kuş_sıra,birds,canvas
    exec("kuş{}isim = kuşş()".format(kuş_sıra))
    exec("kuş{} = canvas.create_oval(100,250,120,270,fill='yellow',width=3)".format(kuş_sıra))
    exec("birds.append([kuş{}isim,kuş{}])".format(kuş_sıra,kuş_sıra))
    kuş_sıra += 1
class pipe():
    def __init__(self):
        self.x = 550
        self.y = 0
        self.geri = 0
def pipe_oluştur(y):
    global pipes,sıra,canvas
    exec("pipe{}isim = pipe()".format(sıra))
    exec("pipe{}isim.y = {}".format(sıra,y))
    exec("pipe{}1 = canvas.create_rectangle({},0,{}+50,{}-75,fill='green')".format(sıra,550,550,y))
    exec("pipe{}2 = canvas.create_rectangle({},600,{}+50,{}+75,fill='green')".format(sıra,550,550,y))
    exec("pipes.append([pipe{}isim,pipe{}1,pipe{}2])".format(sıra,sıra,sıra))
    sıra += 1
def eval_genomes(genomes,config):
    global zıpla,sıra,pipes,canvas,birds
    kuş_sıra = 0
    birds = []
    zıpla = 0
    skor = 0
    düş = 0
    sıra = 0
    pipes = []
    pipe_sıra = 0
    pencere = Tk()
    pencere.geometry("+400+0")
    canvas = Canvas(width=500,height=600,bg="cyan")
    canvas.pack()
    yazı = canvas.create_text(240,50,text=skor,font=("italic",18),fill="white")
    a = time.time()
    #pencere.bind("<Key>",lambda a : keya(a.keysym))
    süre = time.time()
    öl = 50
    nets = []
    ge = []
    for genome_id, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        ge.append(genome)
        kuş_oluştur()
    pipe_oluştur(random.randint(100,500))
    süre = time.time()
    yap = 1
    while öl != 0:
        if time.time()-a >= 1/60:
            canvas.delete(yazı)
            yazı = canvas.create_text(240,50,text=skor,font=("italic",18),fill="white")
            if time.time()-süre > 3:
                süre = time.time()
                pipe_oluştur(random.randint(100,500))
            if len(pipes) > 0:
                for i in pipes:
                    i[0].x -= 4
                    canvas.move(i[1],-4,0)
                    canvas.move(i[2],-4,0)
                    if i[0].x < -50:
                        canvas.delete(i)
                        pipes.remove(i)
                        pipe_sıra -= 1
                    if pipes[pipe_sıra][0].x+81 < 100:
                        pipe_sıra += 1
                        skor += 1
                        for i in birds:
                            if skor < 100:
                                ge[birds.index(i)].fitness += 5
            for bird in birds:
                if skor < 100:
                    ge[birds.index(bird)].fitness += 0.1
                output = nets[birds.index(bird)].activate((bird[0].y, abs(bird[0].y - (pipes[pipe_sıra][0].y-75)), abs(bird[0].y - (pipes[pipe_sıra][0].y+75))))
                if output[0] > 0.5:
                    bird[0].zıpla = 80
                if bird[0].zıpla == 0:
                    if bird[0].düş <= 8:
                        bird[0].düş += 0.5
                    bird[0].y += bird[0].düş
                    canvas.move(bird[1],0,bird[0].düş)
                else:
                    bird[0].düş = 0
                    bird[0].y -= 10
                    canvas.move(bird[1],0,-10)
                    bird[0].zıpla -= 10
                if len(pipes) > 0:
                    for i in pipes:
                        if bird[0].x+20 >= i[0].x and bird[0].x <= i[0].x+50 and bird[0].y >= i[0].y+75:
                            ge[birds.index(bird)].fitness -= 5
                            nets.pop(birds.index(bird))
                            ge.pop(birds.index(bird))
                            birds.pop(birds.index(bird))
                            canvas.delete(bird[1])
                            öl -= 1
                        if bird[0].x+20 >= i[0].x and bird[0].x <= i[0].x+50 and bird[0].y <= i[0].y-75:
                            ge[birds.index(bird)].fitness -= 5
                            nets.pop(birds.index(bird))
                            ge.pop(birds.index(bird))
                            birds.pop(birds.index(bird))
                            canvas.delete(bird[1])
                            öl -= 1
                if bird[0].y >= 650 or bird[0].y < -10:
                    ge[birds.index(bird)].fitness -= 5
                    nets.pop(birds.index(bird))
                    ge.pop(birds.index(bird))
                    birds.pop(birds.index(bird))
                    canvas.delete(bird[1])
                    öl -= 1
            try:
                canvas.update()
            except:
                pass
            a = time.time()
    pencere.destroy()
    pencere.mainloop()
def run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    
    winner = p.run(eval_genomes, 50)
    
if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)
