from turtle import Turtle

class Ball(Turtle):
    """Instantiate ball. Inherits from Turtle class."""
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
