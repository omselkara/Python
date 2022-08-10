class Head:
    def __init__(self):
        self.x = 2
        self.y = 0
        self.yön = [1,0]
        self.moved = True
        self.body = [Body(1,0,[1,0],[]),Body(0,0,[1,0],[])]

    def turn(self,face):
        if self.moved:
            if face=="w" and self.yön!=[0,+1] and self.yön!=[0,-1]:
                self.yön = [0,-1]
                self.moved = False
            elif face=="s" and self.yön!=[0,-1] and self.yön!=[0,+1]:
                self.yön = [0,+1]
                self.moved = False
            elif face=="a" and self.yön!=[+1,0] and self.yön!=[-1,0]:
                self.yön = [-1,0]
                self.moved = False
            elif face=="d" and self.yön!=[-1,0] and self.yön!=[+1,0]:
                self.yön = [+1,0]
                self.moved = False
            if not self.moved:
                for body in self.body:
                    body.moves.append([self.x,self.y,self.yön])

    def move(self):
        self.x += self.yön[0]
        self.y += self.yön[1]
        self.moved = True

    def add_body(self):
        newbody = Body(self.body[-1].oldx,self.body[-1].oldy,self.body[-1].oldyön,self.body[-1].moves)
        if self.body[-1].oldyön!=self.body[-1].yön:
            newbody.moves.insert(0,[self.body[-1].x,self.body[-1].y,self.body[-1].yön])
        self.body.append(newbody)


class Body:
    def __init__(self,x,y,yön,moves):
        self.x = x
        self.y = y
        self.oldx = x
        self.oldy = y
        self.oldyön = yön
        self.yön = yön
        self.moves = [[i[0],i[1],i[2]] for i in moves]
    
    def move(self):
        self.oldx = self.x
        self.oldy = self.y
        self.oldyön = self.yön
        self.x += self.yön[0]
        self.y += self.yön[1]
        if len(self.moves):
            if self.x==self.moves[0][0] and self.y==self.moves[0][1]:
                self.yön = self.moves[0][2]
                self.moves.pop(0)
