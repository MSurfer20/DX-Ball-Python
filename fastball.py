from powerup import PowerUp
import math

class fastball(PowerUp):
    def __init__(self, x, y, x_vel, y_vel):
        icon="⚡"
        super().__init__(x, y, x_vel, y_vel, icon)
    
    def execute(self, board):
        self.x=-1
        self.y=-1
        check_flag=0
        for pow_up in board._powerups:
            if isinstance(pow_up, fastball) and pow_up.remaining_time>0:
                pow_up.remaining_time=120
                check_flag=1
        if check_flag==0:
            super().execute()
            for ball in board._balls:
                ball.increase_ball_velocity()
    
    def deactivate(self, board):
        super().deactivate()
        for ball in board._balls:
            ball.decrease_ball_velocity()
