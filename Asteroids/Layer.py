from Neuron import Neuron

class Layer:
    def __init__(self,neuron_count,prev_neuron_count):
        self.neuron_count = neuron_count
        self.prev_neuron_count = prev_neuron_count
        self.neurons = [Neuron(self.prev_neuron_count) for i in range(neuron_count)]

    def activate(self,inputs):
        values = []
        for neuron in self.neurons:
            values.append(neuron.activate(inputs))
        return values
    
    def mutate(self):
        for neuron in self.neurons:
            neuron.mutate()