import random

class Weight:
    def __init__(self,from_neuron,to_neuron):
        self.from_neuron = from_neuron
        self.to_neuron = to_neuron
        self.weight = random.uniform(-3,+3)

    def activate(self):
        self.to_neuron.value += (self.from_neuron.value*self.weight)