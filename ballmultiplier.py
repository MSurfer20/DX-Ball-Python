from powerup import PowerUp
from ball import ball

class ballmultiplier(PowerUp):
    def __init__(self, x, y, x_vel, y_vel):
        icon='❌'
        super().__init__(x, y, x_vel, y_vel, icon)
    
    def execute(self, board):
        super().execute()
        new_balls=[]
        for each_ball in board._balls:
            ball1=ball(each_ball.x, each_ball.y, each_ball.x_vel, max(each_ball.y_vel,1), False, each_ball.fire, each_ball.fast_ball)
            ball2=ball(each_ball.x, each_ball.y, each_ball.x_vel, min(-1,-each_ball.y_vel), False, each_ball.fire, each_ball.fast_ball)
            new_balls=new_balls+[ball1, ball2]
        board._balls=new_balls

    def deactivate(self, board):
        pass
