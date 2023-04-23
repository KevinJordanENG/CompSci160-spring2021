'''
Welcome to the GPA calculator!
User inputs courses with name, # of credits, and grades
outputs GPA, number of credits attempted vs passed,
and number of classes attempted vs passed
by Kevin Jordan for CSCI 160
'''

print("GPA Calculator")
numClasses = 0 #initialize
totalHonPoints = 0
totalCredits = 0
creditsPassed = 0
classesPassed = 0
GPA = 0

classNames = input("Enter a class: ") #first prompt
while classNames != '': #event controlled loop with exit of empty string
    numClasses = numClasses + 1 #iterator
    numCredits = int(input("Enter the number of credits: ")) #credits per class
    if numCredits > 0: #check valid input
        letGrade = input("Enter your grade: ")
        if letGrade == "A" or letGrade == "a": #determine grade and convet to number
            numGrade = 4
        elif letGrade == "B" or letGrade == "b":
            numGrade = 3
        elif letGrade == "C" or letGrade == "c":
            numGrade = 2
        elif letGrade == "D" or letGrade == "d":
            numGrade = 1
        else:
            numGrade = 0
        honPoints = numCredits * numGrade #per class calc
        totalHonPoints = totalHonPoints + honPoints #update total
        if (numGrade == 0) or (numGrade == 1): #determine pass or not
            creditsPassed = creditsPassed + 0 #no pass, do not add class data to passed totals
            classesPassed = classesPassed + 0        
        else: #if passed update totals
            creditsPassed = creditsPassed + numCredits
            classesPassed = classesPassed + 1
        totalCredits = totalCredits + numCredits #total crdits
        GPA = totalHonPoints / totalCredits #GPA calc
        print()
        classNames = input("Enter the next class: ") #next prompt
    else: #not valid credit number input breakout
        numClasses = numClasses - 1
        classNames = ''
        print("You entered an invalid input. GPA so far...") #error message

print() #print table of results
print("GPA:", format(GPA, "21.3f"))
print("Credits attepmted", format(totalCredits, "8d"))
print("Credits passed", format(creditsPassed, "11d"))
print("Classes attempted", format(numClasses, "8d"))
print("Classes passed", format(classesPassed, "11d"))

