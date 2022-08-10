from Layer import Layer
from Neuron import Neuron
from Weight import Weight
import random

class Genome:
    def __init__(self,input,hidden,output,baby=False):
        self.score = 0
        self.input = input
        self.output = output
        self.layers = {"Inputs":Layer(self,"Inputs",0,self.input),"Hiddens":[Layer(self,"Hiddens",0,hidden)],
        "Outputs":Layer(self,"Outputs",0,self.output)}
        if not baby:
            self.mutate(hidden+input+output,True)

    def mutate(self,repeat=1,connect=False):
        for i in range(repeat):
            #add neuron
            if random.uniform(0,1)<=0.01:
                if random.uniform(0,1)<0.1/len(self.layers["Hiddens"]):
                    self.layers["Hiddens"].append(Layer(self,"Hiddens",len(self.layers["Hiddens"]),1))
                else:
                    layer = random.randint(0,len(self.layers["Hiddens"])-1)
                    self.layers["Hiddens"][layer].add_neuron()
            #connect neurons
            if (random.uniform(0,1)<=0.2 and not connect) or (random.uniform(0,1)<0.75 and connect):
                layer1 = random.randint(0,len(self.layers["Hiddens"]))
                layer2 = layer1+random.randint(0,len(self.layers["Hiddens"])-layer1)
                if layer1==0:
                    layer1 = self.layers["Inputs"]
                else:
                    layer1 = self.layers["Hiddens"][layer1-1]
                if layer2==len(self.layers["Hiddens"]):
                    layer2 = self.layers["Outputs"]
                else:
                    layer2 = self.layers["Hiddens"][layer2]
                neuron1 = random.choice(layer1.neurons)
                neuron2 = random.choice(layer2.neurons)
                neuron1.connect(neuron2)
            #cut connect neurons
            if random.uniform(0,1)<=0.05:
                layer = random.randint(0,len(self.layers["Hiddens"]))
                if layer==len(self.layers["Hiddens"]):
                    layer = self.layers["Outputs"]
                else:
                    layer = self.layers["Hiddens"][layer]
                neuron = random.choice(layer.neurons)
                if len(neuron.weights)>0:
                    index = random.randint(0,len(neuron.weights)-1)
                    neuron.weights.pop(index)
            #bias mutate    
            if random.uniform(0, 1)<0.15:
                layer = random.randint(0,len(self.layers["Hiddens"]))
                if layer==len(self.layers["Hiddens"]):
                    layer = self.layers["Outputs"]
                else:
                    layer = self.layers["Hiddens"][layer]
                neuron = random.choice(layer.neurons)
                neuron.bias += random.uniform(-0.5,+0.5)
            #bias mutate
            elif random.uniform(0, 1)<0.1:
                layer = random.randint(0,len(self.layers["Hiddens"]))
                if layer==len(self.layers["Hiddens"]):
                    layer = self.layers["Outputs"]
                else:
                    layer = self.layers["Hiddens"][layer]
                neuron = random.choice(layer.neurons)
                neuron.bias = random.uniform(-3,+3)
            #bias mutate
            elif random.uniform(0, 1)<0.05:
                layer = random.randint(0,len(self.layers["Hiddens"]))
                if layer==len(self.layers["Hiddens"]):
                    layer = self.layers["Outputs"]
                else:
                    layer = self.layers["Hiddens"][layer]
                neuron = random.choice(layer.neurons)
                neuron.bias = 0
            #weight mutation
            if random.uniform(0, 1)<0.15:
                layer = random.randint(0,len(self.layers["Hiddens"]))
                if layer==len(self.layers["Hiddens"]):
                    layer = self.layers["Outputs"]
                else:
                    layer = self.layers["Hiddens"][layer]
                neuron = random.choice(layer.neurons)
                if len(neuron.weights)>0:
                    weight = random.choice(neuron.weights)
                    weight.weight += random.uniform(-0.5,+0.5)
            #weight mutation
            elif random.uniform(0, 1)<0.1:
                layer = random.randint(0,len(self.layers["Hiddens"]))
                if layer==len(self.layers["Hiddens"]):
                    layer = self.layers["Outputs"]
                else:
                    layer = self.layers["Hiddens"][layer]
                neuron = random.choice(layer.neurons)
                if len(neuron.weights)>0:
                    weight = random.choice(neuron.weights)
                    weight.weight = random.uniform(-3,+3)
            #weight mutation
            elif random.uniform(0, 1)<0.05:
                layer = random.randint(0,len(self.layers["Hiddens"]))
                if layer==len(self.layers["Hiddens"]):
                    layer = self.layers["Outputs"]
                else:
                    layer = self.layers["Hiddens"][layer]
                neuron = random.choice(layer.neurons)
                if len(neuron.weights)>0:
                    weight = random.choice(neuron.weights)
                    weight.weight = 0

    def activate(self,inputs):
        for i in range(len(self.layers["Inputs"].neurons)):
            self.layers["Inputs"].neurons[i].value = inputs[i]
        for i in self.layers["Hiddens"]:
            i.activate()
        outputs = []
        for i in self.layers["Outputs"].neurons:
            i.activate()
            outputs.append(i.value)
        return outputs

    def generate_baby(self,parent,a=0):
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
        #selecting best probability
        probability = score1/(score1+score2)
        baby = Genome(self.input,0,self.output,True)
        baby.layers["Hiddens"] = []
        for layer_index in range(len(bestparent.layers["Hiddens"])):
            layerbest = bestparent.layers["Hiddens"][layer_index]
            layerbaby = Layer(baby,"Hiddens",layer_index,0)
            baby.layers["Hiddens"].append(layerbaby)
            layerother = 0
            if len(otherparent.layers["Hiddens"])>layer_index:
                layerother = otherparent.layers["Hiddens"][layer_index]
            for neuron_index in range(len(layerbest.neurons)):
                neuronbest = layerbest.neurons[neuron_index]
                neuronbaby = Neuron(layerbaby,neuron_index)
                layerbaby.neurons.append(neuronbaby)
                neuronother = 0
                if layerother and len(layerother.neurons)>neuron_index:
                    neuronother = layerother.neurons[neuron_index]
                if (random.uniform(0,1)<probability or not neuronother):
                    neuronbaby.bias = neuronbest.bias
                else:
                    neuronbaby.bias = neuronother.bias
                for weight_index in range(len(neuronbest.weights)):
                    weightbest = neuronbest.weights[weight_index]
                    weightother = 0
                    if neuronother and len(neuronother.weights)>weight_index:
                        weightother = neuronother.weights[weight_index]
                    if (random.uniform(0,1)<probability or not weightother or weightother.from_neuron.layer.index>=len(bestparent.layers["Hiddens"]) or
                    (weightother.from_neuron.layer.layer_type=="Hiddens" and weightother.from_neuron.index>=len(bestparent.layers["Hiddens"][weightother.from_neuron.layer.index].neurons)) or
                    (weightother.from_neuron.layer.layer_type=="Inputs" and weightother.from_neuron.index>=len(bestparent.layers["Inputs"].neurons))):
                        if weightbest.from_neuron.layer.layer_type=="Hiddens":
                            from_neuron = baby.layers["Hiddens"][weightbest.from_neuron.layer.index].neurons[weightbest.from_neuron.index]
                        else:
                            from_neuron = baby.layers["Inputs"].neurons[weightbest.from_neuron.index]
                        from_neuron.connect(neuronbaby)
                        neuronbaby.weights[-1].weight = weightbest.weight
                    else:
                        if weightother.from_neuron.layer.layer_type=="Hiddens":
                            from_neuron = baby.layers["Hiddens"][weightother.from_neuron.layer.index].neurons[weightother.from_neuron.index]
                        else:
                            from_neuron = baby.layers["Inputs"].neurons[weightother.from_neuron.index]
                        from_neuron.connect(neuronbaby)
                        neuronbaby.weights[-1].weight = weightother.weight            
        for neuron_index in range(self.output):
            neuronbest = bestparent.layers["Outputs"].neurons[neuron_index]
            neuronother = otherparent.layers["Outputs"].neurons[neuron_index]
            neuronbaby = baby.layers["Outputs"].neurons[neuron_index]
            if random.uniform(0,1)<probability:
                neuronbaby.bias = neuronbest.bias
            else:
                neuronbaby.bias = neuronother.bias
            for weight_index in range(len(neuronbest.weights)):
                weightbest = neuronbest.weights[weight_index]
                weightother = 0
                if weight_index<len(neuronother.weights):
                    weightother = neuronother.weights[weight_index]
                if (random.uniform(0,1)<probability or not weightother or weightother.from_neuron.layer.index>=len(bestparent.layers["Hiddens"]) or
                (weightother.from_neuron.layer.layer_type=="Hiddens" and weightother.from_neuron.index>=len(bestparent.layers["Hiddens"][weightother.from_neuron.layer.index].neurons)) or
                (weightother.from_neuron.layer.layer_type=="Inputs" and weightother.from_neuron.index>=len(bestparent.layers["Inputs"].neurons))):
                    if weightbest.from_neuron.layer.layer_type=="Hiddens":
                        from_neuron = baby.layers["Hiddens"][weightbest.from_neuron.layer.index].neurons[weightbest.from_neuron.index]
                    else:
                        from_neuron = baby.layers["Inputs"].neurons[weightbest.from_neuron.index]
                    from_neuron.connect(neuronbaby)
                    neuronbaby.weights[-1].weight = weightbest.weight
                else:
                    if weightother.from_neuron.layer.layer_type=="Hiddens":
                        from_neuron = baby.layers["Hiddens"][weightother.from_neuron.layer.index].neurons[weightother.from_neuron.index]
                    else:
                        from_neuron = baby.layers["Inputs"].neurons[weightother.from_neuron.index]
                    from_neuron.connect(neuronbaby)
                    neuronbaby.weights[-1].weight = weightother.weight
        return baby
        
    def get_schema(self):
        layers = [self.input]
        for i in self.layers["Hiddens"]:
            layers.append(len(i.neurons))
        layers.append(self.output)
        return layers

    def get_detailed_schema(self):
        schema = []
        schema.append(self.layers["Inputs"].get_detailed_schema())
        schema.append([])
        for layer in self.layers["Hiddens"]:
            schema[1].append(layer.get_detailed_schema())
        schema.append(self.layers["Outputs"].get_detailed_schema())
        return schema
    
    def apply_detailed_schema(self,schema):
        self.layers["Hiddens"] = []
        self.layers["Inputs"].apply_detailed_schema(schema[0])
        for i in range(len(schema[1])):
            layer = Layer(self,schema[1][i][0],schema[1][i][1],0)
            layer.apply_detailed_schema(schema[1][i])
            self.layers["Hiddens"].append(layer)
        self.layers["Outputs"].apply_detailed_schema(schema[2])
