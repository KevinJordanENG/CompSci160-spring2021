'''
Aloha! Bienvenue and welcome to Lab 8.2
Writes letters KCJ using turtle graphics
and unique functions for each letter
once without and once with shadows added
by Kevin Jordan for CSCI160 
kevin.jordan@und.edu ID: 1301006
'''

def drawK(x, y, letterColor): #draws a K with turtle
    import turtle
    tortuga = turtle.Turtle()
    tortuga.home()
    tortuga.pencolor(letterColor)
    tortuga.pensize(20)
    tortuga.penup()
    tortuga.goto(x,y)
    tortuga.pendown()
    tortuga.right(90)
    tortuga.forward(300)
    tortuga.right(180)
    tortuga.forward(150)
    tortuga.right(30)
    tortuga.forward(173.2050908)
    tortuga.right(180)
    tortuga.forward(173.2050908)
    tortuga.left(60)
    tortuga.forward(173.2050908)

def drawC(x, y, letterColor): #draws a C with turtle one char width to right of K
    import turtle
    tortuga = turtle.Turtle()
    tortuga.home()
    tortuga.pencolor(letterColor)
    tortuga.pensize(20)
    tortuga.penup()
    tortuga.goto(x+120,y)
    tortuga.forward(86.60254038)
    tortuga.right(90)
    tortuga.forward(43.30127019)
    tortuga.right(180)
    tortuga.pendown()
    tortuga.circle(43.30127019, 180)
    tortuga.forward(213.3974596)
    tortuga.circle(43.30127019, 180)

def drawJ(x, y, letterColor): #draws a J with turtle two char widths to right of K
    import turtle
    tortuga = turtle.Turtle()
    tortuga.home()
    tortuga.pencolor(letterColor)
    tortuga.pensize(20)
    tortuga.penup()
    tortuga.goto(x+240,y)
    tortuga.right(90)
    tortuga.forward(256.6987298)
    tortuga.pendown()
    tortuga.circle(43.30127019, 180)
    tortuga.forward(256.6987298)
    tortuga.left(90)
    tortuga.forward(86.60254038)

def drawShadowedK(x, y, letterColor, offset): #draws a K and its shadow with turtle
    drawK(x+offset, y-offset, "black")
    drawK(x, y, letterColor)

def drawShadowedC(x, y, letterColor, offset): #draws a C and its shadow with turtle one char width to right of K
    drawC(x+offset, y-offset, "black")
    drawC(x, y, letterColor)

def drawShadowedJ(x, y, letterColor, offset): #draws a J and its shadow with turtle two char widths to right of K
    drawJ(x+offset, y-offset, "black")
    drawJ(x, y, letterColor)

def main(): #main program to call functions
    x = int(input("Please enter 1st starting x coordinate value: ")) #user promt -450 recommended
    y = int(input("Please enter 1st starting y coordinate value: ")) #user promt 250 recommended
    x2 = int(input("Please enter 2nd starting x coordinate value: ")) #user promt 100 recommended
    y2 = int(input("Please enter 2nd starting y coordinate value: ")) #user promt 100 recommended
    letterColor = input("Please enter valid turtle color: ") #why not 'gold'
    offset = int(input("Please enter desired shadow offset: ")) #5-25 recommended
    import turtle
    scrn = turtle.Screen() #turtle screen setup
    scrn.setup (1200,800)
    scrn.bgcolor ("medium blue")
    drawK(x, y, letterColor) #calls initals functions no shadow
    drawC(x, y, letterColor)
    drawJ(x, y, letterColor)
    drawShadowedK(x2, y2, letterColor, offset) #calls initials functions with shadows
    drawShadowedC(x2, y2, letterColor, offset)
    drawShadowedJ(x2, y2, letterColor, offset)
    scrn.exitonclick() #exit condition

main() #calls to execute