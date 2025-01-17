import numpy as np
import brick
from os import system
from paddle import paddle
from ball import ball
import math
import random
import global_stuff
from colorama import Fore, Style, Style
import sys
import time
import datetime
from bullets import bullet
from ufo import ufo
from ufo_ascii import ufo_ascii
from bombs import bomb
from laser import laser
import os


class board():
    def __init__(self, rows, columns, score=0, strttime=0, lives_left=10):
        self._rows=rows
        self._columns=columns
        self._board = np.empty(shape=(rows+1, columns+1), dtype=np.object)
        self._paddle = paddle(rows-1,columns/2)
        posn=random.randint(int(self._paddle.y), int(self._paddle.y+self._paddle.length))
        dist_from_centre=self._paddle.get_left_coor()+(self._paddle.get_length())/2-posn
        factor_change=math.floor(dist_from_centre/2.5)
        y_vel=-factor_change*0.5
        self._balls = [ball(rows-2, posn, -1, y_vel)]
        self._powerups =[]
        self.score=score
        self.remaining_lives=lives_left
        if strttime==0:
            self.start_time=time.time()
        else:
            self.start_time=strttime
        self.game_on=1
        self.level_time=time.time()
        self._bullets=[]
        self.max_score=0
        self.ufo=None
        self.bombs=[]
        self.frame_no=0
    
    def getdim(self):
        return (self._rows, self._columns)
    
    def get_brick(self, x, y, typ):
        if typ==0:
            self.max_score+=5
            return brick.brick1(x,y)
        elif typ==1:
            self.max_score+=10
            return  brick.brick2(x,y)
        elif typ==2:
            self.max_score+=15
            return brick.brick3(x,y)
        elif typ==3:
            self.max_score+=20
            return brick.brick4(x,y)
        elif typ==4:
            return brick.brickfixed(x,y)
        elif typ==5:
            self.max_score+=20
            return brick.explodingbrick(x,y)
        elif typ==6:
            return None
        elif typ==7:
            self.max_score+=20
            return brick.colorchangingbrick(x,y)
    
    # def createlevel2(self):
    #     for x in range(6, 22, 2):
    #         y=1
    #         while y<116:
    #             if self._board[x][y]:
    #                 y+=1
    #                 continue
    #             ob=self.get_random_brick(x,y)
    #             for k in range(0,6):
    #                 for h in range(0,2):
    #                     self._board[x+h][y+k]=ob
    #             if ob:
    #                 y+=5
    #             else:
    #                 y+=1
        
    #     self.max_score=1000
        # self.insertspecblocks()
    
    # def insertspecblocks(self):
    #     ob=brick.explodingbrick(20,45)
    #     for k in range(0,2):
    #         self._board[20+k][45]=self._board[20+k][46]=self._board[20+k][47]=self._board[20+k][48]=ob
    
    # def createlevel3(self):
    #     # arr=[[0,0,5], [2,6,5], [4, 12, 5], [6,18,5],]
    #     arr=[[16, 6, 1], [16, 18, 2], [16, 24, 3], [16, 30, 4], [16, 42, 3], [16, 48, 4], [16, 54, 1], [16, 60, 4], [16, 66, 1], [16, 72, 2], [16, 78, 3], [16, 84, 4], [16, 90, 0], [16, 96, 1], [16, 102, 2], [16, 108, 3], [16, 114, 4]]
    #     arr+=[ [2, 18, 3], [2, 24, 2], [2, 30, 4], [2, 42, 4], [2, 48, 1], [2, 54, 0], [2, 60, 1], [2, 66, 2], [2, 72, 4], [2, 78, 1], [2, 84, 0], [2, 90, 4], [2, 96, 3], [2, 102, 4], [2, 108, 2], [2, 114, 1]]
    #     arr+=[[2,30,5],[2,36,5],[2,42,5],[4,36,5],[2,42,5],[2,48,5]]
    #     arr+=[[4, 6, 3], [4, 18, 4], [4, 24, 2], [4, 30, 3], [4, 42, 2], [4, 48, 0], [4, 54, 4], [4, 60, 4], [4, 66, 2], [4, 72, 1], [4, 78, 2], [4, 84, 4], [4, 90, 2], [4, 96, 4], [4, 102, 3], [4, 108, 4], [4, 114, 1], [6, 6, 4], [6, 24, 0], [6, 30, 1], [6, 42, 1], [6, 48, 4], [6, 54, 3], [6, 60, 0], [6, 66, 1], [6, 72, 2], [6, 78, 2], [6, 84, 4], [6, 90, 4], [6, 96, 0], [6, 102, 1], [6, 108, 0], [6, 114, 2], [8, 6, 0], [8, 18, 3], [8, 24, 0], [8, 30, 0], [8, 42, 0], [8, 48, 4], [8, 54, 1], [8, 60, 1], [8, 66, 4], [8, 72, 2], [8, 78, 1], [8, 84, 4], [8, 90, 1], [8, 96, 2], [8, 102, 0], [8, 108, 4], [8, 114, 4], [10, 6, 1], [10, 18, 2], [10, 24, 4], [10, 30, 4], [10, 42, 4], [10, 48, 2], [10, 54, 0], [10, 60, 3], [10, 66, 0], [10, 72, 2], [10, 78, 2], [10, 84, 3], [10, 90, 0], [10, 96, 0], [10, 102, 3], [10, 108, 0], [10, 114, 3], [12, 6, 2], [12, 18, 3], [12, 24, 3], [12, 30, 2], [12, 42, 0], [12, 48, 0], [12, 54, 0], [12, 60, 2], [12, 66, 4], [12, 72, 4], [12, 78, 1], [12, 84, 1], [12, 90, 0], [12, 96, 2], [12, 102, 1], [12, 108, 2], [12, 114, 1], [14, 6, 2], [14, 18, 1], [14, 24, 3], [14, 30, 1], [14, 42, 3], [14, 48, 3], [14, 54, 2], [14, 60, 3], [14, 66, 2], [14, 72, 4], [14, 78, 3], [14, 84, 4], [14, 90, 0], [14, 96, 3], [14, 102, 1], [14, 108, 3], [14, 114, 3]]
    #     arr+=[[2, 6, 5], [4, 12, 5], [6, 18, 5], [8, 24, 5], [10, 30, 5], [12, 36, 5], [14, 36, 5]]
    #     for typ in arr:
    #         ob=self.get_brick(typ[0],typ[1],typ[2])
    #         for a in range(0,6):
    #                 self._board[typ[0]][typ[1]+a]=ob
    
    def createlevel1(self):
        arr=[[4, 18, 2], [4, 24, 0], [4, 30, 2], [4, 36, 1], [4, 42, 2], [4, 48, 1], [6, 18, 1], [6, 24, 1], [6, 30, 1], [6, 36, 2], [6, 42, 2], [6, 48, 2], [8, 18, 2], [8, 24, 2], [8, 30, 1], [8, 36, 4], [8, 42, 2], [8, 48, 3], [10, 18, 3], [10, 24, 4], [10, 30, 3], [10, 36, 1], [10, 42, 2], [10, 48, 3], [12, 18, 1], [12, 24, 3], [12, 30, 1], [12, 36, 0], [12, 42, 1], [12, 48, 0], [14, 18, 4], [14, 24, 0], [14, 30, 2], [14, 36, 3], [14, 42, 0], [14, 48, 7]]
        arr+=[[4, 60, 7], [4, 66, 2], [4, 72, 0], [4, 78, 2], [4, 84, 0], [4, 90, 2], [6, 60, 0], [6, 66, 0], [6, 72, 0], [6, 78, 0], [6, 84, 0], [6, 90, 0], [8, 60, 4], [8, 66, 2], [8, 72, 0], [8, 78, 1], [8, 84, 4], [8, 90, 2], [10, 60, 0], [10, 66, 1], [10, 72, 2], [10, 78, 3], [10, 84, 4], [10, 90, 0], [12, 60, 0], [12, 66, 1], [12, 72, 0], [12, 78, 1], [12, 84, 0], [12, 90, 1], [14, 60, 4], [14, 66, 0], [14, 72, 2], [14, 78, 3], [14, 84, 0], [14, 90, 1]]
        arr+=[[4, 102, 2], [4, 108, 1], [4, 114, 0], [4, 120, 7], [6, 102, 2], [6, 108, 0], [6, 114, 0], [6, 120, 0], [8, 102, 0], [8, 108, 2], [8, 114, 1], [8, 120, 0], [10, 102, 0], [10, 108, 1], [10, 114, 0], [10, 120, 0], [12, 102, 2], [12, 108, 4], [12, 114, 0], [12, 120, 1], [14, 102, 4], [14, 108, 2], [14, 114, 0], [14, 120, 1]]
        arr+=[[4,18,5],[4,24,5],[5,24,5],[6,30,5],[7,36,5],[8,36,5]]
        arr+=[[10,36,5],[11,36,5],[12,30,5],[13,24,5],[14,24,5],[15,18,5]]
        for typ in arr:
            ob=self.get_brick(typ[0],typ[1],typ[2])
            for a in range(0,6):
                    self._board[typ[0]][typ[1]+a]=ob
        self.max_score=865
    
    def createlevel5(self):
        self.ufo=ufo(4, self._paddle.y)
        arr=[[12, 18, 4], [12, 30, 4], [14, 32, 4], [14, 54, 4], [14, 100, 4], [14, 110, 4], [18, 4, 4], [18, 16, 4], [18, 30, 4], [18, 48, 4], [19, 62, 4], [21, 100, 4], [19, 3, 4], [19, 90, 4], [14, 100, 4]]
        for typ in arr:
            ob=self.get_brick(typ[0],typ[1],typ[2])
            for a in range(0,6):
                    self._board[typ[0]][typ[1]+a]=ob
        self.max_score=1000000000000000000000

    def createlevel6(self):
        # arr=[[4, 18, 2], [4, 24, 0], [4, 30, 2], [4, 36, 1], [4, 42, 2], [4, 48, 1], [6, 18, 1], [6, 24, 1], [6, 30, 1], [6, 36, 2], [6, 42, 2], [6, 48, 2], [8, 18, 2], [8, 24, 2], [8, 30, 1], [8, 36, 4], [8, 42, 2], [8, 48, 3], [10, 18, 3], [10, 24, 4], [10, 30, 3], [10, 36, 1], [10, 42, 2], [10, 48, 3], [12, 18, 1], [12, 24, 3], [12, 30, 1], [12, 36, 0], [12, 42, 1], [12, 48, 0], [14, 18, 4], [14, 24, 0], [14, 30, 2], [14, 36, 3], [14, 42, 0], [14, 48, 7]]
        # arr+=[[4, 60, 7], [4, 66, 2], [4, 72, 0], [4, 78, 2], [4, 84, 0], [4, 90, 2], [6, 60, 0], [6, 66, 0], [6, 72, 0], [6, 78, 0], [6, 84, 0], [6, 90, 0], [8, 60, 4], [8, 66, 2], [8, 72, 0], [8, 78, 1], [8, 84, 4], [8, 90, 2], [10, 60, 0], [10, 66, 1], [10, 72, 2], [10, 78, 3], [10, 84, 4], [10, 90, 0], [12, 60, 0], [12, 66, 1], [12, 72, 0], [12, 78, 1], [12, 84, 0], [12, 90, 1], [14, 60, 4], [14, 66, 0], [14, 72, 2], [14, 78, 3], [14, 84, 0], [14, 90, 1]]
        # arr+=[[4, 102, 2], [4, 108, 1], [4, 114, 0], [4, 120, 7], [6, 102, 2], [6, 108, 0], [6, 114, 0], [6, 120, 0], [8, 102, 0], [8, 108, 2], [8, 114, 1], [8, 120, 0], [10, 102, 0], [10, 108, 1], [10, 114, 0], [10, 120, 0], [12, 102, 2], [12, 108, 4], [12, 114, 0], [12, 120, 1], [14, 102, 4], [14, 108, 2], [14, 114, 0], [14, 120, 1]]
        # arr+=[[4,18,5],[4,24,5],[5,24,5],[6,30,5],[7,36,5],[8,36,5]]
        # arr+=[[10,36,5],[11,36,5],[12,30,5],[13,24,5],[14,24,5],[15,18,5]]
        # arr=[[6, 6, 2], [6, 12, 2], [6, 18, 2], [6, 24, 2], [6, 30, 2], [6, 36, 2], [6, 42, 2], [6, 48, 2], [6, 54, 2], [6, 60, 2], [7, 6, 2], [7, 12, 2], [7, 18, 2], [7, 24, 2], [7, 30, 2], [7, 36, 2], [7, 42, 2], [7, 48, 2], [7, 54, 2], [7, 60, 2], [8, 6, 2], [8, 12, 2], [8, 18, 2], [8, 24, 2], [8, 30, 2], [8, 36, 2], [8, 42, 2], [8, 48, 2], [8, 54, 2], [8, 60, 2], [9, 6, 2], [9, 12, 2], [9, 18, 2], [9, 24, 2], [9, 30, 2], [9, 36, 2], [9, 42, 2], [9, 48, 2], [9, 54, 2], [9, 60, 2], [10, 6, 2], [10, 12, 2], [10, 18, 2], [10, 24, 2], [10, 30, 2], [10, 36, 2], [10, 42, 2], [10, 48, 2], [10, 54, 2], [10, 60, 2], [11, 6, 2], [11, 12, 2], [11, 18, 2], [11, 24, 2], [11, 30, 2], [11, 36, 2], [11, 42, 2], [11, 48, 2], [11, 54, 2], [11, 60, 2], [12, 6, 2], [12, 12, 2], [12, 18, 2], [12, 24, 2], [12, 30, 2], [12, 36, 2], [12, 42, 2], [12, 48, 2], [12, 54, 2], [12, 60, 2], [13, 6, 2], [13, 12, 2], [13, 18, 2], [13, 24, 2], [13, 30, 2], [13, 36, 2], [13, 42, 2], [13, 48, 2], [13, 54, 2], [13, 60, 2], [14, 6, 2], [14, 12, 2], [14, 18, 2], [14, 24, 2], [14, 30, 2], [14, 36, 2], [14, 42, 2], [14, 48, 2], [14, 54, 2], [14, 60, 2], [15, 6, 2], [15, 12, 2], [15, 18, 2], [15, 24, 2], [15, 30, 2], [15, 36, 2], [15, 42, 2], [15, 48, 2], [15, 54, 2], [15, 60, 2], [16, 6, 2], [16, 12, 2], [16, 18, 2], [16, 24, 2], [16, 30, 2], [16, 36, 2], [16, 42, 2], [16, 48, 2], [16, 54, 2], [16, 60, 2], [17, 6, 2], [17, 12, 2], [17, 18, 2], [17, 24, 2], [17, 30, 2], [17, 36, 2], [17, 42, 2], [17, 48, 2], [17, 54, 2], [17, 60, 2]]
        arr=[[6, 6, 0], [6, 12, 3], [6, 18, 1], [6, 24, 7], [6, 30, 4], [6, 36, 3], [6, 42, 0], [6, 48, 7], [6, 54, 4], [6, 60, 1], [7, 6, 1], [7, 12, 4], [7, 18, 2], [7, 24, 2], [7, 30, 4], [7, 36, 0], [7, 42, 7], [7, 48, 1], [7, 54, 2], [7, 60, 7], [8, 6, 0], [8, 12, 0], [8, 18, 1], [8, 24, 7], [8, 30, 3], [8, 36, 4], [8, 42, 3], [8, 48, 2], [8, 54, 4], [8, 60, 3], [9, 6, 3], [9, 12, 4], [9, 18, 0], [9, 24, 1], [9, 30, 2], [9, 36, 0], [9, 42, 2], [9, 48, 2], [9, 54, 0], [9, 60, 1], [10, 6, 1], [10, 12, 2], [10, 18, 0], [10, 24, 7], [10, 30, 1], [10, 36, 0], [10, 42, 0], [10, 48, 4], [10, 54, 4], [10, 60, 0], [11, 6, 3], [11, 12, 3], [11, 18, 2], [11, 24, 0], [11, 30, 1], [11, 36, 7], [11, 42, 2], [11, 48, 0], [11, 54, 3], [11, 60, 2], [12, 6, 3], [12, 12, 1], [12, 18, 7], [12, 24, 3], [12, 30, 3], [12, 36, 2], [12, 42, 1], [12, 48, 3], [12, 54, 7], [12, 60, 2], [13, 6, 0], [13, 12, 3], [13, 18, 4], [13, 24, 4], [13, 30, 3], [13, 36, 7], [13, 42, 0], [13, 48, 2], [13, 54, 2], [13, 60, 2], [14, 6, 0], [14, 12, 3], [14, 18, 7], [14, 24, 2], [14, 30, 3], [14, 36, 2], [14, 42, 1], [14, 48, 7], [14, 54, 0], [14, 60, 2], [15, 6, 3], [15, 12, 1], [15, 18, 7], [15, 24, 4], [15, 30, 0], [15, 36, 1], [15, 42, 4], [15, 48, 4], [15, 54, 2], [15, 60, 1], [16, 6, 4], [16, 12, 0], [16, 18, 7], [16, 24, 7], [16, 30, 7], [16, 36, 0], [16, 42, 0], [16, 48, 0], [16, 54, 1], [16, 60, 0], [17, 6, 7], [17, 12, 0], [17, 18, 0], [17, 24, 1], [17, 30, 3], [17, 36, 1], [17, 42, 2], [17, 48, 2], [17, 54, 2], [17, 60, 0]]
        arr+=[[6, 72, 0], [6, 78, 1], [6, 84, 4], [6, 90, 0], [6, 96, 3], [6, 102, 1], [6, 108, 2], [6, 114, 4], [6, 120, 3], [6, 126, 3], [7, 72, 3], [7, 78, 4], [7, 84, 4], [7, 90, 4], [7, 96, 0], [7, 102, 7], [7, 108, 3], [7, 114, 7], [7, 120, 4], [7, 126, 2], [8, 72, 3], [8, 78, 7], [8, 84, 2], [8, 90, 7], [8, 96, 0], [8, 102, 2], [8, 108, 2], [8, 114, 1], [8, 120, 7], [8, 126, 3], [9, 72, 1], [9, 78, 1], [9, 84, 3], [9, 90, 2], [9, 96, 2], [9, 102, 4], [9, 108, 0], [9, 114, 1], [9, 120, 4], [9, 126, 3], [10, 72, 1], [10, 78, 0], [10, 84, 3], [10, 90, 3], [10, 96, 2], [10, 102, 2], [10, 108, 1], [10, 114, 2], [10, 120, 4], [10, 126, 7], [11, 72, 7], [11, 78, 4], [11, 84, 0], [11, 90, 1], [11, 96, 1], [11, 102, 1], [11, 108, 2], [11, 114, 1], [11, 120, 3], [11, 126, 7], [12, 72, 4], [12, 78, 7], [12, 84, 4], [12, 90, 2], [12, 96, 1], [12, 102, 4], [12, 108, 2], [12, 114, 4], [12, 120, 0], [12, 126, 0], [13, 72, 1], [13, 78, 4], [13, 84, 2], [13, 90, 2], [13, 96, 7], [13, 102, 2], [13, 108, 7], [13, 114, 4], [13, 120, 0], [13, 126, 4], [14, 72, 4], [14, 78, 3], [14, 84, 1], [14, 90, 3], [14, 96, 4], [14, 102, 0], [14, 108, 1], [14, 114, 1], [14, 120, 1], [14, 126, 0], [15, 72, 7], [15, 78, 7], [15, 84, 1], [15, 90, 3], [15, 96, 3], [15, 102, 4], [15, 108, 4], [15, 114, 2], [15, 120, 2], [15, 126, 0], [16, 72, 7], [16, 78, 0], [16, 84, 3], [16, 90, 0], [16, 96, 0], [16, 102, 7], [16, 108, 4], [16, 114, 1], [16, 120, 1], [16, 126, 7], [17, 72, 4], [17, 78, 2], [17, 84, 0], [17, 90, 0], [17, 96, 7], [17, 102, 1], [17, 108, 1], [17, 114, 2], [17, 120, 2], [17, 126, 1]]
        self.max_score=self.score
        for typ in arr:
            ob=self.get_brick(typ[0],typ[1],typ[2])
            for a in range(0,6):
                    self._board[typ[0]][typ[1]+a]=ob
    
    def createlevel7(self):
        arr=[[6, 6, 0], [6, 12, 3], [6, 18, 1], [6, 24, 7], [6, 30, 4], [6, 36, 3], [6, 42, 0], [6, 48, 7], [7, 12, 4], [7, 18, 2], [6, 54, 4], [6, 60, 1], [8, 6, 0], [8, 12, 0], [8, 18, 1], [8, 24, 7], [8, 30, 3], [8, 36, 4], [8, 42, 3], [8, 48, 2], [8, 54, 4], [8, 60, 3], [10, 6, 1], [10, 12, 2], [10, 18, 0], [10, 24, 7], [10, 30, 1], [10, 36, 0], [10, 42, 0], [10, 48, 4], [10, 54, 4], [10, 60, 0], [12, 6, 3], [12, 12, 1], [12, 18, 7], [12, 24, 3], [12, 30, 3], [12, 36, 2], [12, 42, 1], [12, 48, 3], [12, 54, 7], [12, 60, 2], [14, 6, 0], [14, 12, 3], [14, 18, 7], [14, 24, 2], [14, 30, 3], [14, 36, 2], [14, 42, 1], [14, 48, 7], [14, 54, 0], [14, 60, 2], [16, 6, 4], [16, 12, 0], [16, 18, 7], [16, 24, 7], [16, 30, 7], [16, 36, 0], [16, 42, 0], [16, 48, 0], [16, 54, 1], [16, 60, 0], [6, 72, 0], [6, 78, 1], [6, 84, 4], [6, 90, 0], [6, 96, 3], [6, 102, 1], [6, 108, 2], [6, 114, 4], [6, 120, 3], [6, 126, 3], [8, 72, 3], [8, 78, 7], [8, 84, 2], [8, 90, 7], [8, 96, 0], [8, 102, 2], [8, 108, 2], [8, 114, 1], [8, 120, 7], [8, 126, 3], [10, 72, 1], [10, 78, 0], [10, 84, 3], [10, 90, 3], [10, 96, 2], [10, 102, 2], [10, 108, 1], [10, 114, 2], [10, 120, 4], [10, 126, 7], [12, 72, 4], [12, 78, 7], [12, 84, 4], [12, 90, 2], [12, 96, 1], [12, 102, 4], [12, 108, 2], [12, 114, 4], [12, 120, 0], [12, 126, 0], [14, 72, 4], [14, 78, 3], [14, 84, 1], [14, 90, 3], [14, 96, 4], [14, 102, 0], [14, 108, 1], [14, 114, 1], [14, 120, 1], [14, 126, 0], [16, 72, 7], [16, 78, 0], [16, 84, 3], [16, 90, 0], [16, 96, 0], [16, 102, 7], [16, 108, 4], [16, 114, 1], [16, 120, 1], [16, 126, 7]]
        self.max_score=self.score
        for typ in arr:
            ob=self.get_brick(typ[0],typ[1],typ[2])
            for a in range(0,6):
                    self._board[typ[0]][typ[1]+a]=ob
        

    def liveslost(self):
        self.remaining_lives-=1
        self.finish_powerups()
        if self.remaining_lives == 0:
            system('clear')
            self.game_on=-1

        else:
            posn=random.randint(int(self._paddle.y), int(self._paddle.y+self._paddle.length))
            dist_from_centre=self._paddle.get_left_coor()+(self._paddle.get_length())/2-posn
            factor_change=math.floor(dist_from_centre/2.5)
            y_vel=-factor_change*0.5
            self._balls = [ball(global_stuff.rows-2, posn, -1, y_vel)]

    def finish_powerups(self):
        for powu in self._powerups:
            if powu.remaining_time>=0:
                powu.deactivate(self)
        self._powerups=[]

    def printboard(self):
        print_str=""
        print_str+="LIVES: "+str(self.remaining_lives)+"\t"+"TIME: "+str(datetime.timedelta(seconds=int(time.time()-self.start_time)))+"\t"+"SCORE: "+str(self.score)+" "
        if self.ufo:
            for k in range(int(self.ufo.health/10)):
                print_str+=Fore.GREEN+"\u2588" +Style.RESET_ALL
        if time.time()-self.level_time>=30 and not self.ufo:
            print_str+="FALL TIME "
        tim=-1
        for pow_up in self._powerups:
            if isinstance(pow_up, laser):
                tim=max(pow_up.remaining_time, tim)
        if self._paddle.shoot:
            print_str+=Fore.RED+"LASER ON: "+ str(tim) +Style.RESET_ALL
        for powu in self._powerups:
            if powu.remaining_time>0:
                print_str+=powu.icon
        curlen=len(print_str)
        for y in range(global_stuff.cols+1-curlen):
            print_str+=" "
        print_str+="\n"
        for y in range(global_stuff.cols+1):
            print_str+="\u23AF"
        print_str+="\n"
        for x in range(global_stuff.rows+1):
            print_str+="\u23B9"
            y=0
            while y<len(self._board[x]):
                if (x==self._paddle.x and y==self._paddle.y):
                    for k in range(self._paddle.length):
                        print_str+="\u2588"
                    # print("\u2588", end="")
                    y+=self._paddle.length
                    continue
                if x==self._paddle.x-1 and y==self._paddle.y and self._paddle.shoot:
                    print_str+="\u23B9"
                    y+=1
                    continue
                if x==self._paddle.x-1 and y==self._paddle.y+self._paddle.length and self._paddle.shoot:
                    print_str+="\u23B8"
                    y+=1
                    continue
                
                if(isinstance(self._board[x][y], brick.brick)) and self._board[x][y].lvl>0:
                    # print(self._board[x][y].lvl, end="")
                    ob=self._board[x][y]
                    if ob.lvl==1:
                        print_str+=Fore.GREEN+"\u2588"+ Style.RESET_ALL
                        y+=1
                        continue
                        # print(Fore.GREEN+"\u2588"+ Style.RESET_ALL,end="")
                    if ob.lvl==2:
                        print_str+=Fore.YELLOW+"\u2588" +Style.RESET_ALL
                        y+=1
                        continue
                        # print(Fore.YELLOW+"\u2588" +Style.RESET_ALL,end="")
                    if ob.lvl==3:
                        y+=1
                        print_str+=Fore.RED+"\u2588"+ Style.RESET_ALL
                        continue
                        # print(Fore.RED+"\u2588"+ Style.RESET_ALL,end="")
                    if ob.lvl==4:
                        y+=1
                        print_str+=Fore.LIGHTMAGENTA_EX+"\u2588" +Style.RESET_ALL
                        continue
                        # print(Fore.LIGHTMAGENTA_EX+"\u2588" +Style.RESET_ALL,end="")
                    if ob.lvl==10:
                        y+=1
                        print_str+=Fore.WHITE+"\u2588" +Style.RESET_ALL
                        continue
                    if ob.lvl==20:
                        y+=1
                        print_str+=Fore.CYAN+"\u2588" +Style.RESET_ALL
                        continue
                
                # elif (x==math.floor(self._ball.x) and y==math.floor(self._ball.y)):
                #     # print("\u2B24", end="")
                #     print_str+="\u2B24"
                else:
                    if self.ufo is not None:
                        if x>=self.ufo.x and x<=self.ufo.x+self.ufo.width:
                            if y==self.ufo.y:
                                for k in range(self.ufo.length):
                                    print_str+="*"
                                y+=self.ufo.length
                                continue
                    flag1=0
                    for ball in self._balls:
                        if math.floor(ball.x)==x and math.floor(ball.y)==y:
                            print_str+=ball.icon
                            flag1=1
                            break
                    if flag1:
                        y+=1
                        continue
                    flag1=0
                    for bom in self.bombs:
                        if math.floor(bom.x)==x and math.floor(bom.y)==y:
                            print_str+="💣"
                            flag1=1
                            break
                    if flag1:
                        y+=2
                        continue
                    flag=0
                    for pow_up in self._powerups:
                        if pow_up.x==x and pow_up.y==y:
                            # print("\u2795",end="")
                            print_str+=pow_up.icon
                            flag=1
                            break
                    if flag:
                        y+=2
                        continue
                    flag=0
                    for bull in self._bullets:
                        if bull.x==x and bull.y==y:
                            # print("\u2795",end="")
                            print_str+="\u8593"
                            flag=1
                            break
                    if flag:
                        y+=2
                        continue
                    print_str+=" "
                    y+=1
                
                
                        # print(" ", end="")
            # print()
            print_str+="\u23B8\n"
        system('clear')
        print(print_str)
        # np.set_printoptions(threshold=sys.maxsize)
        # print(self._board)
        

    def moveboardpaddle(self, key):
        self._paddle.movepaddle(key, self._balls)
        if self.ufo:
            self.ufo.moveufo(key, self)
    
    def droppows(self):
        for pow_up in self._powerups:
            prev_x=pow_up.x
            pow_up.droppowerup()
            curr_x=pow_up.x
            if prev_x<self._paddle.x-1 and curr_x>=self._paddle.x-1 and pow_up.y>=self._paddle.y and pow_up.y<=self._paddle.y+self._paddle.length:
                pow_up.execute(self)
    
    def reducepows(self):
        for index, pow_up in enumerate(self._powerups):
            pow_up.reducetime()
            if pow_up.remaining_time==0:
                pow_up.deactivate(self)
        
    def moveballs(self):
        for index, ball in enumerate(self._balls):
            ball.moveball(self)
        for bullet in self._bullets:
            bullet.moveball(self)
    
    def detectcollisionballs(self):
        for ball in self._balls:
            ball.detectbrickcollision(self)
            ball.detectpaddlecollision(self._paddle, self)
            ball.detectufocollision(self.ufo, self)
        for pow_up in self._powerups:
            pow_up.detectcollision()
    
    def releaseballs(self):
        for ball in self._balls:
            ball.releaseball()

    def check_bricks(self, x, y):
        if x<0 or x>global_stuff.rows or y<0 or y>global_stuff.cols:
            return False
        if isinstance(self._board[x][y], brick.brick) and self._board[x][y].lvl>0:
            return True
        return False
    
    def balls_remaining(self):
        return len(self._balls)
    
    def add_powerup(self, powu):
        self._powerups.append(powu)
    
    def increase_score(self, val):
        self.score+=val
        if self.score>=self.max_score:
            self.game_on=2
    
    def fallbricks(self):
        new_board=np.empty(shape=(global_stuff.rows+1, global_stuff.cols+1), dtype=np.object)
        for row in range(len(self._board)):
            for column in range(len(self._board[row])):
                if isinstance(self._board[row][column], brick.brick) and self._board[row][column].lvl>0:
                    new_board[row+1][column]=self._board[row][column]
        last_row=-1
        for row in range(len(self._board)):
            column=0
            while column<(len(self._board[row])):
                if isinstance(new_board[row][column], brick.brick):
                    new_board[row][column].x+=1
                    last_row=row
                    column+=6
                else:
                    column+=1
        pass
        self._board=new_board
        if last_row==self._paddle.x:
            self.game_on=-1
        pass
    
    def changehardnessbrick(self):
        for x in range(len(self._board)):
            for y in range(len(self._board[x])):
                if isinstance(self._board[x][y], brick.colorchangingbrick):
                # if True:
                    # print(self._board[x][y].lvl)
                    # input()
                    self._board[x][y].changecolor()
                    # self._board[row][column]
                    y+=4
    
    
    def shoot_bullets(self):
        if self.frame_no%4==0 and self._paddle.shoot:
            self._bullets.append(bullet(self._paddle.x, self._paddle.y))
            self._bullets.append(bullet(self._paddle.x-1, self._paddle.y+self._paddle.length-1))
    
    def detectbulletcollision(self):
        for bullet in self._bullets:
            bullet.checkcollision(self)
    
    def createbombs(self):
        if self.ufo is None:
            return
        if (self.frame_no)%10==0:
            self.bombs.append(bomb(self.ufo.x, self.ufo.y))
    
    def dropbombs(self):
        for bom in self.bombs:
            bom.dropbomb()
            if bom.x==self._paddle.x and (bom.y>=self._paddle.y and bom.y<=self._paddle.y+self._paddle.length):
                self.liveslost()
            if bom.x>self._paddle.x:
                self.bombs.remove(bom)
        
    def increment_frame(self):
        self.frame_no+=1
    
    def spawnblocks1(self):
        row=self.ufo.x+self.ufo.width+2
        col=0
        while col<global_stuff.cols:
            br=brick.brick1(row, col)
            for a in range(0,6):
                    self._board[row][col+a]=br
            col+=6
        pass

    def spawnblocks2(self):
        row=self.ufo.x+self.ufo.width+4
        col=0
        while col<global_stuff.cols:
            br=brick.brick2(row, col)
            for a in range(0,6):
                    self._board[row][col+a]=br
            col+=6
        pass