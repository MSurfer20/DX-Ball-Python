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
        self.game_on=True
        self.current_board=board(rows, cols)
    
    def rungame(self):
        self.current_board.createlevel1()
        while(self.current_board.remaining_lives>0):
            self.current_board.printboard()
            c=input_to(getch)
            if c=='q':
                sys.exit(0)
            if c=='a' or c=='d':
                self.current_board.moveboardpaddle(c)
            if c=='p':
                print(current_board)
                input()
            if c==' ':
                self.current_board.releaseballs()
            if c:
                time.sleep(0.05)    
            self.current_board.detectcollisionballs()
            self.current_board.moveballs()
            self.current_board.droppows()
            self.current_board.reducepows()
            time.sleep(0.02)
        system('clear')
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\tGAME OVER!!!")
        print("\t\t\tSCORE: ",self.current_board.score)
        print("\t\t\tTIME PLAYED: ",str(datetime.timedelta(seconds=int(time.time()-self.current_board.start_time))))
        print("PRESS ENTER TO PLAY AGAIN")
        self.game_on=False
