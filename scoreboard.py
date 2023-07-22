from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.level = 0
        with open("data.txt") as data_file:
            self.high_score = int(data_file.read())
        self.level_up()

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(
            arg=f"Level: {self.level}\nHighscore: {self.high_score}",
            move=False,
            align="left",
            font=("Consolas", 15, "normal")
        )
        if self.level > self.high_score:
            with open("data.txt", "w") as data_file:
                self.high_score = self.level
                data_file.write(str(self.high_score))

    def game_over(self):
        self.home()
        self.write(
            arg=f"CRASHED!",
            move=False,
            align="center",
            font=("Consolas", 40, "bold")
        )
