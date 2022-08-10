from math import cos,sin,tan,radians,atan2,atan,degrees

class Player:
    def __init__(self,x,y,width,height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.acc = [0,0]
        self.angle = -90
        self.calc_points()
        self.lastfire = 0
        self.bullets = []
    
    def move(self):
        self.lastfire -= 1
        indexes = []
        for index in range(len(self.bullets)):
            i = self.bullets[index]
            i[0] += cos(radians(i[2]))*10
            i[1] += sin(radians(i[2]))*10
            if i[0]<0 or i[0]>self.width or i[1]<0 or i[1]>self.height:
                indexes.append(index)
        for i in range(1,len(indexes)):
            self.bullets.pop(indexes[len(indexes)-i])

        self.x += self.acc[0]#cos(radians(self.angle))*
        self.y += self.acc[1]#sin(radians(self.angle))*
        if self.acc[0]<0:
            self.acc[0] += 0.05
            self.acc[0] = min(0,self.acc[0])
        else:
            self.acc[0] -= 0.05
            self.acc[0] = max(0,self.acc[0])
        if self.acc[1]<0:
            self.acc[1] += 0.05
            self.acc[1] = min(0,self.acc[1])
        else:
            self.acc[1] -= 0.05
            self.acc[1] = max(0,self.acc[1])
        self.calc_points()

    def turn(self,face):
        self.angle += face*5
        self.angle = self.angle%360
    
    def gas(self):
        self.acc[0] += cos(radians(self.angle))*0.2
        self.acc[1] += sin(radians(self.angle))*0.2
        if self.acc[0]>5:
            self.acc[0]=5
        elif self.acc[0]<-5:
            self.acc[0]=-5
        if self.acc[1]>5:
            self.acc[1]=5
        elif self.acc[1]<-5:
            self.acc[1]=-5
        
    def calc_points(self):
        self.point1 = (self.x+cos(radians(self.angle))*25,self.y+sin(radians(self.angle))*25)
        self.point2 = (self.x+cos(radians(self.angle+233))*16,self.y+sin(radians(self.angle+233))*16)
        self.point3 = (self.x+cos(radians(self.angle+127))*16,self.y+sin(radians(self.angle+127))*16)

    def show(self,canvas):
        canvas.create_line(self.point1[0],self.point1[1],self.point2[0],self.point2[1],fill="white")
        canvas.create_line(self.point2[0],self.point2[1],self.x,self.y,fill="white")
        canvas.create_line(self.x,self.y,self.point3[0],self.point3[1],fill="white")
        canvas.create_line(self.point3[0],self.point3[1],self.point1[0],self.point1[1],fill="white")
        for i in self.bullets:
            canvas.create_oval(i[0]-1,i[1]-1,i[0]+1,i[1]+1,fill="white",width=0)
    
    def fire(self):
        if self.lastfire<=0:
            self.bullets.append([self.point1[0],self.point1[1],self.angle])
            self.lastfire = 20
        
    def inputs(self,asteroids):
        liste = []
        for i in range(8):
            angle = i*45+self.angle
            rad_angle = radians(angle)
            m = tan(rad_angle)
            a = m
            b = -1
            c = -m*self.x+self.y
            denom = (a**2+b**2)**0.5
            closest = -1
            for asteroid in asteroids:
                x2 = asteroid.x-self.x
                y2 = asteroid.y-self.y
                dist = abs(a*asteroid.x+b*asteroid.y+c)/denom
                if dist<asteroid.radius:    
                    angle2 = degrees(atan2(y2,x2))
                    if (i*45)==0:
                        print(angle,angle2)
                    if abs(angle2-angle)<=90:
                        distance = (y2**2+x2**2)**0.5
                        distance = distance-(((asteroid.radius**2)-dist**2)**0.5)
                        if closest==-1 or distance<closest:
                            closest = distance
                    elif abs((angle2%360)-angle)<=90:
                        distance = (y2**2+x2**2)**0.5
                        distance = distance-(((asteroid.radius**2)-dist**2)**0.5)
                        if closest==-1 or distance<closest:
                            closest = distance
                    else:
                        angle = angle%360
                        if abs(angle2-angle)<=90:
                            distance = (y2**2+x2**2)**0.5
                            distance = distance-(((asteroid.radius**2)-dist**2)**0.5)
                            if closest==-1 or distance<closest:
                                closest = distance
                        elif abs((angle2%360)-angle)<=90:
                            distance = (y2**2+x2**2)**0.5
                            distance = distance-(((asteroid.radius**2)-dist**2)**0.5)
                            if closest==-1 or distance<closest:
                                closest = distance
            closest = max(0,closest)
            liste.append(closest)         
        return liste

