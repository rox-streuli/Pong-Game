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
        """Write a winner message on window if player press 'q'."""
        self.goto(0, 0)
        self.clear()
        if who == "DRAW":
            self.write(f"**** GAME OVER ****\nIt is a {who}",
                       align=ALIGMENT, font=('verdana', 18, 'normal'))
        else:
            self.write(f"**** GAME OVER ****\nThe winner is {who}",
                       align=ALIGMENT, font=('verdana', 18, 'normal'))
