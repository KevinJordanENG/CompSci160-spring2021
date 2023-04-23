'''
Aloha! Bienvenue and welcome to Lab 7.1
Asks for file name and opens existing file
takes input of test scores until sentinel entered
writes to file and closes
by Kevin Jordan for CSCI160 
kevin.jordan@und.edu ID: 1301006
'''

import FileUtils 
print("Lets find your File!")
fileName = FileUtils.selectOpenFile("Open File") #selects file to open

if fileName == None: #makes sure user selected a file
    print("Not entered, bye!")
    exit() #if not exits program

outFile = open(fileName, "w") #write mode selected for file
testScore = int(input("Please enter test score (0-100), -1 to exit: ")) #user input
while (testScore < -1) or (testScore > 100): #makes sure in range
    testScore = int(input("Sorry test scores in % range 0-100. -1 to exit: "))
while testScore != -1: #while sentinel close value is not entered
    outFile.write(str(testScore) + '\n') #writes score with endline
    testScore = int(input()) 
    while (testScore < -1) or (testScore > 100): #makes sure in range
        testScore = int(input("Sorry test scores in % range 0-100. -1 to exit: "))    
outFile.close() #close file when exit sentinel value is entered