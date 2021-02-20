from board import board
from input import input_to
from input import Get
import numpy as np
import sys
import time
from global_stuff import *

getch=Get()


if __name__ == '__main__':
    current_board=board(rows, cols)
    current_board.createlevel1()
    while(True):
        current_board.printboard()
        c=input_to(getch)
        if c=='q':
            sys.exit(0)
        if c=='a' or c=='d':
            current_board.moveboardpaddle(c)
        if c=='p':
            print(current_board)
            input()
        if c==' ':
            current_board.releaseballs()
        if c:
            time.sleep(0.05)    
        current_board.detectcollisionballs()
        current_board.moveballs()
        current_board.droppows()
        current_board.reducepows()
        time.sleep(0.02)
