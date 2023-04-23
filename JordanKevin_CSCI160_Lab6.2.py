'''
Welcome to the multiplication table program
Takes user input in 1-10 range and creates
Table of values 1-10 times input 
by Kevin Jordan for CSCI 160
'''

userVal = int(input("Please enter an integer value 1-10: "))
if userVal < 1 or userVal > 10:
    print("Sorry, bad number dude...")
else:
    print()
    print("Multiplication table for", userVal)
    for num in range(1, 10+1):
        ans = num * userVal
        print(format(num, "2d"), '*', format(userVal, "2d"), '=', format(ans, "3d"))