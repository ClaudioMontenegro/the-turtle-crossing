from turtle import Turtle, Screen
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "black", "pink"]
MOVE_INCREMENT = 10
STARTING_Y_POSITION = list(range(-220, 250, 50))
STARTING_X_POSITION = list(range(300, 500, 100))
screen = Screen()


class CarManager:
    def __init__(self):
        self.list_car = []
        self.new_car_list = []
        self.level = 1
        self.car_maker()

    def car_maker(self):
        for i in range(0, 1000):
            self.car = Turtle("square")
            self.car.color(random.choice(COLORS))
            self.car.shapesize(stretch_len=2)
            self.car.penup()
            self.car.ht()
            self.car.goto(random.choice(STARTING_X_POSITION), random.choice(STARTING_Y_POSITION))
            self.list_car.append(self.car)

    def car_move(self):
        number = random.randint(0, 999)
        randit = random.randint(0, 999)
        if (number % 2) == 1 and number > randit:
            self.new_car_list.append(self.list_car[number])
        for car in self.new_car_list:
            new_x = car.xcor() - MOVE_INCREMENT * (self.level/5)
            y = car.ycor()
            car.st()
            car.goto(new_x, y)

    def car_clear(self):
        for self.car in self.list_car:
            self.car.clear()

    def collision(self, player):
        for car in self.new_car_list:
            if car.xcor() <= 0:
                if car.distance(player) < 30:
                    return False
