from entity import entity
from powerup import PowerUp
from expandpaddle import expandpaddle
from shrinkpaddle import shrinkpaddle
from ballmultiplier import ballmultiplier
from fastball import fastball
from paddlegrab import paddlegrab
from thruball import thruball
import global_stuff
import random

class brick(entity):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.lvl=-1
    
    def reducelvl(self, board):
        self.lvl-=1
        if self.lvl==0:
            for y in range(0,6):
                board._board[self.x][self.y+y]=None
            self.increasescore(board)
            a=self.generate_powerup(self.x,self.y)
            if a:
                board.add_powerup(a)
    
    def destroy(self, board):
        self.lvl=0
        for y in range(0,6):
            board._board[self.x][self.y+y]=None
        self.increasescore(board)
        a=self.generate_powerup(self.x,self.y)
        if a:
            board.add_powerup()
    
    def increasescore(self, board): #overloaded
        pass
        
    
    def generate_powerup(self, x,y):
        num=random.randint(0,1)
        if num:
            return
        num=random.randint(0,5)
        if num==0:
            return expandpaddle(x,y)
        elif num==1:
            return shrinkpaddle(x,y)
        elif num==2:
            return ballmultiplier(x,y)
        elif num==3:
            return fastball(x,y)
        elif num==4:
            return paddlegrab(x,y)
        elif num==5:
            return thruball(x,y)
        
            
    
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

    def reducelvl(self, board):
        return None

    def increasescore(self, board):
        pass

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
        self.increasescore(board)
        board._board[self.x][self.y]=None
        if self.y+6<global_stuff.cols and board._board[self.x+1][self.y+6]:
            board._board[self.x+1][self.y+6].destroy(board)
        if self.y+6<global_stuff.cols and board._board[self.x][self.y+6]:
            board._board[self.x][self.y+6].destroy(board)
        for k in range(-1,7):
            if board._board[self.x+1][self.y+k]:
                board._board[self.x+1][self.y+k].destroy(board)
        if board._board[self.x-1][self.y-1]:
            board._board[self.x-1][self.y-1].destroy(board)
        if board._board[self.x][self.y-1]:
            board._board[self.x][self.y-1].destroy(board)
        for k in range(-1,7):
            if board._board[self.x-1][self.y+k]:
                board._board[self.x-1][self.y+k].destroy(board)
        a=self.generate_powerup(self.x,self.y)
        if a:
            board.add_powerup(a)
    
    def increasescore(self, board):
        board.increase_score(2.5)
