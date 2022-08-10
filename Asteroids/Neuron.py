import random
from Activation import tanh

class Neuron:
    def __init__(self,weight_count):
        self.weight_count = weight_count
        self.bias = random.uniform(-3,+3)
        self.weights = [random.uniform(-3,+3) for i in range(self.weight_count)]
        self.multiplier = weight_count**0.5
    
    def activate(self,inputs):
        value = 0
        for i in range(self.weight_count):
            value += self.weights[i]*inputs[i]
        return tanh(value/self.multiplier+self.bias)

    def mutate(self):
        if random.uniform(0,1)<0.2:
            self.bias += random.uniform(-1, +1)
        elif random.uniform(0,1)<0.1:
            self.bias = random.uniform(-3, +3)
        elif random.uniform(0,1)<0.05:
            self.bias = 0
        for i in range(self.weight_count):
            if random.uniform(0,1)<0.2:
                self.weights[i] += random.uniform(-1, +1)
            elif random.uniform(0,1)<0.1:
                self.weights[i] = random.uniform(-3, +3)
            elif random.uniform(0,1)<0.05:
                self.weights[i] = 0


    