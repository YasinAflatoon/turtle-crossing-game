from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_wid=1.2, stretch_len=1.2)
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def up(self):
        self.forward(8)

    def down(self):
        self.backward(8)
