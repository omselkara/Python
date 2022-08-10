from tkinter import *
import time
from Game import Game
import random
import keyboard

def key(event):
    #if event.char==" ":
        #show = not show
    game.press(event.char)

width = 600
height = 600

fps = 75
pencere = Tk()
#pencere.bind("<Key>", key)
canvas = Canvas(pencere,bg="black",width=width,height=height,highlightthickness=0)
canvas.pack()
pencere.update()
canvas.update()


frame = time.time()

game = Game(width, height,1)
while 1:
    if time.time()-frame>=1/fps:        
        canvas.delete(ALL)
        if keyboard.is_pressed("w"):
            game.press("w")
        if keyboard.is_pressed("a"):
            game.press("a")
        if keyboard.is_pressed("d"):
            game.press("d")
        if keyboard.is_pressed(" "):
            game.press(" ")
        game.move()
        game.show(canvas)
        frame = time.time()
    canvas.update()

pencere.mainloop()
