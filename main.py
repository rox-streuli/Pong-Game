from turtle import Screen
from turtle import Turtle
from paddle import Paddle

# constants
LINE_SETUP_START = -300
START_POSITION_PADDLE_1 = -400, 0
START_POSITION_PADDLE_2 = 400, 0

# create board
board = Screen()
board.setup(height=600, width=900)
board.bgcolor('black')
board.title("Pong")

# turn off tracer
board.tracer(0)

# create board_line turtle
board_line = Turtle()
board_line.pensize(3)
board_line.pencolor('white')
board_line.hideturtle()
board_line.penup()
board_line.speed('fastest')
board_line.setposition(0, LINE_SETUP_START)
board_line.setheading(90)

# draw mid board line
for _ in range(30):
    board_line.pendown()
    board_line.forward(10)
    board_line.penup()
    board_line.forward(10)

paddle_1 = Paddle(START_POSITION_PADDLE_1)
paddle_2 = Paddle(START_POSITION_PADDLE_2)

# update sscreen to show board
board.update()

board.listen()
# Collect key-events for paddle_1
board.onkey(paddle_1.move_up, key='Up')
board.onkey(paddle_1.move_down, key='Down')

# Collect key-events for paddle_2
board.onkey(paddle_2.move_up, key='a')
board.onkey(paddle_2.move_down, key='z')

game_on = True
board.tracer(1)
while game_on:
    board.update()

board.exitonclick()
