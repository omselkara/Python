from colormap import rgb2hex
from Snake import Head
import random

colors = [rgb2hex(170,204,102),rgb2hex(241, 17, 26),rgb2hex(43, 51, 26)]

class Map:
    def __init__(self,col,row,dx,dy):
        self.col = col
        self.row = row
        self.dx = dx
        self.dy = dy
        self.map = [[0 for x in range(self.col)] for y in range(self.row)]
        self.head = Head()
        self.map[0][2] = -1
        self.map[0][1] = -1
        self.map[0][0] = -1
        self.dead = False
        self.foodx = 0
        self.foody = 0
        self.generate_food()
        self.life = col*row

    def generate_food(self):
        liste = []
        for y in range(self.row):
            for x in range(self.col):
                if self.map[y][x]==0:
                    liste.append([x,y])
        self.foodx,self.foody = random.choice(liste)

    def move(self):
        if not self.dead:
            self.life -= 1
            if self.life==0:
                self.dead = True
            self.head.body[-1].move()
            self.map[self.head.body[-1].oldy][self.head.body[-1].oldx] = 0
            x = self.head.x
            y = self.head.y
            self.head.move()
            if self.dead or self.head.x>=self.col or self.head.x<0 or self.head.y>=self.row or self.head.y<0 or self.map[self.head.y][self.head.x]==-1:
                self.dead = True
                self.head.x = x
                self.head.y = y
                self.head.body[-1].x = self.head.body[-1].oldx
                self.head.body[-1].y = self.head.body[-1].oldy
                self.head.body[-1].yön = self.head.body[-1].oldyön
                self.map[self.head.body[-1].y][self.head.body[-1].x] = -1
            else:
                self.map[y][x] = 0
                self.map[self.head.y][self.head.x] = -1
            if not self.dead:
                for body in self.head.body[0:-1]:
                    self.map[body.y][body.x] = 0
                    body.move()
                    self.map[body.y][body.x] = -1
                self.map[self.head.body[-1].y][self.head.body[-1].x] = -1
                if self.head.x==self.foodx and self.head.y==self.foody:
                    self.generate_food()
                    self.head.add_body()
                    self.life += len(self.head.body)*40
    
    def inputs(self):
        faces = [[-1,-1],[0,-1],[+1,-1],[-1,0],[+1,0],[-1,+1],[0,+1],[+1,+1]]
        liste = []
        #food = []
        #wall = []
        #body = []
        for face in faces:
            #food.append(0)
            #wall.append(0)
            #body.append(0)
            x = self.head.x+face[0]
            y = self.head.y+face[1]
            dist = 0
            while 1:
                if x<0 or x>=self.col or y<0 or y>=self.row:
                    #wall[-1] = dist
                    liste.append(dist)
                    break
                if self.map[y][x]==-1:# and food[-1]==0:
                    #body[-1] = dist
                    liste.append(dist)
                    #wall[-1] = dist
                    break
                #if self.map[y][x]==1:# and body[-1]==0:
                    #food[-1] = dist
                    #break
                x += face[0]
                y += face[1]
                dist += 1
        #for i in range(8):
            #liste.append(body[i])
        #for i in range(8):
            #liste.append(wall[i])
        #for i in range(8):
            #liste.append(food[i])
        liste.append(self.foodx-self.head.x)
        liste.append(self.foody-self.head.y)
        return liste

    def draw(self,canvas):
        canvas.create_rectangle(0,0,self.col*self.dx,self.row*self.dy,fill=colors[0],width=0)
        self.map[self.foody][self.foodx] = 1
        for y in range(self.row):
            for x in range(self.col):
                if self.map[y][x]!=0:
                    canvas.create_rectangle(x*self.dx,y*self.dy,x*self.dx+self.dx,y*self.dy+self.dy,fill=colors[self.map[y][x]],width=0)
    
    def press(self,face):
        self.head.turn(face)
