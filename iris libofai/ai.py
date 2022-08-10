import math
import random
from copy import deepcopy
import numpy as np
#Aktivasyon fonksiyonu
def sigmoid(x):
    return 1/(1+np.exp(-x))
class network:
    def __init__(self,ins,layers,outs,pop):
        #Neural network u oluşturma
        self.ins = deepcopy(ins)
        self.layers = deepcopy(layers)
        self.layers.append(1)
        self.outs = deepcopy(outs)
        self.genomes = []
        self.pop = deepcopy(pop)
        for out in range(self.outs):
            self.genomes.append([])
            for i in range(self.pop):
                self.genomes[out].append(genome(self.ins,self.layers))
    #Eğitme
    def train(self,inputs,outputs,epoch,until=0.1):
        for _ in range(epoch):
            for output in range(len(outputs)):
                losses = []
                for i in self.genomes[output]:
                    losses.append(i.calc_loss(inputs,outputs[output]))
                best = deepcopy(self.genomes[output][losses.index(min(losses))].get_clone())
                for index,i in enumerate(self.genomes[output]):
                    i.set_clone(best)
                    if index!=0:
                        i.mutate()
            toplam = 0
            for output in range(len(outputs)):
                toplam += self.genomes[output][0].calc_loss(inputs,outputs[output])
            if toplam <=until:
                break
            print("Epoch:"+str(_)+"\nLoss:"+str(int(toplam)+1))
    #Çıktı alma
    def activate(self,input1):
        output = []
        for out in range(len(self.genomes)):
            output.append(self.genomes[out][0].activate(input1))
        for index,i in enumerate(output):
            if i<0.5:
                output[index] = 0
            else:
                output[index] = 1
        return output
    #Network u kaydetme
    def save(self,name="best.conf"):
        clone_of_bests = []
        for output in range(len(self.genomes)):
            clone_of_bests.append(self.genomes[output][0].get_clone())
        dosya = open(name,"w",encoding="utf-8")
        dosya.write(str(clone_of_bests))
        dosya.close()
    #Networku yükleme
    def load(self,name="best.conf"):
        dosya = open(name,"r")
        clone = eval(dosya.readline())
        dosya.close()
        for output in range(len(clone)):
            self.genomes[output][0].set_clone(clone[output])
#Network içinde bulunan öğrenen yapay zeka
class genome:
    def __init__(self,ins,layers):
        self.ins = deepcopy(ins)
        self.layers = deepcopy(layers)
        self.neurons = []
        self.biasses = []
        last = self.ins
        for i in self.layers:
            self.neurons.append([])
            self.biasses.append(bias())
            for a in range(i):
                self.neurons[-1].append(neuron(last))
            last = i
    #Çıktı alma
    def activate(self,ins):
        gelen = deepcopy(ins)
        for layer in range(len(self.neurons)):
            yeni = []
            for neur in range(len(self.neurons[layer])):
                yeni.append(self.neurons[layer][neur].activate(gelen,self.biasses[layer].biass))
            gelen = deepcopy(yeni)

        return gelen[0]
    #Klonlama
    def get_clone(self):
        clone_conn = []
        clone_bias = []
        for layer in range(len(self.neurons)):
            clone_bias.append(self.biasses[layer].biass)
            clone_conn.append([])
            for neur in range(len(self.neurons[layer])):
                clone_conn[layer].append(self.neurons[layer][neur].get_clone())
        return [clone_conn,clone_bias]
    #Klonlama
    def set_clone(self,clones):
        clone_conn = deepcopy(clones[0])
        clone_bias = deepcopy(clones[1])
        for layer in range(len(self.neurons)):
            self.biasses[layer].biass = clone_bias[layer]
            for neur in range(len(self.neurons[layer])):
                self.neurons[layer][neur].set_clone(clone_conn[layer][neur])
    #Kayıp hesaplama
    def calc_loss(self,ins,outs):
        loss = 0
        for i in range(len(ins)):
            loss += abs(outs[i]-self.activate(ins[i]))
        return loss
    #Ağılıkları değişme
    def mutate(self):
        for layer in range(len(self.neurons)):
            self.biasses[layer].mutate()
            for neur in range(len(self.neurons[layer])):
                self.neurons[layer][neur].mutate()
                
class neuron:
    def __init__(self,connlen):
        self.connlen = deepcopy(connlen)
        self.conns = []
        for i in range(self.connlen):
            self.conns.append(conn())
    def activate(self,ins,biass):
        toplam = 0
        toplam += biass
        for i in range(self.connlen):
            toplam += self.conns[i].activate(ins[i])
        return sigmoid(toplam)
    def get_clone(self):
        weights = []
        for i in self.conns:
            weights.append(i.weight)
        return weights
    def set_clone(self,weights):
        for index,i in enumerate(self.conns):
            i.weight = weights[index]
    def mutate(self):
        for i in self.conns:
            i.mutate()
#Weight
class conn():
    def __init__(self):
        self.weight = random.uniform(-30,30)
    def activate(self,input1):
        return self.weight*input1
    def mutate(self):
        if random.randint(1,100)==1:
            self.weight = random.uniform(-30,30)
        elif random.randint(1,100)==1:
            self.weight = 0
        elif random.randint(1,100)==1:
            self.weight += random.uniform(-1,1)

class bias():
    def __init__(self):
        self.biass = random.uniform(-30,30)
    def mutate(self):
        if random.randint(1,100)==1:
            self.biass = random.uniform(-30,30)
        elif random.randint(1,100)==1:
            self.biass = 0
        elif random.randint(1,100)==1:
            self.biass += random.uniform(-1,1)
            

