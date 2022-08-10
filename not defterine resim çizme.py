import numpy as np
from PIL import Image
import cv2
characters = [" ",".",",",":",";","o","x","%","#","@"]
def changetoascii(rgb):
    return characters[9-int(((rgb[0]+rgb[1]+rgb[2])/3)/(255/9))]
def write(name1,name2):
    img = np.array(Image.open(name1))
    img = cv2.resize(img,(600,100))
    text = []
    for y in range(len(img)):
        text.append([])
        for x in range(len(img[0])):
            text[y].append(changetoascii(img[y][x]))
    dosya = open(name2,"w")
    for y in text:
        for x in y:
            dosya.write(x)
        dosya.write("\n")
    dosya.close()
    return text
a = write("a.png","a.txt")
