from powerup import PowerUp
import math

class fastball(PowerUp):
    def __init__(self, x, y):
        icon="⚡"
        super().__init__(x, y, icon)
    
    def execute(self, board):
        super().execute()
        for ball in board._balls:
            ball.increase_ball_velocity()
    
    def deactivate(self, paddle):
        pass
