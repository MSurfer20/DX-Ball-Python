from powerup import PowerUp
from ball import ball
import os

class laser(PowerUp):
    def __init__(self, x, y, x_vel, y_vel):
        icon="🔫"
        super().__init__(x, y, x_vel, y_vel, icon)
    
    def execute(self, board):
        self.x=-1
        self.y=-1
        check_flag=0
        for pow_up in board._powerups:
            if isinstance(pow_up, laser) and pow_up.remaining_time>0:
                pow_up.remaining_time=120
                check_flag=1
        if check_flag==0:
            super().execute()
            board._paddle.shoot=True
            system("vlc --intf dummy --loop laserfinal.mp3 &")

    
    def deactivate(self, board):
        board._paddle.shoot=False
        os.system("killall vlc")
