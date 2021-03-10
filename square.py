# Python program to draw square
import turtle

wn = turtle.Screen()  # this is to set up the screen
wn.bgcolor("light green")  # background color
wn.title("Turtle")  # Title of the game
turtle = turtle.Turtle()
turtle.shape("turtle")  # Turtle shape
turtle.color("blue")  # change the turtle color
wn.setup(width=1000, height=600)  # screen setup


for i in range(4):
    turtle.forward(200)
    turtle.right(90)


turtle.done()
