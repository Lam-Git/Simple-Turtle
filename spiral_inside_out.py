import turtle  # Inside_Out

wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("Inside Out")
turtle = turtle.Turtle()
turtle.color("blue")
turtle.shape("turtle")


def sqrfunc(size):
    for i in range(4):
        turtle.fd(size)
        turtle.left(90)
        size = size + 5


sqrfunc(6)
sqrfunc(26)
sqrfunc(46)
sqrfunc(66)
sqrfunc(86)
sqrfunc(106)
sqrfunc(126)
sqrfunc(146)
sqrfunc(166)
