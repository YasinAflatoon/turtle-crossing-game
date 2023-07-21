from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.level = 0
        self.level_up()

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(
            arg=f"level: {self.level}",
            move=False,
            align="left",
            font=("Consolas", 15, "normal")
        )

    def game_over(self):
        self.home()
        self.write(
            arg=f"CRASHED!",
            move=False,
            align="center",
            font=("Consolas", 40, "bold")
        )
