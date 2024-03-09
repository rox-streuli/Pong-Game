from turtle import Turtle

class Paddle(Turtle):
    """Instantiate paddle for playing pong. Inherits from Turtle class."""
    def __init__(self, start_position):
        super().__init__()
        self.hideturtle()
        self.shape('square')
        self.color('white')
        self.penup()
        # Set shapesize(stretch_wid=None, stretch_len=None, outline=None)
        # it will be the equivalent to 50 x 20 pixels turtle
        self.shapesize(5, 1)
        self.goto(start_position)
        self.speed(7)
        self.showturtle()

    def move_up(self):
        """Move paddle up if 'UP' key is pressed."""""
        y_cor = self.ycor() + 20
        self.sety(y_cor)

    def move_down(self):
        """Move paddle down if 'DOWN' key is pressed."""""
        y_cor = self.ycor() - 20
        self.sety(y_cor)
