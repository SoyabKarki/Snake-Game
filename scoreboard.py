from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.display_score()

    def display_score(self):
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def calculate_score(self):
        self.score += 1
        self.clear()
        self.display_score()

    def game_end(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
        self.goto(0, -30)
        self.write("RIGHT CLICK TO CLOSE", align=ALIGNMENT, font=FONT)
