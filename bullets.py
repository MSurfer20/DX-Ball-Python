import math
from global_stuff import *
import brick
from colorama import Fore, Style
from entity import entity

class bullet(entity):
    def __init__(self, x, y, x_vel=-1, y_vel=0):
        super().__init__(x,y)
        self.x_vel=x_vel
        self.y_vel=y_vel

    def moveball(self, board):
        
        self.update_ball_position()
        if((self.x)<=0):
            board._bullets.remove(self)
        # if((self.y)<=0 or (self.y)>=cols-1):
        #     self.sidewallcollision()
    
    def update_ball_position(self):
        self.x+=self.x_vel
    
    def checkcollision(self, board):
        if board.check_bricks(int((self.x)-1), int((self.y))):
            board._board[int((self.x)-1)][int((self.y))].reducelvl(board, self)
            board._bullets.remove(self)
            
    # def detectbrickcollision(self, board):
    #     x_dir=int(math.copysign(1,self.x_vel))
    #     y_dir=int(math.copysign(1,self.y_vel))
    #     curr_x=math.floor(self.x)
    #     curr_y=math.floor(self.y)
    #     if board.check_bricks(int(curr_x), int(curr_y+y_dir)):
    #         if self.fire:
    #             board._board[int(curr_x)][int(curr_y+y_dir)].destroy(board, self)
    #         else:
    #             # if time.time()-board.level_time>10:
    #             # if True:
    #             #     board.fallbricks()
    #             board._board[int(curr_x)][int(curr_y+y_dir)].reducelvl(board, self)
    #             self.reflect_y_velocity()
    #     if board.check_bricks(int(curr_x+x_dir), int(curr_y)) and not board.check_bricks(int(curr_x), int(curr_y)):
    #         if self.fire:
    #             board._board[int(curr_x+x_dir)][int(curr_y)].destroy(board, self)
    #         else:
    #             if board._board[int(curr_x+x_dir)][int(curr_y)] != board._board[int(curr_x)][int(curr_y+y_dir)]:
    #                 # if time.time()-board.level_time>10:
    #                 # if True:
    #                 #     board.fallbricks()
    #                 board._board[int(curr_x+x_dir)][int(curr_y)].reducelvl(board, self)
    #                 self.reflect_x_velocity()
    
    # def reflect_x_velocity(self):
    #     self.x_vel=self.x_vel*-1
    
    # def reflect_y_velocity(self):
    #     self.y_vel=self.y_vel*-1
            
        
    # def detectpaddlecollision(self, paddle):
    #     x_dir=int(math.copysign(1,self.x_vel))
    #     y_dir=int(math.copysign(1,self.y_vel))
    #     curr_x=math.floor(self.x)
    #     curr_y=math.floor(self.y)
    #     if x_dir==1 and curr_y>=paddle.get_left_coor() and curr_y<=paddle.get_right_coor() and curr_x==rows-2:
    #         self.reflect_x_velocity()
    #         dist_from_centre=paddle.get_left_coor()+(paddle.get_length())/2-curr_y
    #         factor_change=math.floor(dist_from_centre/2.5)
    #         self.y_vel=-factor_change*0.5
    #         if paddle.isstick():
    #             self.stuck=True

    
    # def movestuckball(self, dist):
    #     self.y+=dist
    
    # def releaseball(self):
    #     self.stuck=False 
    
    # def setfire(self):
    #     self.fire=True
    #     self.icon=Fore.RED+"\u2B24"+Style.RESET_ALL
    
    # def stopfire(self):
    #     self.fire=False
    #     self.icon="\u2B24"

    # def isstuck(self):
    #     return self.stuck
