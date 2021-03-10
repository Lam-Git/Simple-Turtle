# Python program to draw star
import turtle

wn = turtle.Screen()  # this is to set up the screen
wn.bgcolor("white")
wn.title("Turtle-Star")
star = turtle.Turtle()
star.shape("turtle")
turtle.color("navy")  # change the turtle color

for i in range(5):  # will see how many laps the turtle will go
    star.forward(200)  # the distance/big the star will be drawn
    star.right(144)  # the angle of the corners


turtle.done()
