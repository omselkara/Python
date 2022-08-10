import random
from Weight import Weight
from Activation import tanh

class Neuron:
    def __init__(self,layer,index):
        self.bias = random.uniform(-3,+3)
        self.layer = layer
        self.index = index
        self.value = 0
        self.weights = []

    def connect(self,to_neuron):
        to_neuron.weights.append(Weight(self,to_neuron))

    def activate(self):
        self.value = self.bias
        for i in self.weights:
            i.activate()
        self.value = tanh(self.value/(max(1,len(self.weights)+1)**0.5))

    def get_detailed_schema(self):
        schema = [self.index,self.bias,[]]
        for weight in self.weights:
            schema[-1].append([[weight.from_neuron.layer.layer_type,weight.from_neuron.layer.index,weight.from_neuron.index],#[weight.to_neuron.layer.layer_type,weight.to_neuron.layer.index,weight.to_neuron.index]
            weight.weight])
        return schema
    
    def apply_detailed_schema(self,schema):
        self.weights = []
        for i in range(len(schema)):
            if schema[i][0][0]=="Inputs":
                from_neuron = self.layer.genome.layers["Inputs"].neurons[schema[i][0][2]]
            else:
                from_neuron = self.layer.genome.layers["Hiddens"][schema[i][0][1]].neurons[schema[i][0][2]]
            weight = Weight(from_neuron,self)
            weight.weight = schema[i][1]
            self.weights.append(weight)
