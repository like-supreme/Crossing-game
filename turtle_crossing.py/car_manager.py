from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X_COOR = 280

class CarManager:
    def __init__(self):
        self.all_cars = []


    def create_car(self):
        chance = random.randint(1 , 6)
        y_coor = random.randint(-250 , 250)
        if chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))            
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.hideturtle()
            new_car.goto(X_COOR , y_coor)
            new_car.showturtle()
            self.all_cars.append(new_car)
        else:
            pass 

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)


    
    def level_up(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += 10
        