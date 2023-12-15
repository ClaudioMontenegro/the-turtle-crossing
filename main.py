import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
score = Scoreboard()
player = Player()
car = CarManager()
screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    n = 0
    while n < 500:
        time.sleep(0.1)
        screen.update()
        car.car_move()
        game_is_on = car.collision(player)
        n += 1
        if player.ycor() >= 260:
            score.score_count()
            player.reset()
            car.car_clear()
            car.level += 1
        if game_is_on == False:
            score.game_over()
            break

screen.exitonclick()
