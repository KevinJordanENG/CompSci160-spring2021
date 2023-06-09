'''
Welcome to my house scene drawing program!
Written for CSCI 160 by Kevin Jordan
this program uses turtle to draw a nice lil house
estilo de Baja California Sur
'''

# setup for canvas on which to draw
import turtle
import math
scrn = turtle.Screen()
scrn.setup (1200,800)
scrn.bgcolor ("medium blue")
tortuga = turtle.Turtle()
tortuga.speed(8)

# draw ground
tortuga.pensize(0)
tortuga.begin_fill()
tortuga.fillcolor("chocolate")
tortuga.penup()
tortuga.goto(-600,-400)
tortuga.pendown()
tortuga.forward(1200)
tortuga.left(90)
tortuga.forward(300)
tortuga.left(90)
tortuga.forward(1200)
tortuga.left(90)
tortuga.forward(300)
tortuga.end_fill()

# draw house
tortuga.pensize(4)
tortuga.begin_fill()
tortuga.fillcolor("sienna")
tortuga.penup()
tortuga.goto(254,100)
tortuga.pendown()
tortuga.forward(400)
tortuga.left(120)
tortuga.forward(200)
tortuga.left(60)
tortuga.forward(200)
tortuga.left(60)
tortuga.forward(200)
tortuga.left(43.18067319)
tortuga.forward(438.5533035)
tortuga.left(76.81932681)
tortuga.forward(200)
tortuga.left(76.81932681)
tortuga.forward(438.5533035)
tortuga.left(103.18067319)
tortuga.forward(400)
tortuga.end_fill()

# draw door
tortuga.begin_fill()
tortuga.fillcolor("black")
tortuga.penup()
tortuga.goto(0,-100)
tortuga.pendown()
tortuga.circle(40,180)
tortuga.forward(123)
tortuga.left(76.81932681)
tortuga.forward(82)
tortuga.left(103.18067319)
tortuga.forward(142)
tortuga.end_fill()

# draw window
tortuga.begin_fill()
tortuga.fillcolor("black")
tortuga.penup()
tortuga.goto(180,-100)
tortuga.pendown()
tortuga.circle(40,180)
tortuga.forward(80)
tortuga.left(80)
tortuga.forward(82)
tortuga.left(100)
tortuga.forward(95)
tortuga.end_fill()

# draw sun
tortuga.begin_fill()
tortuga.fillcolor("gold")
tortuga.penup()
tortuga.goto(450,300)
tortuga.pendown()
tortuga.circle(60)
tortuga.end_fill()

#draw cactus (tree)
tortuga.begin_fill()
tortuga.fillcolor("dark green")
tortuga.penup()
tortuga.goto(-380,-280)
tortuga.pendown()
tortuga.forward(100)
tortuga.right(45)
tortuga.forward(80)
tortuga.left(45)
tortuga.forward(270)
tortuga.circle(20,180)
tortuga.forward(260)
tortuga.right(45)
tortuga.forward(35)
tortuga.right(135)
tortuga.forward(500)
tortuga.circle(20,180)
tortuga.forward(480)
tortuga.right(135)
tortuga.forward(35)
tortuga.right(45)
tortuga.forward(400)
tortuga.circle(20,180)
tortuga.forward(410)
tortuga.left(45)
tortuga.forward(80)
tortuga.right(45)
tortuga.forward(120)
tortuga.left(90)
tortuga.forward(56)
tortuga.end_fill()

# exit criteria
scrn.exitonclick()