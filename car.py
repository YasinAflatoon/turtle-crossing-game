import random
from turtle import Turtle

COLORS = ["green", "blue", "red", "yellow", "purple", "orange"]


class Car:
    def __init__(self):
        self.all_cars = []
        self.car_gen_rate = 1

    def create_car(self):
        if random.randint(1, 6) <= self.car_gen_rate:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.setheading(180)
            car.shapesize(stretch_wid=1.5, stretch_len=3.5)
            car.color(random.choice(COLORS))
            car.goto(random.randint(280, 300), random.randint(-240, 240))
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.forward(5)
