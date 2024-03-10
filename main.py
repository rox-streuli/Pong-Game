from turtle import Screen, Turtle
from board_line import Board_line
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

# constants
START_POSITION_PADDLE_1 = -400, 0
START_POSITION_PADDLE_2 = 400, 0
HEIGHT= 600
WIDTH = 900
PLAYER_1 = 0
PLAYER_2 = 0

# create board
board = Screen()
board.setup(width=WIDTH, height=HEIGHT)
board.bgcolor('black')
board.title("Pong")

# Creade scoreboard banner
scoreboard = Scoreboard()
scoreboard.refresh_scoreboard(PLAYER_1, PLAYER_2)

# turn off tracer
board.tracer(0)

# create line in the middle of the board
line = Board_line()

# crate paddles
paddle_1 = Paddle(START_POSITION_PADDLE_1)
paddle_2 = Paddle(START_POSITION_PADDLE_2)

# create ball
def new_ball():
    return Ball()

ball = new_ball()

# prapare to listen to key events
board.listen()

# Collect key-events for paddle_1
board.onkey(paddle_1.move_up, key='a')
board.onkey(paddle_1.move_down, key='z')

# Collect key-events for paddle_2
board.onkey(paddle_2.move_up, key='Up')
board.onkey(paddle_2.move_down, key='Down')

game_on = True

while game_on:
    time.sleep(0.1)
    board.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_on_wall()

    # detect collision with paddles
    if paddle_1.distance(ball) < 50 and ball.xcor() < -380 or \
            paddle_2.distance(ball) < 50 and ball.xcor() > 380:
        ball.bounce_on_paddle()

    # Point for opposite player if paddle misses ball
    if ball.xcor() > 400:
        # point player 1
        PLAYER_1 += 1
        # reset ball and refresh score
        ball = new_ball()
        scoreboard.refresh_scoreboard(PLAYER_1, PLAYER_2)

    elif ball.xcor() < -400:
        # point player 2
        PLAYER_2 += 1
        # reset ball and refresh score
        ball = new_ball()
        scoreboard.refresh_scoreboard(PLAYER_1, PLAYER_2)


board.exitonclick()
