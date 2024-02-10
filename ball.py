from turtle import Turtle

class Ball(Turtle):
    """Instantiate ball. Inherits from Turtle class."""
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.setheading(10)

    def move(self):
        self.forward(20)

    def bounce_on_paddle(self):
        direction = self.heading()
        if direction == 0:
            new_direction = 180
        elif direction == 180:
            new_direction = 0
        elif 90 < direction < 180 or direction > 270:
            new_direction = direction - 90
        elif 180 < direction < 270 or direction < 90:
            new_direction = direction + 90
        self.setheading(new_direction)
        self.move()

    def bounce_on_wall(self):
        direction = self.heading()
        if direction == 90:
            new_direction = 272
        elif direction == 270:
            new_direction = 92
        elif direction < 90:
            new_direction = 360 - direction
        elif 90 < direction < 180:
            new_direction = direction + 90
        elif direction > 180:
            new_direction = 360 - direction
        self.setheading(new_direction)
        self.move()
