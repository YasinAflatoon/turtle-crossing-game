from turtle import Screen
from player import Player
from car import Car
from scoreboard import ScoreBoard
import time

sc = Screen()
sc.setup(width=600, height=600)
sc.tracer(0)

player = Player()
board = ScoreBoard()
car_manager = Car()

sc.listen()
sc.onkeypress(player.up, "Up")
sc.onkeypress(player.down, "Down")

game_on = True
game_speed = 0.1
while game_on:

    time.sleep(game_speed)
    sc.update()
    car_manager.create_car()
    car_manager.move()

    # Detect collision with car
    for car in car_manager.all_cars:
        if ((car.xcor() - 35 < player.xcor() < car.xcor() + 35) and (car.distance(player) < 35)) or\
                ((car.ycor() - 15 < player.ycor() < car.ycor() + 15) and (car.distance(player) < 48)):
            game_on = False
            board.game_over()

    if player.ycor() >= 270:
        board.level_up()
        for car in car_manager.all_cars:
            car.goto(-320, -320)
            car.hideturtle()
        car_manager.all_cars.clear()
        player.goto(0, -280)
        game_speed *= 0.9
        if board.level % 10 == 0:
            car_manager.car_gen_rate += 1

sc.exitonclick()
