#Torian Dawkins
#create a computer germ

from turtle import *

color('cyan')

#back ground color
bgcolor('black')

#the speed of the figure
speed(15)

hideturtle()

#initializer
b = 0

while b < 200:
    right(b)
    forward(b * 3)
    b = b + 1
