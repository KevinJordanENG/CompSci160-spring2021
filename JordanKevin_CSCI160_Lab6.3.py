'''
Welcome to the rectangle drawing program
Takes user input for width and height and
Draws a rectangle with a '*' of that size
by Kevin Jordan for CSCI 160
'''

symbol = '*'
space = ' '

width = int(input("Please enter a Width (values 1-20): "))
while (width < 1) or (width > 20):
    width = int(input("Yo I said betweeen 1-20! Please enter a Width: "))
height = int(input("Please enter a Height (values 1-10): "))
while (height < 1) or (height > 10):
    height = int(input("Ey man, What did I say? Please enter a Height value 1-10! "))

print(symbol*width)
if width == 1:
    for j in range((height-2)):
        print(symbol)
else:    
    for j in range((height-2)):
        print(symbol, space*(width-2), symbol, sep='')
if height != 1:
    print(symbol*width)
        