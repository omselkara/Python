import random
from math import tanh
class net:
    def __init__(self,input,output,pop):
        self.genomes = []
        self.input = input
        self.output = output
        self.sayı = pop+1
        for i in range(pop):
            exec(f"gen{i} = genome(input,output,{i})")
            exec(f"self.genomes.append(gen{i})")
    def newgenome(self,index):
        exec(f"gen{self.sayı} = genome(self.input,self.output,index)")
        exec(f"self.genomes[{index}] = gen{self.sayı}")
        self.sayı += 1
    def train(self,inputs,outputs,step):
        for i in range(0,len(self.genomes)):
            self.genomes[i].sayı = 1
            self.genomes[i].last = 0
            self.fitness = 0
        for _ in range(step):
            loses = []
            for i in range(0,len(self.genomes)):
                loss = 0
                for ad in range(len(inputs)):
                    output = self.genomes[i].output(inputs[ad])
                    for s in range(self.output):
                        loss += outputs[ad][s]-output[s]
                if loss>0:
                    if self.genomes[i].last == -1:
                        self.genomes[i].sayı = (self.genomes[i].sayı*3)/random.randint(4,6)
                    self.genomes[i].last = 1
                    for d in range(self.input):
                        self.genomes[i].cons[s][d].weigth += self.genomes[i].sayı
                        self.genomes[i].cons[s][d].bias += self.genomes[i].sayı
                if loss<0:
                    if self.genomes[i].last == 1:
                        self.genomes[i].sayı = (self.genomes[i].sayı*3)/random.randint(4,6)
                    self.genomes[i].last = -1
                    for d in range(self.input):
                        self.genomes[i].cons[s][d].weigth -= self.genomes[i].sayı
                        self.genomes[i].cons[s][d].bias -= self.genomes[i].sayı
                loses.append(loss)
        #print(loses)
    def kill(self):
        genomes = []
        while (len(genomes)!=len(self.genomes)):
            fitness = 10000000000
            yer = 0
            for i in self.genomes:
                if i.fitness < fitness:
                   yer = i.yer

            genomes.append(yer)
        for i in range(int(len(self.genomes)/10)):
            self.newgenome(genomes[i])
            
class genome:
    def __init__(self,input,output,yer):
        self.input = input
        self.outputs = output
        self.sayı = 1
        self.last = 0
        self.cons = []
        self.fitness = 0
        self.yer = yer
        for i in range(output):
            self.cons.append([])
            for a in range(input):
                exec(f"con{a} = con()")
                exec(f"self.cons[{i}].append(con{a})")
    def output(self,inputs):
        liste = []
        for i in range(self.outputs):
            sum = 0
            for a in range(self.input):
                sum += self.cons[i][a].out(inputs[a])
            liste.append(tanh(sum))
        return liste
class con:
    def __init__(self):
        self.weigth = random.uniform(-30,30)
        self.bias = random.uniform(-30,30)
    def out(self,sayı):
        return sayı*self.weigth+self.bias

