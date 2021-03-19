from global_stuff import *
class PowerUp:
    def __init__(self, x, y, v_x, v_y, icon):
        self.remaining_time=-1
        self.x=x
        self.y=y
        self.v_x=v_x
        self.v_y=v_y
        # print(self.v_y)
        # print(self.v_x)
        # input()
        self.icon=icon
        self.accel=0.2
    
    def execute(self):
        self.remaining_time=120
        self.x=-1
        self.y=-1
        pass
    
    def deactivate(self):
        pass
    
    def droppowerup(self):
        if self.x==-1 and self.y==-1:
            return
        # print(self.x)
        # print(self.y)
        self.x+=self.v_x
        self.y+=self.v_y
        self.v_x+=self.accel
        if self.v_x>2:
            self.v_x=2
        # print(self.x)
        # print(self.y)
        # input()

    def reducetime(self):
        self.remaining_time-=1
    
    def detectcollision(self):
        if self.x==-1 and self.y==-1:
            return
        if((self.x)<=0):
            self.topwallcollision()
        if((self.y)<=0 or (self.y)>=cols-1):
            self.sidewallcollision()
    
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
    
    def reflect_x_velocity(self):
        self.v_x=self.v_x*-1
    
    def reflect_y_velocity(self):
        self.v_y=self.v_y*-1
