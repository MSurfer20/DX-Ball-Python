import global_stuff 
from entity import entity
class ufo(entity):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.length=15
        self.width=5
        self.health=100
    
    def moveufo(self, key, board):
        if key=='d':
            max_d=min(3, global_stuff.cols-self.length-self.y+1)
            # for ball in board._balls:
            self.y+=max_d
            # for ball in board._balls:
            #     if ball.x>=self.x and self.x+self.length>ball.x and ball.y>=self.y and ball.y<=self.y+self.width:
            #         ball.x=self.x+self.length+1
            #         ball.x_vel=abs(ball.x_vel)
                
            # for ball in balls:
            #     if ball.isstuck():
            #         ball.movestuckball(max_d)
        elif key=='a':
            max_d=self.y-max(0, self.y-3)
            self.y-=max_d
            # for ball in balls:
            #     if ball.isstuck():
            #         ball.movestuckball(-max_d)
    
    def increasesize(self):
        self.actual_length+=6
        self.length=max(self.actual_length,6)
    
    def decreasesize(self):
        self.actual_length-=6
        self.length=max(self.actual_length,6)
    
    def get_left_coor(self):
        return self.y
    
    def get_right_coor(self):
        return self.y+self.length
    
    def get_length(self):
        return self.length
    
    def isstick(self):
        return self.stick
    
    def check(self, x, y):
        if (x>=self.x and x<=self.x+self.width) and (y>=self.y and y<=self.y+self.length):
            return True
        return False
    
    def reducelvl(self):
        self.health-=10