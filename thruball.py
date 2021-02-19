from powerup import PowerUp
from ball import ball

class thruball(PowerUp):
    def __init__(self, x, y):
        icon="🔥"
        super().__init__(x, y, icon)
    
    def execute(self, board):
        super().execute()
        for ball in board._balls:
            ball.setfire()

    def deactivate(self, board):
        for ball in board._balls:
            ball.stopfire()
