import math
from global_stuff import *
import brick
from colorama import Fore, Style

class ball:
    def __init__(self, x, y, x_vel=-1, y_vel=1, stuck=True, fire=False):
        self.x=x
        self.y=y
        self.x_vel=x_vel
        self.y_vel=y_vel
        self.stuck=stuck
        self.fire=fire
        if fire:
            self.icon=Fore.RED+"\u2B24"+Style.RESET_ALL
        else:
            self.icon="\u2B24"

    def moveball(self, board):
        if self.stuck:
            return  
        if math.floor(self.x+self.x_vel)>=rows:
            board._balls.remove(self)
            return
        self.x+=self.x_vel
        self.y+=self.y_vel
        if((self.x)<=0):
            self.x_vel=self.x_vel*-1
            if self.x<1:
                self.x=0
        if((self.y)<=0 or (self.y)>=cols-1):
            self.y_vel=self.y_vel*-1
            if self.y<1:
                self.y=0
            else:
                self.y=cols-1
        
    def detectbrickcollision(self, board):
        x_dir=int(math.copysign(1,self.x_vel))
        y_dir=int(math.copysign(1,self.y_vel))
        curr_x=math.floor(self.x)
        curr_y=math.floor(self.y)
        if isinstance(board._board[int(curr_x+x_dir)][int(curr_y)], brick.brick) and board._board[int(curr_x+x_dir)][int(curr_y)].lvl>0:
            if self.fire:
                a=board._board[int(curr_x+x_dir)][int(curr_y)].destroy()
                if a:
                    board._powerups.append(a)
            else:
                self.x_vel=self.x_vel*-1
                a=board._board[int(curr_x+x_dir)][int(curr_y)].reducelvl()
                if a:
                    board._powerups.append(a)

        if isinstance(board._board[int(curr_x)][int(curr_y+y_dir)], brick.brick) and board._board[int(curr_x)][int(curr_y+y_dir)].lvl>0:
            if self.fire:
                a=board._board[int(curr_x)][int(curr_y+y_dir)].destroy()
                if a:
                    board._powerups.append(a)
            else:
                self.y_vel=self.y_vel*-1
                a=board._board[int(curr_x)][int(curr_y+y_dir)].reducelvl()
                if a:
                    board._powerups.append(a)
            
        if x_dir==1 and curr_y>=board._paddle.y and curr_y<=board._paddle.y+board._paddle.length and curr_x==rows-2:
            self.x_vel=self.x_vel*-1
            val=board._paddle.y+(board._paddle.length)/2-curr_y
            self.y_vel=-val*0.5
            if board._paddle.stick:
                self.stuck=True

    def detectpaddlecollision(self, paddle):
        pass
    
    def detectwallcollision(self):
        pass
    
    def movestuckball(self, key):
        if key=='d':
            self.y+=3
        elif key=='a':
            self.y-=3
    
    def releaseball(self):
            self.stuck=False 
    
    def setfire(self):
        self.fire=True
        self.icon=Fore.RED+"\u2B24"+Style.RESET_ALL
    
    def stopfire(self):
        self.fire=False
        self.icon="\u2B24"