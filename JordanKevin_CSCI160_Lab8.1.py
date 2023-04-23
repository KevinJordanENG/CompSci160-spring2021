'''
Aloha! Bienvenue and welcome to Lab 8.1
Defines lots of functions and calls them
to verify functionality. Functions include
square, summation, sumOfSquare, factorial,
compare, isOdd, isEven
by Kevin Jordan for CSCI160 
kevin.jordan@und.edu ID: 1301006
'''

def square(intValue):
    '''Function takes integer parameter intValue
    and returns the square of intValue'''
    xtoThe2 = intValue*intValue
    return xtoThe2

def summation(intValue):
    '''Function takes integer parameter intValue and
    returns the summation of values 1 to intValue.
    Ex: summation(5) = 15 (1+2+3+4+5)'''
    Sum = 0
    for num in range(intValue+1):
        Sum = Sum + num
    return Sum

def sumOfSquare(intValue):
    '''Function takes integer parameter intValue and
    returns the sum of squares from 1 to intValue.
    Ex: sumOfSquare(5) = 55 (1+4+9+16+25)'''
    SumOsqr = 0
    for num in range(intValue+1):
        xtoThe2 = square(num)
        SumOsqr = SumOsqr + xtoThe2
    return SumOsqr

def factorial(intValue):
    '''Function takes integer parameter intValue and
    returns the factorial of intValue.
    Ex: factorial(5) = 120 (5*4*3*2*1)'''
    fact = 1
    for num in range(1, intValue+1):
        fact = fact*num
    return fact

def compare(intValue1, intValue2):
    '''Function compares two integer parameters intValue1
    and intValue2. Returns -1 if intValue1 is less than
    intValue2, returns 1 if intValue1 is greater than intValue2
    or returns 0 if intValue1 is equal to intValue2'''
    if intValue1 < intValue2:
        return -1
    elif intValue1 == intValue2:
        return 0
    else:
        return 1

def isOdd(intValue):
    '''Function takes integer parameter intValue and returns
    True if intValue is odd, otherwise returns False'''
    if (intValue%2) == 1:
        return True
    else:
        return False

def isEven(intValue):
    '''Function takes integer parameter intValue and returns
    True if intValue is even, otherwise returns False'''
    if isOdd(intValue) == False:
        return True
    else:
        return False

def main():
    intValue1 = int(input("Please enter 1st positive integer value: "))
    intValue2 = int(input("Please enter 2nd positive integer value: "))
    print()
    print("Demo of square function: square(", intValue1, ") = ", square(intValue1), sep='')
    print("Demo of summation function: summation(", intValue1, ") = ", summation(intValue1), sep='')
    print("Demo of sumOfSquare function: sumOfSquare(", intValue1, ") = ", sumOfSquare(intValue1), sep='')
    print("Demo of factorial function: factorial(", intValue1, ") = ", factorial(intValue1), sep='')
    print("Demo of compare function: compare(", intValue1, ',', intValue2, ") = ", compare(intValue1,intValue2), sep='')
    print("Demo of isOdd function: isOdd(", intValue1, ") = ", isOdd(intValue1), sep='')
    print("Demo of isEven function: isEven(", intValue1, ") = ", isEven(intValue1), sep='')

main()