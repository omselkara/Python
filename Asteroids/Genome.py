from Layer import Layer
import random

class Genome:
    def __init__(self,schema):
        self.schema = schema
        self.layers = []
        self.score = 0
        for layer in range(1,len(self.schema)):
            self.layers.append(Layer(self.schema[layer],self.schema[layer-1]))
    
    def activate(self,inputs):
        ins = inputs
        for layer in self.layers:
            ins = layer.activate(ins)
        return ins

    def mutate(self):
        for layer in self.layers:
            layer.mutate()

    def generate_baby(self,parent):
        if self.score>parent.score:
            bestparent = self
            otherparent = parent
        else:
            bestparent = parent
            otherparent = self
        score1 = bestparent.score
        score2 = otherparent.score
        if score2<0:
            add = abs(score1)+abs(score2)
            score1 += add
            score2 += add
        score1 += 0.000000000000000001
        score2 += 0.000000000000000001
        multiplier= score1/(score1+score2) 
        baby = Genome(self.schema)
        for layer_index in range(len(self.layers)):
            layerbest = bestparent.layers[layer_index]
            layerother = otherparent.layers[layer_index]
            layerbaby = baby.layers[layer_index]
            for neuron_index in range(layerbest.neuron_count):
                neuronbest = layerbest.neurons[neuron_index]
                neuronother = layerother.neurons[neuron_index]
                neuronbaby = layerbaby.neurons[neuron_index]
                if random.uniform(0,1)<multiplier:
                    neuronbaby.bias = neuronbest.bias
                else:
                    neuronbaby.bias = neuronother.bias
                #neuronbaby.bias = neuronother.bias+(neuronbest.bias-neuronother.bias)*multiplier
                for weight_index in range(self.layers[layer_index].neurons[neuron_index].weight_count):
                    weightbest = neuronbest.weights[weight_index]
                    weightother = neuronother.weights[weight_index]
                    if random.uniform(0,1)<multiplier:
                        neuronbaby.weights[weight_index] = weightbest
                    else:
                        neuronbaby.weights[weight_index] = weightother
                    #neuronbaby.weights[weight_index] = weightother+(weightbest-weightother)*multiplier
        return baby