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


class board():
    def __init__(self, rows, columns):
        self._rows=rows
        self._columns=columns
        self._board = np.empty(shape=(rows+1, columns+1), dtype=np.object)
        self._paddle = paddle(rows-1,columns/2)
        self._balls = [ball(rows-2, random.randint(self._paddle.y, self._paddle.y+self._paddle.length))]
        self._powerups =[]
        self.score=0
        self.remaining_lives=6
        self.start_time=time.time()
    
    def getdim(self):
        return (self._rows, self._columns)
    
    def get_random_brick(self, x, y):
        random_number=random.randint(0,10)
        if random_number==0:
            return brick.brick1(x,y)
        elif random_number==1:
            return  brick.brick2(x,y)
        elif random_number==2:
            return brick.brick3(x,y)
        elif random_number==3:
            return brick.brick4(x,y)
        elif random_number==4:
            return brick.brickfixed(x,y)
        elif random_number==5:
            return brick.explodingbrick(x,y)
        else:
            return None
    
    def createlevel1(self):
        for x in range(6, 22, 2):
            y=1
            while y<116:
                if self._board[x][y]:
                    y+=1
                    continue
                ob=self.get_random_brick(x,y)
                for k in range(0,6):
                    for h in range(0,2):
                        self._board[x+h][y+k]=ob
                if ob:
                    y+=5
                else:
                    y+=1
        # self.insertspecblocks()
    
    # def insertspecblocks(self):
    #     ob=brick.explodingbrick(20,45)
    #     for k in range(0,2):
    #         self._board[20+k][45]=self._board[20+k][46]=self._board[20+k][47]=self._board[20+k][48]=ob
    
    def liveslost(self):
        self.remaining_lives-=1
        self.finish_powerups()
        if self.remaining_lives == 0:
            pass
        else:
            a=random.randint(self._paddle.y, self._paddle.y+self._paddle.length)
            self._balls=[ball(global_stuff.rows-2, a)]

    def finish_powerups(self):
        for powu in self._powerups:
            if powu.remaining_time>0:
                powu.deactivate(self)
        self._powerups=[]

    def printboard(self):
        print_str=""
        print_str+="LIVES: "+str(self.remaining_lives)+"\t"+"TIME: "+str(datetime.timedelta(seconds=int(time.time()-self.start_time)))+"\t"+"SCORE: "+str(self.score)
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
            # for y in range(len(self._board[x])):
                # print(self._board[x][y])
            while y<len(self._board[x]):
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
                if (x==self._paddle.x and y==self._paddle.y):
                    for k in range(self._paddle.length):
                        print_str+="\u2588"
                    # print("\u2588", end="")
                    y+=self._paddle.length
                    continue
                # elif (x==math.floor(self._ball.x) and y==math.floor(self._ball.y)):
                #     # print("\u2B24", end="")
                #     print_str+="\u2B24"
                else:
                    flag1=0
                    for ball in self._balls:
                        if math.floor(ball.x)==x and math.floor(ball.y)==y:
                            print_str+=ball.icon
                            flag1=1
                    if flag1:
                        y+=1
                        continue
                    flag=0
                    for pow_up in self._powerups:
                        if pow_up.x==x and pow_up.y==y:
                            # print("\u2795",end="")
                            print_str+=pow_up.icon
                            flag=1
                            break
                    if flag:
                        y+=1
                        continue
                    if not flag: 
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
    
    def droppows(self):
        for pow_up in self._powerups:
            pow_up.droppowerup()
            if pow_up.x==global_stuff.rows-2 and pow_up.y>=self._paddle.y and pow_up.y<=self._paddle.y+self._paddle.length:
                pow_up.execute(self)
    
    def reducepows(self):
        for index, pow_up in enumerate(self._powerups):
            pow_up.reducetime()
            if pow_up.remaining_time==0:
                pow_up.deactivate(self)
                self._powerups.remove(pow_up)
        
    def moveballs(self):
        for index, ball in enumerate(self._balls):
            ball.moveball(self)
    
    def detectcollisionballs(self):
        for ball in self._balls:
            a=ball.detectbrickcollision(self)
    
    def releaseballs(self):
        for ball in self._balls:
            ball.releaseball()
