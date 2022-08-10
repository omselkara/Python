import random
from PIL import Image
import numpy as np
seed = 17471798
random.seed(seed)
liste = []
for y in range(100):
    liste.append([])
    for x in range(300):
        liste[y].append([255,255,255])
y = 50
for x in range(300):
    for y2 in range(0,y):
        liste[99-y2][x] = [0,255,0]
    olasılık = []
    if y>0:
        olasılık.append(-1)
    olasılık.append(0)
    if y<100:
        olasılık.append(+1)
    y += olasılık[random.randint(0,len(olasılık)-1)]
liste = np.asarray(liste,np.uint8)
liste = Image.fromarray(liste)
liste.save("a.png")
