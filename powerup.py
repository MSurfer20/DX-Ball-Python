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
        # print(self.x)
        # print(self.y)
        self.x+=self.v_x
        self.y+=self.v_y
        self.v_x+=self.accel
        # print(self.x)
        # print(self.y)
        # input()

    def reducetime(self):
        self.remaining_time-=1
