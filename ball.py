import math
from global_stuff import *
import global_stuff
import brick
from colorama import Fore, Style
from entity import entity
import time
import os
from playsound import playsound


class ball(entity):
    def __init__(self, x, y, x_vel=-1, y_vel=1, stuck=True, fire=False, fast_ball=1, gold=False):
        super().__init__(x,y)
        self.x_vel=x_vel
        self.y_vel=y_vel
        self.stuck=stuck
        self.fire=fire
        self.gold_ball=gold
        if fire:
            self.icon=Fore.RED+"\u2B24"+Style.RESET_ALL
        elif gold:
            self.icon=Fore.YELLOW+"\u2B24"+Style.RESET_ALL
        else:
            self.icon="\u2B24"
        self.fast_ball=fast_ball

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
        self.y+=self.y_vel*self.fast_ball
            
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
        if board.balls_remaining()==0:
            board.liveslost()
        
    def detectbrickcollision(self, board):
        x_dir=int(math.copysign(1,self.x_vel))
        y_dir=int(math.copysign(1,self.y_vel))
        curr_x=math.floor(self.x)
        curr_y=math.floor(self.y)
        if board.check_bricks(int(curr_x), int(curr_y+y_dir)):
            brick_x=board._board[int(curr_x)][int(curr_y+y_dir)].x
            brick_y=board._board[int(curr_x)][int(curr_y+y_dir)].y
            if self.gold_ball:
                os.system("aplay Explosion+1.mp3 &")
                board._board[int(curr_x)][int(curr_y+y_dir)].destroy(board, self)
                if brick_y+6<global_stuff.cols and board._board[brick_x+1][brick_y+6]:
                    board._board[brick_x+1][brick_y+6].destroy(board, self)
                if brick_y+6<global_stuff.cols and board._board[brick_x][brick_y+6]:
                    board._board[brick_x][brick_y+7].destroy(board, self)
                for k in range(-1,7):
                    if board._board[brick_x+1][brick_y+k]:
                        board._board[brick_x+1][brick_y+k].destroy(board, self)
                if board._board[brick_x-1][brick_y-1]:
                    board._board[brick_x-1][brick_y-1].destroy(board, self)
                if board._board[brick_x][brick_y-1]:
                    board._board[brick_x][brick_y-1].destroy(board, self)
                for k in range(-1,7):
                    if board._board[brick_x-1][brick_y+k]:
                        board._board[brick_x-1][brick_y+k].destroy(board, self)
                if not self.fire:
                    self.reflect_y_velocity()
                
                # a=self.generate_powerup(brick_x,brick_y, ball.x_vel, ball.y_vel)
                # if a:
                #     board.add_powerup(a)
            
            elif self.fire:
                board._board[int(curr_x)][int(curr_y+y_dir)].destroy(board, self)
            else:
                # if time.time()-board.level_time>10:
                os.system("aplay brickwall.wav &")
                board._board[int(curr_x)][int(curr_y+y_dir)].reducelvl(board, self)
                self.reflect_y_velocity()
           
                
        if board.check_bricks(int(curr_x+x_dir), int(curr_y)) and not board.check_bricks(int(curr_x), int(curr_y)):
            brick_x=board._board[int(curr_x+x_dir)][int(curr_y)].x
            brick_y=board._board[int(curr_x+x_dir)][int(curr_y)].y
            if self.gold_ball:
                os.system("aplay Explosion+1.mp3 &")
                board._board[int(curr_x+x_dir)][int(curr_y)].destroy(board, self)
                if brick_y+6<global_stuff.cols and board._board[brick_x+1][brick_y+6]:
                    board._board[brick_x+1][brick_y+6].destroy(board, self)
                if brick_y+6<global_stuff.cols and board._board[brick_x][brick_y+6]:
                    board._board[brick_x][brick_y+6].destroy(board, self)
                for k in range(-1,7):
                    if board._board[brick_x+1][brick_y+k]:
                        board._board[brick_x+1][brick_y+k].destroy(board, self)
                if board._board[brick_x-1][brick_y-1]:
                    board._board[brick_x-1][brick_y-1].destroy(board, self)
                if board._board[brick_x][brick_y-1]:
                    board._board[brick_x][brick_y-1].destroy(board, self)
                for k in range(-1,7):
                    if board._board[brick_x-1][brick_y+k]:
                        board._board[brick_x-1][brick_y+k].destroy(board, self)
                # if board._board[int(curr_x+x_dir)][int(curr_y)] != board._board[int(curr_x)][int(curr_y+y_dir)]:
                if not self.fire:
                    self.reflect_x_velocity()
                
                # a=board._board[int(curr_x+x_dir)][int(curr_y)].generate_powerup(brick_x,brick_y, ball.x_vel, ball.y_vel)
                # if a:
                    # board.add_powerup(a)
            elif self.fire:
                board._board[int(curr_x+x_dir)][int(curr_y)].destroy(board, self)
            else:
                if board._board[int(curr_x+x_dir)][int(curr_y)] != board._board[int(curr_x)][int(curr_y+y_dir)]:
                    # if time.time()-board.level_time>10:
                    os.system("aplay brickwall.wav &")
                    board._board[int(curr_x+x_dir)][int(curr_y)].reducelvl(board, self)
                    self.reflect_x_velocity()
            
    
    def reflect_x_velocity(self):
        self.x_vel=self.x_vel*-1
    
    def reflect_y_velocity(self):
        self.y_vel=self.y_vel*-1
            
        
    def detectpaddlecollision(self, paddle, board):
        x_dir=int(math.copysign(1,self.x_vel))
        y_dir=int(math.copysign(1,self.y_vel))
        curr_x=math.floor(self.x)
        curr_y=math.floor(self.y)
        if x_dir==1 and curr_y>=paddle.get_left_coor() and curr_y<=paddle.get_right_coor() and curr_x==rows-2:
            self.reflect_x_velocity()
            if time.time()-board.level_time>=30 and board.ufo is None:
                board.fallbricks()
            dist_from_centre=paddle.get_left_coor()+(paddle.get_length())/2-curr_y
            factor_change=math.floor(dist_from_centre/2.5)
            self.y_vel=-factor_change*0.5
            if paddle.isstick():
                self.stuck=True
            else:
                os.system("aplay bounce.wav &")

    
    def movestuckball(self, dist):
        self.y+=dist
    
    def releaseball(self):
        self.stuck=False 
    
    def setfire(self):
        self.fire=True
        self.icon=Fore.RED+"\u2B24"+Style.RESET_ALL
    
    def stopfire(self):
        self.fire=False
        if self.gold_ball:
            self.icon=Fore.YELLOW+"\u2B24"+Style.RESET_ALL
        else:
            self.icon="\u2B24"
    
    def setgold(self):
        self.gold_ball=True
        self.icon=Fore.YELLOW+"\u2B24"+Style.RESET_ALL
    
    def stopgold(self):
        self.gold_ball=False
        if self.fire:
            self.icon=Fore.RED+"\u2B24"+Style.RESET_ALL
        else:
            self.icon="\u2B24"

    def isstuck(self):
        return self.stuck

    def increase_ball_velocity(self):
        self.fast_ball=2
    
    def decrease_ball_velocity(self):
        self.fast_ball=1

    def detectufocollision(self, ufo, board):
        if not ufo:
            return
        x_dir=int(math.copysign(1,self.x_vel))
        y_dir=int(math.copysign(1,self.y_vel))
        curr_x=math.floor(self.x)
        curr_y=math.floor(self.y)
        flag=0
        if ufo.check(int(curr_x), int(curr_y+y_dir)):
                # if time.time()-board.level_time>10:
            ufo.reducelvl()
            board.increase_score(30)
            if ufo.health==70:
                board.spawnblocks1()
                pass
            if ufo.health==40:
                board.spawnblocks2()
            if ufo.health==0:
                board.game_on=2
            os.system("aplay bounce.wav &")
            flag=1
            if self.y-ufo.y>ufo.y+ufo.length-self.y:
                self.y_vel=abs(self.y_vel)
                self.y=ufo.y+ufo.length+1
            else:
                self.y_vel=-(abs(self.y_vel))
                self.y=ufo.y-1
        elif ufo.check(int(curr_x+x_dir), int(curr_y)):
                # if time.time()-board.level_time>10:
            os.system("aplay bounce.wav &")
            if flag==0:
                ufo.reducelvl()
                board.increase_score(30)
                if ufo.health==70:
                    board.spawnblocks1()
                    pass
                if ufo.health==40:
                    board.spawnblocks2()
            self.reflect_x_velocity()
