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
    
    def gameloop(self):
        while(self.current_board.game_on==1):
            c=input_to(getch)
            if c=='q':
                sys.exit(0)
            if c=='a' or c=='d':
                self.current_board.moveboardpaddle(c)
            if c==' ':
                self.current_board.releaseballs()
            if c=='s':
                self.current_board.game_on=0
            if c=='c':
                self.current_board.shoot_bullets()
            if c=='p':
                input()
            if c is not None:
                time.sleep(0.05)
            self.current_board.detectbulletcollision()
            self.current_board.moveballs()
            self.current_board.detectcollisionballs()
            self.current_board.droppows()
            self.current_board.reducepows()
            self.current_board.changehardnessbrick()
            self.current_board.createbombs()
            self.current_board.dropbombs()
            self.current_board.increment_frame()
            self.current_board.spawnblocks()
            self.current_board.printboard()
            
    
    def rungame(self):
        self.current_board.createlevel1()
        self.gameloop()
        system('clear')
        if self.current_board.game_on==-1:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\tGAME OVER!!!")
            print("\t\t\tSCORE: ",self.current_board.score)
            print("\t\t\tTIME PLAYED: ",str(datetime.timedelta(seconds=int(time.time()-self.current_board.start_time))))
            print("PRESS ENTER TO PLAY AGAIN")
        else:
            self.current_board=board(rows, cols, self.current_board.score, self.current_board.start_time, self.current_board.remaining_lives)
            self.current_board.createlevel3()
            self.gameloop()
            system('clear')
            if self.current_board.game_on==-1:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\tGAME OVER!!!")
                print("\t\t\tSCORE: ",self.current_board.score)
                print("\t\t\tTIME PLAYED: ",str(datetime.timedelta(seconds=int(time.time()-self.current_board.start_time))))
                print("PRESS ENTER TO PLAY AGAIN")
            else:
                self.current_board=board(rows, cols, self.current_board.score, self.current_board.start_time, self.current_board.remaining_lives)
                self.current_board.createlevel5()
                self.gameloop()
                if self.current_board.game_on==-1:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\tGAME OVER!!!")
                    print("\t\t\tSCORE: ",self.current_board.score)
                    print("\t\t\tTIME PLAYED: ",str(datetime.timedelta(seconds=int(time.time()-self.current_board.start_time))))
                    print("PRESS ENTER TO PLAY AGAIN")
                else:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\tYOU WON THE GAME!!!")
                    print("\t\t\tSCORE: ",self.current_board.score)
                    print("\t\t\tTIME PLAYED: ",str(datetime.timedelta(seconds=int(time.time()-self.current_board.start_time))))
                    print("PRESS ENTER TO PLAY AGAIN")
