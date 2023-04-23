'''
Welcome to +/- average program
Takes all user inputs and averages all
Positive and negative integers separately
by Kevin Jordan for CSCI 160
'''

negTotal = 0
posTotal = 0
negNumCount = 0
posNumCount = 0
negAvg = 0
posAvg = 0

userInt = int(input("Please enter any integer (0 to exit): "))
while userInt != 0:
    if userInt < 0:
        negTotal = negTotal + userInt
        negNumCount += 1
        negAvg = negTotal / negNumCount
    elif userInt > 0:
        posTotal = posTotal + userInt
        posNumCount += 1
        posAvg = posTotal / posNumCount
    userInt = int(input("Please enter any integer (0 to exit): "))

print()
print(negNumCount, ":Negative number(s)")
print("Average of Negative numbers: ", format(negAvg, "5.2f"))
print()
print(posNumCount, ":Positive number(s)")
print("Average of Positive numbers: ", format(posAvg, "5.2f"))