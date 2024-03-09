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
        self.paddle1 = 0
        self.paddle2 = 0
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        """Update paddle score."""
        self.write(f"Player 1 : {self.paddle1}\tPlayer 2 : {self.paddle2}",
                   align=ALIGMENT, font=FONT)

    def increase_score(self, who):
        """Increase score by 1 and refresh scoreboard."""
        who += 1
        self.clear()
        self.refresh_scoreboard()

    def game_over(self, who):
        """Write game over message on window."""
        self.goto(0, 0)
        self.reset()
        self.write(f"**** GAME OVER ****\n PLAYER {who} WINS!", align=ALIGMENT,
                   font=('verdana', 18, 'normal'))
