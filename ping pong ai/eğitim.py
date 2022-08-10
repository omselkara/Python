import os,neat,pickle,random,time
from math import cos,sin,radians
from tkinter import *
def eval_genomes(genomes,config):
    ge = []
    nets = []
    for genome_id,genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome,config)
        nets.append(net)
        ge.append(genome)
        derece = 1
        xkendi = 560
        ykendi = 200
        xtop = 300
        ytop = 200
        çık = 0
        yapaşağı = 0
        yaptepe = 0
        an = time.time()
        while not çık:
            if xtop <= 60:
                derece = (random.randint(110,250))
            if int(xtop+10) == xkendi-15 and ytop > ykendi-50 and ytop < ykendi+50:
                ge[len(ge)-1].fitness += 1
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
            if derece >= 90 and derece <= 270:
                output = nets[len(nets)-1].activate((ytop,ykendi))
                if output[0] > 0.5 and output[1] > 0.5:
                    ge[len(ge)-1].fitness -= 1
                    çık = 1
                if output[0] > 0.5 and ykendi-50 >= 0:
                    ykendi -= 0.1
                if output[1] > 0.5 and ykendi+50 <= 400:
                    ykendi += 0.1
            if xtop+10 >= 600:
                ge[len(ge)-1].fitness -= 1
                çık = 1   
def run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    winner = p.run(eval_genomes, 50)
    with open("bests.pkl", "wb") as f:
        pickle.dump(winner, f)
        f.close()
    
if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)
