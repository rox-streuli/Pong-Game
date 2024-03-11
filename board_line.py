from turtle import Turtle

# constants
LINE_SETUP_START = -300
GUIDE_POSITION = (0, -280)
ALIGMENT = 'center'
FONT = ('verdana', 10, 'normal')

class Board_line(Turtle):
    """Instantiate board_line. Inherits from Turtle class."""
    def __init__(self):
        super().__init__()
        self.pensize(2)
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


class Guide(Turtle):
    """Instantiate game commands guide."""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(GUIDE_POSITION)
        self.color('lightpink')
        self.write(f"Paddle_1 press keys 'a' and 'z'. Paddle_2 press "
                   f"'up and 'down'. Press 'Q' for end game.",
                   align=ALIGMENT, font=FONT)