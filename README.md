Into to turtle module:

see more in-dept info@ https://realpython.com/beginners-guide-python-turtle/
or https://www.geeksforgeeks.org/turtle-programming-python/

“Turtle” is a Python feature like a drawing board, which lets us command a turtle to draw all over it! Turtle is a pre-installed Python library that enables users to create pictures and shapes by providing them with a virtual canvas. The onscreen pen that you use for drawing is called the turtle and this is what gives the library its name. In short, the Python turtle library helps new programmers get a feel for what programming with Python is like in a fun and interactive way. It’s a straightforward yet versatile way to understand the concepts of Python.

With the Python turtle library, you can draw and create various types of shapes and images.

So as stated above, before we can use turtle, we need to import it. We import it as :

from turtle import \*

# or

import turtle

After importing the turtle library and making all the turtle functionalities available to us, we need to create a new drawing board(window) and a turtle.

Method ---Parameter ---Description
Turtle() ---None---Creates and returns a new turtle object
forward() ---amount ---Moves the turtle forward by the specified amount
backward() ---amount ---Moves the turtle backward by the specified amount
right() ---angle ---Turns the turtle clockwise
left() ---angle ---Turns the turtle counter clockwise
penup() ---None ---Picks up the turtle’s Pen
pendown() ---None--- Puts down the turtle’s Pen
up() ---None ---Picks up the turtle’s Pen
down() ---None ---Puts down the turtle’s Pen
color() ---Color name ---Changes the color of the turtle’s pen
fillcolor() ---Color name ---Changes the color of the turtle will use to fill a polygon
heading() ---None ---Returns the current heading
position() ---None ---Returns the current position
goto() ---x, y--- Move the turtle to position x,y
begin_fill()--- None ---Remember the starting point for a filled polygon
end_fill() ---None ---Close the polygon and fill with the current fill color
dot() ---None ---Leave the dot at the current position
stamp() ---None ---Leaves an impression of a turtle shape at the current location
shape() ---shapename ---Should be ‘arrow’, ‘classic’, ‘turtle’ or ‘circle’

Turtle have a couple of other options that you can try :
Square
Arrow
Circle
Turtle
Triangle
Classic
