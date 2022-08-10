from tkinter import *
import time
from Map import Map
from Network import Network
import random

def key(event):
    global show
    if event.char==" ":
        show = not show
    #map.press(event.char)

fps = 100000
pencere = Tk()
pencere.bind("<Key>", key)
canvas = Canvas(pencere,bg="gray",width=600,height=600,highlightthickness=0)
canvas.pack()
pencere.update()
canvas.update()


frame = time.time()

col = 30
row = 30
dx = canvas.winfo_width()/col
dy = canvas.winfo_height()/row
map = Map(col,row,dx,dy)
map.dead = False

net = Network(10, 32, 4, 500)
#net.load()
best = net.genomes[0]
show = True

while 1:
    if map.dead or not show:
        for gen in net.genomes:
            gen.seed = random.uniform(0,100)
            random.seed(gen.seed)
            map = Map(col,row,dx,dy)
            while not map.dead:
                out = gen.activate(map.inputs())
                if out[0]>0.5:
                    map.head.turn("w")
                if out[1]>0.5 and map.head.moved:
                    map.head.turn("d")
                if out[2]>0.5 and map.head.moved:
                    map.head.turn("s")
                if out[3]>0.5 and map.head.moved:
                    map.head.turn("a")
                map.move()
            gen.score = len(map.head.body)**4
        best = net.select()
        random.seed(best.seed)
        map = Map(col,row,dx,dy)
    if show and time.time()-frame>=1/fps:        
        canvas.delete(ALL)
        out = best.activate(map.inputs())
        if out[0]>0.5:
            map.head.turn("w")
        if out[1]>0.5 and map.head.moved:
            map.head.turn("d")
        if out[2]>0.5 and map.head.moved:
            map.head.turn("s")
        if out[3]>0.5 and map.head.moved:
            map.head.turn("a")
        map.move()
        map.draw(canvas)
        frame = time.time()
    canvas.update()

pencere.mainloop()
