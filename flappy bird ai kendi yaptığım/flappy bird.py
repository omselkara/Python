from tkinter import *
import time,random
from my_neat import net
pencere = Tk()
pencere.geometry("+0+0")
canvas = Canvas(pencere,width=400,height=600,highlightthickness=0,bg="cyan")
canvas.pack()
class bird:
    def __init__(self,yer):
        self.x = 75
        self.yer = yer
        self.y = 300
        self.gravity = 0.3
        self.velocity = 0
    def hareket(self):
        self.velocity += self.gravity
        self.y += self.velocity
    def jump(self):
        self.velocity = -7
    def display(self):
        self.hareket()
        self.bird = canvas.create_oval(self.x-10,self.y-10,self.x+10,self.y+10,fill="yellow",width=3)
    def remove(self):
        canvas.delete(self.bird)
class pipe():
    def __init__(self):
        self.x = 500
        self.y = random.randint(100,500)
    def display(self):
        self.x -= 2
        self.pipe1 = canvas.create_rectangle(self.x-25,0,self.x+25,self.y-75,fill="green")
        self.pipe2 = canvas.create_rectangle(self.x-25,self.y+75,self.x+25,600,fill="green")
    def remove(self):
        canvas.delete(self.pipe1)
        canvas.delete(self.pipe2)
pop = 100
nets = net(3,1,pop)
outs = [[-1],[1]]
while 1:
    an = time.time()
    birds = []
    pipes = []
    skor = 0
    pipeno = 0
    ins = [[200+random.randint(-150,350),375+random.randint(-200,125),225+random.randint(-125,275)],[400+random.randint(-150,350),375+random.randint(-200,125),225+random.randint(-125,275)]]
    nets.kill()
    nets.train(ins,outs,1000)
    for i in range(0,pop):
        exec("sayı{} = bird({})".format(i,i))
        exec("birds.append(sayı{})".format(i))
    frame = 1
    exec("pipe{} = pipe()".format(len(pipes)))
    exec("pipes.append(pipe{})".format(len(pipes)))
    while 1:
        if 1:
            if frame%180==0:
                exec("pipe{} = pipe()".format(len(pipes)))
                exec("pipes.append(pipe{})".format(len(pipes)))
            for i in pipes:
                i.display()
                if pipes[pipeno].x+25<=75:
                    pipeno += 1
                    skor += 1
                    for a in birds:
                        nets.genomes[a.yer].fitness += 5
            if len(pipes)>1:
                if pipes[pipeno-1].x+25<=0:
                    pipes.pop(pipeno-1)
                    pipeno -= 1
            ölenler = []
            for index,i in enumerate(birds):
                if i.y >=610 or i.y<-10:
                    ölenler.append(index)
                if (i.x>=pipes[pipeno].x-25 and i.x<=pipes[pipeno].x+25) and (i.y<=pipes[pipeno].y-75 or i.y>=pipes[pipeno].y+75):
                    ölenler.append(index)
            for i in ölenler[::-1]:
                nets.genomes[birds[i].yer].fitness -= 5
                birds.remove(birds[i])
            if len(birds) == 0:
                canvas.delete(ALL)
                break
            for i in birds:
                output = nets.genomes[i.yer].output([i.y,(pipes[pipeno].y-75),(pipes[pipeno].y+75)])
                if output[0]>=0.5:
                    i.jump()
            for i in birds:
                i.display()
            yazı = canvas.create_text(200,75,text=str(skor),font=("italic",30))
            canvas.update()
            canvas.delete(yazı)
            for i in birds:
                i.remove()
            for i in pipes:
                i.remove()
            an = time.time()
            frame +=1
            for a in birds:
                nets.genomes[a.yer].fitness += 0.1
pencere.mainloop()
