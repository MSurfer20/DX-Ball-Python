from powerup import PowerUp
from expandpaddle import expandpaddle
from shrinkpaddle import shrinkpaddle
from ballmultiplier import ballmultiplier
from fastball import fastball
from paddlegrab import paddlegrab
from thruball import thruball
# from global_stuff import power_array
import random

class brick:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.lvl=-1
    
    def reducelvl(self):
        self.lvl-=1
        if self.lvl==0:
            pow=thruball(self.x, self.y)
            return None
            return pow
        return None
    
    def destroy(self):
        self.lvl=0
        pow=paddlegrab(self.x, self.y)
        return pow
    
    def generate_powerup(self):
        pass
        
            
    
class brick1(brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lvl=1

class brick2(brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lvl=2

class brick3(brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lvl=3

class brick4(brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lvl=4

class brickfixed(brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lvl=10
    def reducelvl(self):
        return None
