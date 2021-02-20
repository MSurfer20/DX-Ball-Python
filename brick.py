from powerup import PowerUp
from expandpaddle import expandpaddle
from shrinkpaddle import shrinkpaddle
from ballmultiplier import ballmultiplier
from fastball import fastball
from paddlegrab import paddlegrab
from thruball import thruball
# from global_stuff import power_array
import random

class brick:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.lvl=-1
    
    def reducelvl(self, board):
        self.lvl-=1
        if self.lvl==0:
            for y in range(0,6):
                for x in range(0,2):
                    board._board[self.x+x][self.y+y]=None
            return self.generate_powerup(self.x,self.y)
        return None
    
    def destroy(self, board):
        self.lvl=0
        for y in range(0,6):
            for x in range(0,2):
                board._board[self.x+x][self.y+y]=None
        return self.generate_powerup(self.x,self.y)
        
    
    def generate_powerup(self, x,y):
        num=random.randint(0,1)
        if num:
            return None
        num=random.randint(0,5)
        if num==0:
            return expandpaddle(x,y)
        elif num==1:
            return shrinkpaddle(x,y)
        elif num==2:
            return ballmultiplier(x,y)
        elif num==3:
            fastball(x,y)
        elif num==4:
            return paddlegrab(x,y)
        elif num==5:
            return thruball(x,y)
        
            
    
class brick1(brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lvl=1

class brick2(brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lvl=2

class brick3(brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lvl=3

class brick4(brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lvl=4

class brickfixed(brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lvl=10
    def reducelvl(self, board):
        return None

class explodingbrick(brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lvl=20
    def reducelvl(self, board):
        return self.destroy(board)
    def destroy(self, board):
        if not board._board[self.x][self.y]:
            return
        self.lvl=0
        board._board[self.x][self.y]=None
        if board._board[self.x+2][self.y+6]:
            board._board[self.x+2][self.y+6].destroy(board)
        if board._board[self.x][self.y+6]:
            board._board[self.x][self.y+6].destroy(board)
        for k in range(0,7):
            if board._board[self.x+2][self.y+k]:
                board._board[self.x+2][self.y+k].destroy(board)
        if board._board[self.x-1][self.y-1]:
            board._board[self.x-1][self.y-1].destroy(board)
        if board._board[self.x][self.y-1]:
            board._board[self.x][self.y-1].destroy(board)
        for k in range(0,7):
            if board._board[self.x-1][self.y+k]:
                board._board[self.x-1][self.y+k].destroy(board)
        return self.generate_powerup(self.x,self.y)
