from turtle import Turtle

# constants
LINE_SETUP_START = -300

class Board_line(Turtle):
    """Instantiate board_line. Inherits from Turtle class."""
    def __init__(self):
        super().__init__()
        self.pensize(3)
        self.pencolor('white')
        self.hideturtle()
        self.penup()
        self.setposition(0, LINE_SETUP_START)
        self.setheading(90)
        # draw mid board line
        for _ in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
