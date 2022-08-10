import numpy as np
import json
np.warnings.filterwarnings('ignore')
def activation(x):
    return 1.0 / (1.0 + np.exp(-x))
def derivative(x):
    return x*(1-x)
class network:
    def __init__(this,layers,weights=(-1,+1)):
        this.inputs = layers[0]
        this.layers = layers
        this.neurons = [np.random.uniform(weights[0],weights[1],(this.layers[layer],this.layers[layer-1]+1)) for layer in range(1,len(this.layers))]
        this.outputs = []
        this.losses = []
    def activate(this,inputs):
        lastinputs = inputs
        this.outputs = [np.array(lastinputs)]
        for layer in range(len(this.layers)-1):
            this.outputs.append([])
            lastinputs = np.array(list(map(activation,np.sum(this.neurons[layer][:,:-1]*lastinputs,axis=1)+this.neurons[layer][:,-1])))
            this.outputs[layer+1] = lastinputs
        return lastinputs
    def calculate_loss(this,outs):
        this.losses = []
        for layer in range(len(this.layers)-1):
            this.losses.append([])
        for layer in reversed(range(len(this.layers)-1)):
            if layer==len(this.layers)-2:
                losses = outs-this.outputs[layer+1]
            else:
                losses = []
                for neuron in range(this.layers[layer+1]):
                    loss = 0
                    for neuron2 in range(this.layers[layer+2]):
                        loss += this.losses[layer+1][neuron2]*this.neurons[layer+1][neuron2][neuron]
                    losses.append(loss)
            this.losses[layer] = losses*derivative(this.outputs[layer+1])
    def adjust_weights(this,l_rate):
        for layer in range(len(this.layers)-1):
            for neuron in range(this.layers[layer+1]):
                this.neurons[layer][neuron][:-1] += this.losses[layer][neuron]*l_rate*this.outputs[layer]
                this.neurons[layer][neuron][-1] += this.losses[layer][neuron]*l_rate
    def train(this,inputs,outs,epoch=10000,l_rate=0.1,interval=100):
        for _ in range(epoch):
            loss = 0
            for i in range(len(inputs)):
                this.activate(inputs[i])
                this.calculate_loss(outs[i])
                this.adjust_weights(l_rate)
                loss += np.sum((np.array(outs[i])-this.outputs[-1])**2)
            if _%interval==0:
                print(f"Epoch:{_}  Loss:{loss}")
        print(f"Epoch:{_}  Loss:{loss}")
    def save(this,name="save.npz"):
        dictionary = {}
        dictionary["neurons"] = this.neurons
        dictionary["neurons2"] = this.neurons
        np.savez(name, **dictionary)
    def load(this,name="save.npz"):
        dictionary = np.load(name,allow_pickle=True)
        this.neurons = dictionary["neurons"]

            
