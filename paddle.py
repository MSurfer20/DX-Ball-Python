import global_stuff 
from entity import entity
import playsound
class paddle(entity):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.length=20
        self.actual_length=20
        self.stick=False
    
    def movepaddle(self, key, balls):
        if key=='d':
            max_d=min(3, global_stuff.cols-self.length-self.y+1)
            self.y+=max_d
            for ball in balls:
                if ball.isstuck():
                    ball.movestuckball(max_d)
        elif key=='a':
            max_d=self.y-max(0, self.y-3)
            self.y-=max_d
            for ball in balls:
                if ball.isstuck():
                    ball.movestuckball(-max_d)
    
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
