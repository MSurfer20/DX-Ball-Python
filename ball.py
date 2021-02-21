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
        
        if self.ballfell():
            self.removeballs(board)
            return
        self.update_ball_position()
        if((self.x)<=0):
            self.topwallcollision()
        if((self.y)<=0 or (self.y)>=cols-1):
            self.sidewallcollision()
    
    def update_ball_position(self):
        self.x+=self.x_vel
        self.y+=self.y_vel
            
    def ballfell(self):
        if math.floor(self.x+self.x_vel)>=rows:
            return True
        return False

    def topwallcollision(self):
        self.reflect_x_velocity()
        if self.x<1:
            self.x=0
    
    def sidewallcollision(self):
        self.reflect_y_velocity()
        if self.y<1:
            self.y=0
        else:
            self.y=cols-1
    
    def removeballs(self, board):
        board._balls.remove(self)
        if len(board._balls) == 0:
            board.liveslost()
        
    def detectbrickcollision(self, board):
        x_dir=int(math.copysign(1,self.x_vel))
        y_dir=int(math.copysign(1,self.y_vel))
        curr_x=math.floor(self.x)
        curr_y=math.floor(self.y)
        if board.check_bricks(int(curr_x), int(curr_y+y_dir)):
            if self.fire:
                a=board._board[int(curr_x)][int(curr_y+y_dir)].destroy(board)
                if a:
                    board._powerups.append(a)
            else:
                self.reflect_y_velocity()
                a=board._board[int(curr_x)][int(curr_y+y_dir)].reducelvl(board)
                if a:
                    board._powerups.append(a)
        if board.check_bricks(int(curr_x+x_dir), int(curr_y)):
            if self.fire:
                a=board._board[int(curr_x+x_dir)][int(curr_y)].destroy(board)
                if a:
                    board._powerups.append(a)
            else:
                if board._board[int(curr_x+x_dir)][int(curr_y)] != board._board[int(curr_x)][int(curr_y+y_dir)]:
                    self.x_vel=self.x_vel*-1
                    a=board._board[int(curr_x+x_dir)][int(curr_y)].reducelvl(board)
                    if a:
                        board._powerups.append(a)
    
    def reflect_x_velocity(self):
        self.x_vel=self.x_vel*-1
    
    def reflect_y_velocity(self):
        self.y_vel=self.y_vel*-1
            
        
    def detectpaddlecollision(self, paddle):
        x_dir=int(math.copysign(1,self.x_vel))
        y_dir=int(math.copysign(1,self.y_vel))
        curr_x=math.floor(self.x)
        curr_y=math.floor(self.y)
        if x_dir==1 and curr_y>=paddle.y and curr_y<=paddle.y+paddle.length and curr_x==rows-2:
            self.reflect_x_velocity()
            val=paddle.y+(paddle.length)/2-curr_y
            self.y_vel=-val*0.5
            if paddle.stick:
                self.stuck=True

    
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
