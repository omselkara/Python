from Genome import Genome
from Selector import calc_probability,select
import random

class Network:
    def __init__(self,schema,pop):
        self.schema = schema
        self.pop = pop
        self.genereation = 0
        self.genomes = [Genome(self.schema) for i in range(self.pop)]

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

