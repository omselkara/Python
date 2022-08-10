import numpy as np
import datetime

cdef float activation(float x):
    cdef double e = 2.7182818284590452353602874713527
    return 1.0/ (1.0 + e**-x)

cdef float derivative(float x):
    return x*(1-x)

cdef list network(list layers):
    cdef list neurons = []
    cdef int layer,neuron,weight
    for layer in range(len(layers)-1):
        neurons.append([])
        for neuron in range(layers[layer+1]):
            neurons[layer].append([])
            for weight in range(layers[layer]+1):
                neurons[layer][neuron].append(np.random.uniform(-1,+1))
    return neurons

cdef list activate(list neurons,list inputs):
    cdef list lastinputs = inputs
    cdef int layer,neuron,weight
    cdef float value
    cdef list newinputs
    cdef list outputs = []
    for layer in range(len(neurons)):
        outputs.append(lastinputs)
        newinputs = []
        for neuron in range(len(neurons[layer])):
            value = 0
            value += neurons[layer][neuron][-1]
            for weight in range(len(neurons[layer][neuron])-1):
                value += lastinputs[weight]*neurons[layer][neuron][weight]
            newinputs.append(activation(value))
        lastinputs = newinputs
    outputs.append(lastinputs)
    return [lastinputs,outputs]

cdef list calculate_loss(list neurons,list outputs,list outs):
    cdef list losses = []
    cdef int layer,neuron,neuron2,weight,i
    cdef list loss
    cdef float value
    for layer in range(len(neurons)):
        losses.append([])
    for layer in reversed(range(len(neurons))):
        loss = []
        if layer==len(neurons)-1:
            for i in range(len(outs)):
                loss.append((outs[i]-outputs[layer+1][i])*derivative(outputs[layer+1][i]))
        else:
            for neuron in range(len(neurons[layer])):
                value = 0
                for neuron2 in range(len(neurons[layer+1])):
                    value += losses[layer+1][neuron2]*neurons[layer+1][neuron2][neuron]
                loss.append(value*derivative(outputs[layer+1][neuron]))
        losses[layer] = loss
    return losses
cdef void adjust_weights(list neurons,list losses,list outputs,float l_rate):
    cdef int layer,neuron,weight
    for layer in range(len(neurons)):
        for neuron in range(len(neurons[layer])):
            for weight in range(len(neurons[layer][neuron])-1):
                neurons[layer][neuron][weight] += losses[layer][neuron]*l_rate*outputs[layer][weight]
            neurons[layer][neuron][-1] += losses[layer][neuron]*l_rate

cdef void train(list neurons,list inputs,list outs,int epoch=10000,float l_rate=0.1,int interval=100):
    cdef int _,i
    cdef float loss 
    cdef list output,losses
    for _ in range(epoch):
        loss = 0
        for i in range(len(inputs)):
            output = activate(neurons,inputs[i])[1]
            losses = calculate_loss(neurons,output,outs[i])
            adjust_weights(neurons,losses,output,l_rate)
            loss += np.sum((np.array(outs[i])-output[-1])**2)
        if interval!=0 and _%interval==0:
            print(f"Epoch:{_}  Loss:{loss}")
    if interval!=0:
        print(f"Epoch:{_}  Loss:{loss}")

def create_network(layers):
    return network(layers)

def activate_network(neurons,inputs):
    return activate(neurons,inputs)[0]

def train_network(neurons,inputs,outs,epoch=10000,l_rate=0.1,interval=100):
    train(neurons,inputs,outs,epoch,l_rate,interval)

def save_network(neurons,name="save.npz"):
    dictionary = {}
    dictionary["neurons"] = neurons
    dictionary["time"] = datetime.datetime.now()
    np.savez(name, **dictionary)

def load_network(name="save.npz"):
    dictionary = np.load(name,allow_pickle=True)
    neurons = list(dictionary["neurons"])
    return neurons



        

    