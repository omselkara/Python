import random 
from Player import Player
from Asteroid import Asteroid
from math import cos,sin,radians

class Game:
    def __init__(self,width,height,asteroid_count):
        self.asteroid_count = asteroid_count
        self.width = width
        self.height = height
        self.asteroids = []
        self.player = Player(width/2,height/2,width,height)
        self.dead = False
        self.score = 0
        self.lifespan = 1000
        for i in range(asteroid_count):
            self.generate_asteroid()
    
    def move(self):
        if not self.dead:
            self.lifespan -= 1
            for i in range(self.asteroid_count):
                if len(self.asteroids)<self.asteroid_count:
                    self.generate_asteroid()
                else:
                    break
            if self.player.x>self.width:
                self.player.x = 0
            if self.player.x<0:
                self.player.x = self.width
            if self.player.y>self.height:
                self.player.y = 0
            if self.player.y<0:
                self.player.y = self.height
            self.player.move()
            indexes = []
            for i in range(len(self.asteroids)):
                self.asteroids[i].move()
                if (self.asteroids[i].x+self.asteroids[i].radius*3<0 or self.asteroids[i].y+self.asteroids[i].radius*3<0 or 
                    self.asteroids[i].x-self.asteroids[i].radius*3>self.width or self.asteroids[i].y-self.asteroids[i].radius*3>self.height):
                    indexes.append([i,False])
                else:
                    for index in range(len(self.player.bullets)):
                        bullet = self.player.bullets[index]
                        dist = distance(bullet[0],bullet[1],self.asteroids[i].x,self.asteroids[i].y)
                        if dist<=self.asteroids[i].radius:
                            indexes.append([i,True])
                            self.player.bullets.pop(index)
                            self.score += 1
                            self.lifespan = 1000
                            if self.asteroids[i].radius/2>8:
                                self.asteroids.append(Asteroid(self.asteroids[i].x+cos(radians(self.asteroids[i].angle+45))*15,self.asteroids[i].y+sin(radians(self.asteroids[i].angle+45))*15, self.asteroids[i].angle+45,self.asteroids[i].radius/2))
                                self.asteroids.append(Asteroid(self.asteroids[i].x+cos(radians(self.asteroids[i].angle-45))*15,self.asteroids[i].y+sin(radians(self.asteroids[i].angle-45))*15, self.asteroids[i].angle-45,self.asteroids[i].radius/2))
                            break
            for i in range(0,len(indexes)):
                if not indexes[len(indexes)-i-1][1] and self.asteroids[indexes[len(indexes)-i-1][0]].radius==35:
                    self.generate_asteroid()
                self.asteroids.pop(indexes[len(indexes)-i-1][0])
            for i in self.asteroids:
                dist = distance(i.x,i.y,self.player.point1[0],self.player.point1[1])
                if dist<i.radius:
                    self.dead = True
                    break
                dist = distance(i.x,i.y,self.player.point2[0],self.player.point2[1])
                if dist<i.radius:
                    self.dead = True
                    break
                dist = distance(i.x,i.y,self.player.point3[0],self.player.point3[1])
                if dist<i.radius:
                    self.dead = True
                    break
            if self.lifespan<=0:
                self.dead = True
        self.dead = False

    def show(self,canvas):
        self.player.show(canvas)
        for i in self.asteroids:
            i.show(canvas)
        liste = self.player.inputs(self.asteroids)
        for i in range(8):
            angle = radians(i*45+self.player.angle)
            if liste[i]>0:
                canvas.create_line(self.player.x,self.player.y,self.player.x+cos(angle)*liste[i],self.player.y+sin(angle)*liste[i],fill="red")
            else:
                canvas.create_line(self.player.x,self.player.y,self.player.x+cos(angle)*1000,self.player.y+sin(angle)*1000,fill="white")
        canvas.create_text(0,0,text=f"Score:{self.score}",anchor="nw",fill="white",font=("italic",15))
        canvas.create_text(0,30,text=f"LifeSpan:{self.lifespan}",anchor="nw",fill="white",font=("italic",15))
    
    def press(self,button):
        if not self.dead:
            if button=="w":
                self.player.gas()
            elif button=="a":
                self.player.turn(-1)
            elif button=="d":
                self.player.turn(+1)
            elif button==" ":
                self.player.fire()
    
    def generate_asteroid(self):
        val = random.uniform(0,1)
        if val>=0 and val<0.25:
            x = -30
            y = random.randint(0,self.height)
            angle = random.randint(-60,+60)
        elif val>=0.25 and val<0.5:
            x = self.width+30
            y = random.randint(0,self.height)
            angle = random.randint(120,+240)
        elif val>=0.5 and val<0.75:
            x = random.randint(0,self.width)
            y = -30
            angle = random.randint(30,150)
        else:
            x = random.randint(0,self.width)
            y = self.height+30
            angle = random.randint(-150,-30)
        asteroid = Asteroid(x,y,angle)
        self.asteroids.append(asteroid)
    
def distance(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5
