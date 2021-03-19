from entity import entity
from powerup import PowerUp
from expandpaddle import expandpaddle
from shrinkpaddle import shrinkpaddle
from ballmultiplier import ballmultiplier
from fastball import fastball
from paddlegrab import paddlegrab
from thruball import thruball
from laser import laser
from fireball import fireball
import global_stuff
import random
import os

class brick(entity):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.lvl=-1
    
    def reducelvl(self, board, ball):
        self.lvl-=1
        if self.lvl==0:
            for y in range(0,6):
                board._board[self.x][self.y+y]=None
            self.increasescore(board)
            if board.ufo:
                return
            a=self.generate_powerup(self.x,self.y, ball.x_vel, ball.y_vel)
            if a:
                board.add_powerup(a)
    
    def destroy(self, board, ball):
        self.lvl=0
        for y in range(0,6):
            board._board[self.x][self.y+y]=None
        self.increasescore(board)
        a=self.generate_powerup(self.x,self.y, ball.x_vel, ball.y_vel)
        if a:
            board.add_powerup(a)
    
    def increasescore(self, board): #overloaded
        pass
    
    def generate_powerup(self, x,y, x_vel, y_vel):
        num=random.randint(0,1)
        if num:
            return
        num=random.randint(0,7)
        # num=7
        if num==0:
            return expandpaddle(x,y, x_vel, y_vel)
        elif num==1:
            return shrinkpaddle(x,y,x_vel,y_vel)
        elif num==2:
            return ballmultiplier(x,y,x_vel,y_vel)
        elif num==3:
            return fastball(x,y,x_vel,y_vel)
        elif num==4:
            return paddlegrab(x,y,x_vel,y_vel)
        elif num==5:
            return thruball(x,y,x_vel,y_vel)
        elif num==6:
            return laser(x,y,x_vel,y_vel)
        elif num==7:
            return fireball(x, y, x_vel, y_vel)
        
            
    
class brick1(brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lvl=1

    def increasescore(self, board):
        board.increase_score(5)
    
class brick2(brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lvl=2

    def increasescore(self, board):
        board.increase_score(10)


class brick3(brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lvl=3

    def increasescore(self, board):
        # board.score+=15
        board.increase_score(15)


class brick4(brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lvl=4

    def increasescore(self, board):
        # board.score+=20
        board.increase_score(20)


class brickfixed(brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lvl=10

    def reducelvl(self, board, ball):
        return None

    def increasescore(self, board):
        pass

class explodingbrick(brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lvl=20

    def reducelvl(self, board, ball):
        os.system("aplay Explosion.wav &")
        return self.destroy(board, ball)

    def destroy(self, board, ball):
        if not board._board[self.x][self.y]:
            return
        self.lvl=0
        self.increasescore(board)
        board._board[self.x][self.y]=None
        if self.y+6<global_stuff.cols and board._board[self.x+1][self.y+6]:
            board._board[self.x+1][self.y+6].destroy(board, ball)
        if self.y+6<global_stuff.cols and board._board[self.x][self.y+6]:
            board._board[self.x][self.y+6].destroy(board, ball)
        for k in range(-1,7):
            if board._board[self.x+1][self.y+k]:
                board._board[self.x+1][self.y+k].destroy(board, ball)
        if board._board[self.x-1][self.y-1]:
            board._board[self.x-1][self.y-1].destroy(board, ball)
        if board._board[self.x][self.y-1]:
            board._board[self.x][self.y-1].destroy(board, ball)
        for k in range(-1,7):
            if board._board[self.x-1][self.y+k]:
                board._board[self.x-1][self.y+k].destroy(board, ball)
        a=self.generate_powerup(self.x,self.y, ball.x_vel, ball.y_vel)
        if a:
            board.add_powerup(a)
    
    def increasescore(self, board):
        board.increase_score(2.5)

class colorchangingbrick(brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lvl=3
        self.hit=0

    def increasescore(self, board):
        # board.score+=20
        board.increase_score(20)
    
    def changecolor(self):
        if self.hit==0:
            self.lvl=random.randint(1,4)
    
    def reducelvl(self, board, ball):
        self.hit=1
        super().reducelvl(board, ball)
    
    def destroy(self, board, ball):
        super().destroy(board, ball)
        self.hit=1

class defencebrick(brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lvl=2
        self.hit=0
    def increasescore(self, board):
        # board.score+=20
        board.increase_score(20)
    
    def reducelvl(self, board, ball):
        self.lvl-=1
        if self.lvl==0:
            for y in range(0,6):
                board._board[self.x][self.y+y]=None
            self.increasescore(board)