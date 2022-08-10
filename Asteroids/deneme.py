from tkinter import *
import time
from Game import Game
from Network import Network
import random

def key(event):
    global show
    if event.char==" ":
        show = not show
    #map.press(event.char)

width = 600
height = 600

fps = 60
pencere = Tk()
pencere.bind("<Key>", key)
canvas = Canvas(pencere,bg="black",width=width,height=height,highlightthickness=0)
canvas.pack()
pencere.update()
canvas.update()


frame = time.time()

game = Game(width, height,10)

net = Network([8,32,16,4],250)
#net.load()
best = net.genomes[0]
show = True

while 1:
    if game.dead or not show:
        for gen in net.genomes:
            gen.seed = random.uniform(0,100)
            random.seed(gen.seed)
            game = Game(width, height,10)
            while not game.dead:
                out = gen.activate(game.player.inputs(game.asteroids))
                if out[0]>0.5:
                    game.press("w")
                if out[1]>0.5:
                    game.press("a")
                if out[2]>0.5:
                    game.press("d")
                if out[3]>0.5:
                    game.press(" ")
                game.move()
            gen.score = 2**game.score
        best = net.select()[0]
        random.seed(best.seed)
        game = Game(width, height,10)
    if show and time.time()-frame>=1/fps:        
        canvas.delete(ALL)
        out = best.activate(game.player.inputs(game.asteroids))
        if out[0]>0.5:
            game.press("w")
        if out[1]>0.5:
            game.press("a")
        if out[2]>0.5:
            game.press("d")
        if out[3]>0.5:
            game.press(" ")
        game.move()
        game.show(canvas)
        frame = time.time()
    canvas.update()

pencere.mainloop()
