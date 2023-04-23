'''
Welcome to my smiley face drawing program!
Written for CSCI 160 by Kevin Jordan
this program uses turtle to draw a smiley
'''

# setup for canvas on which to draw
import turtle
scrn = turtle.Screen()
scrn.setup (800,800)
scrn.bgcolor ("deep sky blue")
tortuga = turtle.Turtle()
tortuga.pensize(12)

# draw outside
tortuga.begin_fill()
tortuga.fillcolor("gold")
tortuga.penup()
tortuga.goto(0,-300)
tortuga.pendown()
tortuga.circle(300)
tortuga.end_fill()

# draw right eye
tortuga.begin_fill()
tortuga.fillcolor("black")
tortuga.penup()
tortuga.goto(100,80)
tortuga.pendown()
tortuga.circle(30)
tortuga.end_fill()

# draw left eye
tortuga.begin_fill()
tortuga.fillcolor("black")
tortuga.penup()
tortuga.goto(-100,80)
tortuga.pendown()
tortuga.circle(30)
tortuga.end_fill()

# draw smile
tortuga.penup()
tortuga.goto(-240,0)
tortuga.pendown()
tortuga.right(90)
tortuga.circle(240, 180)

# draw nose
tortuga.penup()
tortuga.goto(0,0)
tortuga.pendown()
tortuga.right(90)
tortuga.forward(20)
tortuga.left(135)
import math
tortuga.forward(math.sqrt(2)*20)

# exit criteria
scrn.exitonclick()
