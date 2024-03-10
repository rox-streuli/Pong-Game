from turtle import Turtle

ALIGMENT = 'center'
FONT = ('verdana', 12, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color('lightgreen')

    def refresh_scoreboard(self, player1, player2):
        """Update player's score."""
        self.clear()
        self.write(f"Player 1 : {player1}\tPlayer 2 : {player2}",
                   align=ALIGMENT, font=FONT)

    def game_over(self, who):
        """Write game over message on window."""
        self.goto(0, 0)
        self.clear()
        self.write(f"**** GAME OVER ****\n PLAYER {who} WINS!", align=ALIGMENT,
                   font=('verdana', 18, 'normal'))
