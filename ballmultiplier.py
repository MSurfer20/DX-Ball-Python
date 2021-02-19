from powerup import PowerUp
from ball import ball

class ballmultiplier(PowerUp):
    def __init__(self, x, y):
        icon='2️⃣'
        super().__init__(x, y, icon)
    
    def execute(self, board):
        super().execute()
        new_balls=[]
        for each_ball in board._balls:
            ball1=ball(each_ball.x, each_ball.y, each_ball.x_vel, each_ball.y_vel, False)
            ball2=ball(each_ball.x, each_ball.y, each_ball.x_vel, -each_ball.y_vel, False)
            new_balls=new_balls+[ball1, ball2]
        board._balls=new_balls

    def deactivate(self, board):
        pass
