from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 24, "normal")
SCOREBOARD_COLOR = "white"
SCOREBOARD_POSITION = (0, 260)
GAMEOVER_POSITION = (0,0)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snakedata.txt") as data:
            self.high_score = int(data.read())
        self.color(SCOREBOARD_COLOR)
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snakedata.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()