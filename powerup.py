class PowerUp:
    def __init__(self, x, y, icon):
        self.remaining_time=-1
        self.x=x
        self.y=y
        self.v_x=2
        self.icon=icon
    
    def execute(self):
        self.remaining_time=120
        self.x=-1
        self.y=-1
        pass
    
    def deactivate(self):
        pass
    
    def droppowerup(self):
        self.x+=self.v_x

    def reducetime(self):
        self.remaining_time-=1
