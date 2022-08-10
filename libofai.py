from random import seed,random
from math import exp
from copy import deepcopy

class network:
    def __init__(self,inputs,layers,outputs):
        self.inputs = deepcopy(inputs)
        self.layers = deepcopy(layers)
        self.outputs = deepcopy(outputs)
        self.genomes = []
        for out in range(self.outputs):
            self.genomes.append(genome(self.inputs,self.layers))
    def train(self,inputs,outs,epoch,learning_rate=0.5):
        for _ in range(epoch):
            sumofloss = 0
            for out in range(self.outputs):
                sumofloss += self.genomes[out].train(inputs,outs[out],1,learning_rate)
            if _%(epoch/100)==0:
                print("Epoch:"+str(_)+"\nLoss:"+str(sumofloss))
    def activate(self,inputs,yüzde=0):
        outputs = []
        for out in range(self.outputs):
            outputs.append(self.genomes[out].feedforward(inputs)[0])
        outs = []
        for i in outputs:
            if not yüzde:
                if i<0.5:
                    a=0
                elif i>0.5:
                    a=1
                else:
                    a=0.5
            else:
                a = i
            outs.append(a)
        return outs
    def save(self,name="best.conf"):
        dosya = open(name,"w",encoding="utf-8")
        genomes = []
        for i in self.genomes:
            genomes.append(i.get_clone())
        dosya.write(str(genomes))
        dosya.close()
    def load(self,name="best.conf"):
        dosya = open(name,"r",encoding="utf-8")
        clone = eval(dosya.readline())
        for out in range(self.outputs):
            self.genomes[out].set_clone(clone[out])
class genome:
    def __init__(self,inputs,layers):
        self.inputs = deepcopy(inputs)
        self.layers = deepcopy(layers)
        self.layers.append(1)
        self.neurons = []
        last = self.inputs
        for layer in range(len(self.layers)):
            self.neurons.append([])
            for a in range(self.layers[layer]):
                neuron = []
                for i in range(last+1):
                    neuron.append(random())
                self.neurons[layer].append({})
                self.neurons[layer][a]["weights"] = neuron
            last = self.layers[layer]
    def activate(self,inputs,weights):
        toplam = weights[-1]
        for i in range(len(weights)-1):
            toplam += inputs[i]*weights[i]
        return toplam
    def sigmoid(self,a):
        return 1.0 / (1.0 + exp(-a))
    def sigmoid_derivative(self,output):
        return output*(1-output)
    def feedforward(self,inputs):
        gelenler = inputs
        for layer in range(len(self.neurons)):
            yeni = []
            for index,neuron in enumerate(self.neurons[layer]):
                out = self.sigmoid(self.activate(gelenler,neuron["weights"]))
                neuron["output"] = out
                yeni.append(out)
            gelenler = yeni
        return gelenler
    def backpropagation(self,out):
        for layer in reversed(range(len(self.neurons))):
            losses = []
            if layer!=len(self.neurons)-1:
                for i in range(len(self.neurons[layer])):
                    loss = 0
                    for neuron in self.neurons[layer+1]:
                        loss += neuron["weights"][i]*neuron["loss"]
                    losses.append(loss)
            else:
                for index,i in enumerate(self.neurons[layer]):
                    loss = out-i["output"]
                    losses.append(loss)
            for i in range(len(self.neurons[layer])):
                self.neurons[layer][i]["loss"] = losses[i] * self.sigmoid_derivative(self.neurons[layer][i]['output'])
    def adjust_weights(self,inputs,learning_rate):
        ins = inputs
        for layer in range(len(self.neurons)):
            if layer!=0:
                ins = []
                for neuron in self.neurons[layer-1]:
                    ins.append(neuron["output"])
            for neuron in self.neurons[layer]:
                for i in range(len(ins)):
                    neuron['weights'][i] += learning_rate * neuron['loss'] * ins[i]
                neuron["weights"][-1] += learning_rate * neuron['loss']
    def train(self,inputs,outs,epoch,learning_rate=0.5):
        for _ in range(epoch):
            sumofloss = 0
            for index,i in enumerate(inputs):
                output = self.feedforward(i)
                real_out = outs[index]
                sumofloss += (real_out-output[0])**2
                self.backpropagation(real_out)
                self.adjust_weights(i,learning_rate)
            #if _%(epoch/100)==0:
                #print("Epoch:"+str(_)+"\nLoss:"+str(sumofloss))
        return sumofloss
    def get_clone(self):
        weights = []
        for layer in range(len(self.neurons)):
            weights.append([])
            for neuron in self.neurons[layer]:
                weights[layer].append(neuron["weights"])
        return deepcopy(weights)
    def set_clone(self,weights):
        clone = deepcopy(weights)
        for layer in range(len(self.neurons)):
            for index,neuron in enumerate(self.neurons[layer]):
                neuron["weights"] = clone[layer][index]

