'''
Welcome to the average program
sums 4 integers, finds average,
and reports individual value deviation from average
by Kevin Jordan for CSCI 160
'''
print("Please only enter INTEGERS")
a = int(input("Type value a: "))
b = int(input("Type value b: "))
c = int(input("Type value c: "))
d = int(input("Type value d: "))

Sum = a+b+c+d
Avg = Sum/4
diffa = abs(Avg-a)
diffb = abs(Avg-b)
diffc = abs(Avg-c)
diffd = abs(Avg-d)
print("Sum of values entered: ", Sum)
print("Average of values entered: ", Avg)
print("Value a:", a, "Deviation from average: ", diffa)
print("Value b:", b, "Deviation from average: ", diffb)
print("Value c:", c, "Deviation from average: ", diffc)
print("Value d:", d, "Deviation from average: ", diffd)