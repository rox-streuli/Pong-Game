from turtle import Turtle
from random import choice

DIRECTIONS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


class Ball(Turtle):
    """Instantiate ball. Inherits from Turtle class."""
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        self.current_ball_speed = 0.1
        self.random_tuple_xy()

    def random_tuple_xy(self):
        """Randomize the start position and direction of the ball."""
        original_position = choice(DIRECTIONS)
        self.goto(original_position)
        if self.xcor() < 0:
            self.x_move *= -1
        if self.ycor() < 0 :
            self.y_move *= -1

    def move(self):
        """Move ball ten pixels diagonally."""
        new_x = (self.xcor() + self.x_move)
        new_y = (self.ycor() + self.y_move)
        self.goto(new_x, new_y)

    def bounce_on_wall(self):
        """Invert ycor() when bounce."""
        self.y_move *= -1

    def bounce_on_paddle(self):
        """Invert xcor() when bounce."""
        self.x_move *= -1
        self.current_ball_speed *= 0.9

    def reset_ball(self):
        """Reset ball position and invert direction
        after ball go out of the screen."""
        self.goto(0, 0)
        self.current_ball_speed = 0.1
        self.bounce_on_paddle()
