from Genome import Genome
from Selector import calc_probability,select
import random
import numpy as np

class Network:
    def __init__(self,input,output,pop):
        self.input = input
        self.output = output
        self.pop = pop
        self.genereation = 0
        self.genomes = [Genome(self.input,self.output) for i in range(self.pop)]

    def select(self,show_best=True):
        probs = calc_probability(self.genomes)
        newgenomes = []
        average = 0
        bests = [self.genomes[0]]
        for gen in self.genomes:
            if gen.score>bests[0].score:
                bests = [gen]
            elif gen.score==bests[0].score:
                bests.append(gen)
            average += gen.score
        average = average/self.pop
        probs = calc_probability(self.genomes)
        for gen in self.genomes:
            if gen.score<average:
                parent1 = random.choice(bests)
            else:
                parent1 = gen
            index = select(probs)
            parent2 = self.genomes[index]
            baby = parent1.generate_baby(parent2)
            baby.mutate()
            newgenomes.append(baby)
        if show_best:
            print(f"Generation:{self.genereation}   Best Score:{bests[0].score}")
        self.genereation += 1
        bests[0].score = 0
        newgenomes[0] = bests[0]
        self.genomes = newgenomes
        return bests
    
    def save(self,name="save.npz"):
        schema = [self.genereation,[]]
        for gen in self.genomes:
            schema[1].append(gen.get_detailed_schema())
        schema = np.array(schema,dtype=object)
        file = open(name,"wb")
        np.save(file,schema,allow_pickle=True)
    
    def load(self,name="save.npz"):
        file = open(name,"rb")
        schema = np.load(file,allow_pickle=True)
        self.genereation = schema[0]
        for i in range(self.pop):
            print(f"Loading Genome:{i}")
            self.genomes[i].apply_detailed_schema(schema[1][i])
