from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.ht()
        self.goto(0, 260)
        self.score = 1
        self.general_score()

    def general_score(self):
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)

    def score_count(self):
        self.score += 1
        self.clear()
        self.general_score()

    def game_over(self):
        self.gameover = self
        self.gameover.goto(0, 0)
        self.gameover.write("GAME OVER", align=ALIGNMENT, font=FONT)
