from powerup import PowerUp
from ball import ball

class paddlegrab(PowerUp):
    def __init__(self, x, y):
        icon="\u270A"
        super().__init__(x, y, icon)
    
    def execute(self, board):
        super().execute()
        board._paddle.stick=True

    def deactivate(self, board):
        board._paddle.stick=False
        pass
