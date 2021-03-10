import turtle

# optional to set up the screen
wn = turtle.Screen()  # this is to set up the screen
wn.bgcolor("white")
wn.title("Hexagon")
polygon = turtle.Turtle()
polygon.shape("turtle")
turtle.color("navy")  # change the turtle color

# variable = values
num_sides = 6
side_length = 100
angle = 360.0 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()
