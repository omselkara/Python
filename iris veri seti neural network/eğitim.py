import csvfile
import neat
import os
import datetime
import pickle
#{'sepal_length': '5.1', 'sepal_width': '3.5', 'petal_length': '1.4', 'petal_width': '0.2', 'species': 'setosa'}
iris = csvfile.load("iris.csv")
def eval_genomes(genomes,config):
    nets = []
    ge = []
    for genome_id,genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome,config)
        nets.append(net)
        ge.append(genome)
    for genome in ge:
        for i in iris:
            hayır = 0
            output = nets[ge.index(genome)].activate((float(i["sepal_length"]),float(i["sepal_width"]),float(i["petal_length"]),float(i["petal_width"])))
            if output[0] > 0.5 and output[1] > 0.5:
                ge[ge.index(genome)].fitness -= 1
                hayır = 1
            if output[0] > 0.5 and output[2] > 0.5:
                ge[ge.index(genome)].fitness -= 1
                hayır = 1
            if output[1] > 0.5 and output[2] > 0.5:
                ge[ge.index(genome)].fitness -= 1
                hayır = 1
            if not hayır:
                if output[0] > 0.5:
                    if i["species"] == "setosa":
                        ge[ge.index(genome)].fitness += 5
                    else:
                        ge[ge.index(genome)].fitness -= 1
                if output[1] > 0.5:
                    if i["species"] == "versicolor":
                        ge[ge.index(genome)].fitness += 5
                    else:
                        ge[ge.index(genome)].fitness -= 1
                if output[2] > 0.5:
                    if i["species"] == "virginica":
                        ge[ge.index(genome)].fitness += 5
                    else:
                        ge[ge.index(genome)].fitness -= 1
def run(config_file):
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
    an = datetime.datetime.now()
    winner = p.run(eval_genomes, 5000)
    with open("bests.pkl", "wb") as f:
        pickle.dump(winner, f)
        f.close()
    an2 = datetime.datetime.now()
    print(an2-an," sürdü")
    a = input("")
    
if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)

