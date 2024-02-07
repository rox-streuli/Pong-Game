from turtle import Turtle

class Ball(Turtle):
    """Instantiate ball. Inherits from Turtle class."""
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')

    def move(self):
        self.forward(20)

    def bounce_on_paddle(self):
        direction = self.heading()
        if direction < 90:
            new_direction = 180 - direction
        elif direction > 270:
            diference_to_360 = 360 - direction
            new_direction = 180 + diference_to_360
        elif 180 > direction > 90:
            diference_to_180 = 180 - direction
            new_direction = diference_to_180
        elif 180 < direction < 270:
            diference_to_270 = 270 - direction
            new_direction = 270 + diference_to_270
        elif direction == 0:
            new_direction = 180
        elif direction == 180:
            new_direction = 0
        self.setheading(new_direction)

    def bounce_on_wall(self):
        direction = self.heading()
        if 180 < direction < 270:
            diference_to_180 = direction - 180
            new_direction = 180 - diference_to_180
        elif direction > 270:
            diference_to_360 = 360 - direction
            new_direction = diference_to_360
        elif 90 < direction < 180:
            diference_to_180 = 180 - direction
            new_direction = 180 + diference_to_180
        elif direction < 90:
            new_direction = 360 - direction
        self.setheading(new_direction)
