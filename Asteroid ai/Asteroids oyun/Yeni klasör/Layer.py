from Neuron import Neuron
import random

class Layer:
    def __init__(self,genome,layer_type,index,neuron_count):
        self.genome = genome
        self.layer_type = layer_type
        self.index = index
        self.neurons = []
        for i in range(neuron_count):
            self.neurons.append(Neuron(self,i))
    
    def add_neuron(self):
        self.neurons.append(Neuron(self,len(self.neurons)))

    def activate(self):
        for i in self.neurons:
            i.activate()

    def get_detailed_schema(self):
        schema = [self.layer_type,self.index]
        for neuron in self.neurons:
            schema.append(neuron.get_detailed_schema())
        return schema
    
    def apply_detailed_schema(self,schema):
        self.neurons = []
        for i in range(2,len(schema)):
            neuron = Neuron(self,schema[i][0])
            neuron.bias = schema[i][1]
            neuron.apply_detailed_schema(schema[i][2])
            self.neurons.append(neuron)
                

    