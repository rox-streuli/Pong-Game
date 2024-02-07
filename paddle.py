from turtle import Turtle

class Paddle(Turtle):
    """Instantiate paddle for playing pong. Inherits from Turtle class."""
    def __init__(self, start_position):
        super().__init__()
        self.hideturtle()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(7, 1)
        self.goto(start_position)
        self.showturtle()

    def move_up(self):
        """Move paddle up if 'UP' key is pressed."""""
        y_cor = self.ycor() + 20
        self.sety(y_cor)

    def move_down(self):
        """Move paddle down if 'DOWN' key is pressed."""""
        y_cor = self.ycor() - 20
        self.sety(y_cor)
