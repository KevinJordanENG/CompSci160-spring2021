'''
Welcome to the integer checking program
enter 2 integers and the program checks the numbers for:
a. if first value is a multiple of 3
b. if first value is even or odd
c. if first value is +,-, or 0
d. if first value is or not in range 2000-2021
e. if first value is >, <, == second value
f. if second value == 0. If !=, value1/value2 as int and float
by Kevin Jordan for CSCI 160
'''

valueOne = int(input("Please enter an integer: "))
valueTwo = int(input("Please enter another integer: "))

# test a
if ((valueOne % 3) == 0) and (valueOne != 0):
    print("Frist integer value is a multiple of 3")
# test b
if (valueOne % 2) == 0:
    print("First integer value is Even")
else:
    print("First integer value is Odd")
# test c
if valueOne > 0:
    print("First integer value is Positive")
elif valueOne < 0:
    print("First integer value is Negative")
else:
    print("First integer value is Zero")
# test d
if (valueOne >= 2000) and (valueOne <= 2021):
    print("First integer value is in range 2000-2021")
else:
    print("First integer value is not in range 2000-2021")
# test e
if valueOne > valueTwo:
    print("First integer value is Greater-Than second integer value")
elif valueOne < valueTwo:
    print("First integer value is Less-Than second integer value")
else:
    print("First integer value is Equal-To second integer value")
# test f
if valueTwo == 0:
    print("Second integer value is Zero")
else:
    intDivVal = int(valueOne/valueTwo)
    floatDivVal = valueOne/valueTwo
    print("First divided by Second value integer form: ", intDivVal)
    print("First divided by Second value floating point form: ", floatDivVal)