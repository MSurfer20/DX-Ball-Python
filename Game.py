from board import board
from input import input_to
from input import Get
import numpy as np
from os import system
import time
from global_stuff import *
import datetime
import time
import sys
getch=Get()

class Game:
    def __init__(self):
        self.current_board=board(rows, cols)
    
    def rungame(self):
        self.current_board.createlevel1()
        while(self.current_board.game_on==1):
            c=input_to(getch)
            if c=='q':
                sys.exit(0)
            if c=='a' or c=='d':
                self.current_board.moveboardpaddle(c)
            if c==' ':
                self.current_board.releaseballs()
            if c:
                time.sleep(0.05)    
            self.current_board.moveballs()
            self.current_board.detectcollisionballs()
            self.current_board.droppows()
            self.current_board.reducepows()
            self.current_board.printboard()
            time.sleep(0.02)
        system('clear')
        if self.current_board.game_on==-1:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\tGAME OVER!!!")
            print("\t\t\tSCORE: ",self.current_board.score)
            print("\t\t\tTIME PLAYED: ",str(datetime.timedelta(seconds=int(time.time()-self.current_board.start_time))))
            print("PRESS ENTER TO PLAY AGAIN")
        else:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\tYOU WONNN!!!")
            print("\t\t\tSCORE: ",self.current_board.score)
            print("\t\t\tTIME PLAYED: ",str(datetime.timedelta(seconds=int(time.time()-self.current_board.start_time))))
            print("PRESS ENTER TO PLAY AGAIN")
