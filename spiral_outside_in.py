# Python program to draw
# Spiral Square Outside In and Inside Out
# using Turtle Programming
# Outside_In

import turtle

wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("Outside In")
turtle = turtle.Turtle()
turtle.color("blue")
turtle.shape("turtle")


def sqrfunc(size):
    for i in range(4):
        turtle.fd(size)
        turtle.left(90)
        size = size - 5


# the code to create the Spiral Square
sqrfunc(156)
sqrfunc(136)
sqrfunc(116)
sqrfunc(96)
sqrfunc(76)
sqrfunc(56)
sqrfunc(36)
