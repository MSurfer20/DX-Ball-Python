from powerup import PowerUp
from ball import ball

class fireball(PowerUp):
    def __init__(self, x, y, x_vel, y_vel):
        icon="F"
        super().__init__(x, y, x_vel, y_vel, icon)
    
    def execute(self, board):
        self.x=-1
        self.y=-1
        check_flag=0
        for pow_up in board._powerups:
            if isinstance(pow_up, fireball) and pow_up.remaining_time>0:
                pow_up.remaining_time=120
                check_flag=1
        if check_flag==0:
            super().execute()
            for ball in board._balls:
                ball.setgold()
    
    def deactivate(self, board):
        for ball in board._balls:
            ball.stopgold()
