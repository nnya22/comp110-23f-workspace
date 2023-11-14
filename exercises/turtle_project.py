"""A piece of abstract art showcasing two humans staring at the moon and sun."""
 
__author__ = "730324119"
 
from turtle import Turtle, done 
 

def main() -> None:
    """The entrypoint of my scene."""
    ertle: Turtle = Turtle()
    draw_square(ertle, -5, 5, 10)
    draw_square(ertle, -10, 10, 20)
    draw_square(ertle, -15, 15, 30)
    draw_square(ertle, -20, 20, 40)
    draw_dot(ertle, -7, 10, 4)
    draw_dot(ertle, 1, 10, 4)
    draw_sun(ertle, 8, -60, 19)
    draw_moon(ertle, -70, 10, 50)
    done()
 

def draw_square(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.color("pink")
    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i = i + 1


def draw_dot(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a dot of the given width whose top-left corner is located at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 15:
        a_turtle.forward(width)
        a_turtle.right(110)
        i = i + 1


def draw_sun(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Attempt to draw a sun of the given width whose top-left corner is located at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 20:
        a_turtle.forward(width)
        a_turtle.right(30)
        i = i + 1


def draw_moon(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Attempt to draw a moon of the given width whose top-left corner is located at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 25:
        a_turtle.forward(width)
        a_turtle.right(100)
        i = i + 1


main()