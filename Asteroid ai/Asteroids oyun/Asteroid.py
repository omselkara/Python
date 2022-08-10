from math import cos,sin,radians
class Asteroid:
    def __init__(self,x,y,angle,radius=35):
        self.radius = radius
        self.x = x
        self.y = y
        self.angle = angle

    def move(self):
        self.x += cos(radians(self.angle))*2
        self.y += sin(radians(self.angle))*2
    
    def show(self,canvas):
        canvas.create_oval(self.x-self.radius,self.y-self.radius,self.x+self.radius,self.y+self.radius,outline="white")