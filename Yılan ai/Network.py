from Genome import Genome
from Selector import calc_probability,select
import random
import numpy as np

class Network:
    def __init__(self,input,hidden,output,pop):
        self.input = input
        self.hidden = hidden
        self.output = output
        self.pop = pop
        self.genereation = 0
        self.genomes = [Genome(self.input,self.hidden,self.output) for i in range(self.pop)]

    def select(self,show_best=True):
        probs = calc_probability(self.genomes)
        newgenomes = []
        best = self.genomes[0]
        for i in range(self.pop):
            gen = self.genomes[i]
            if (gen.score>best.score or (gen.score==best.score and random.uniform(0,1)<0.25)):
                best = gen
            index = select(probs)
            parent1 = self.genomes[index]
            index = select(probs)
            parent2 = self.genomes[index]
            newgenome = parent1.generate_baby(parent2)
            newgenome.mutate()
            newgenomes.append(newgenome)
        if show_best:
            print(f"Generation:{self.genereation}   Best Score:{best.score}   Schema:{best.get_schema()}")
        self.genereation += 1
        best.score = 0
        newgenomes[0] = best
        self.genomes = newgenomes
        return best
    
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
