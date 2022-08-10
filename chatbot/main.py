import json
import random
from copy import deepcopy
from ai import *
load = True
net = network()
if not load:
    net.train("texts.json",100,100)
    net.save()
else:
    net.load()
while 1:
    text = input(">>>")
    if text!="" or text!=" ":
        print(net.activate(text))
