from turtle import Turtle
from random import randint

x_location = randint(-770, 770)
y_location = randint(-400, 400)

def goto_random():
  self.speed(10)
  x_location = randint(-770, 770)
  y_location = randint(-400, 400)
  self.goto(x_location, y_location)