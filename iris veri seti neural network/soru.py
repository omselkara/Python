import csvfile
import neat
import os
import pickle
def eval_genomes(genomes,config,sepal_l,sepal_w,petal_l,petal_w):
    global fitness
    nets = []
    ge = []
    for genome_id,genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome,config)
        nets.append(net)
        ge.append(genome)
    output = nets[0].activate((float(sepal_l),float(sepal_w),float(petal_l),float(petal_w)))
    if output[0] > 0.5:
        return "setosa"
    if output[1] > 0.5:
        return "versicolor"
    if output[2] > 0.5:
        return "virginica"
def run(config_file,s_l,s_w,p_l,p_w):
    """
    runs the NEAT algorithm to train a neural network to play flappy bird.
    :param config_file: location of config file
    :return: None
    """
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    p = neat.Population(config)

    #p.add_reporter(neat.StdOutReporter(True))
    #stats = neat.StatisticsReporter()
    #p.add_reporter(stats)
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_file)
    with open("bests.pkl", "rb") as f:
        genome = pickle.load(f)
    genomes = [(1,genome)]
    cevap = eval_genomes(genomes,config,s_l,s_w,p_l,p_w)
    return cevap
local_dir = os.path.dirname(__file__)
config_path = os.path.join(local_dir, 'config-feedforward.txt')
def bul(sepal_l,sepal_w,petal_l,petal_w):
    global config_path
    verilen = run(config_path,sepal_l,sepal_w,petal_l,petal_w)
    return verilen
