from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        #self.refresh_score()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
    def game_over(self):
        self.goto(0,0)
        # content = "default content"
        # with open("highscore.txt",mode="r") as file:
        #     content = file.read()
        # with open("highscore.txt",mode="w") as file:
        #     if (int(content) < self.score):
        #         self.highscore = self.score
        #     else:
        #         self.highscore = int(content)
        #     file.write(f"{self.highscore}")
        self.write("GAME OVER",align="center",font=("Arial",20,"normal"))
    def refresh_score(self):
        self.clear()
        content = "default content"
        with open("highscore.txt",mode="r") as file:
            content = file.read()
        self.write(f"Score : {self.score}",align="center",font=("Arial",20,"normal"))
    