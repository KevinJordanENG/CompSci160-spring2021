'''
Aloha! Bienvenue and welcome to Lab 11
Birthdays program stores who has birthdays
on any specific day for a one month file.
Can open different month files, add birthdays,
seach by dates, and display all birthdays for month
by Kevin Jordan for CSCI160
kevin.jordan@und.edu ID: 1301006
'''

def printMenuChoices():
    print ("What would you like to do?")
    print (" 1. Open a data file")
    print (" 2. Add new name")
    print (" 3. Search by date")
    print (" 4. Display all birthdays for the month")
    print (" 5. Exit program")
    print ()

def showMenu():
    printMenuChoices()
    menuChoice = int(input("Your choice? "))
    while menuChoice < 1 or menuChoice > 5:
        print("Please enter a valid choice (1-5)")
        print()
        menuChoice = int(input("Your choice? "))
    return menuChoice

def getBdaysFromFile(fileName):
    import os
    bDayDict = {}                                                               #initialize dict
    while os.path.isfile(fileName) == False:                                    #check if is file loop till is
        print("Not found. Be sure to include file extention and try again!")
        fileName = input()  
    inFile = open(fileName, "r")                                                #file open in read mode
    for line in inFile:                                                         #for each line
        line = line.strip()                                                     #get rid of whitespace
        (name, date) = line.split(":")                                          #seperate key value pairs by sep
        bDayDict[date] = name                                                   #assign to dict
    inFile.close()
    return bDayDict                                                             #return dict

def addBday(bDayDict):
    name = input("Name to add: ")
    date = input("Birthdate: ")
    if date in bDayDict:                                                        #if date is taken error message
        print("Sorry, date is taken. Try again with different date")
    else:                                                                       #else add it
        bDayDict[date] = name

def dateSearch(bDayDict):
    date = input("Enter date to search, 0 to quit: ")
    while date != '0':                                                          #loop for search
        if date in bDayDict:                                                    #if key exists print
            print("Birthday: ", bDayDict[date])
        else:                                                                   #else error message
            print("No one with that birthday in list")
        date = input("Enter date to search: ")

def printBdays(bDayDict):
    print("Name                Date")                                           #spaced headers
    for date in bDayDict:                                                       #print formatted output for each entry
        print(format(bDayDict[date], '20s'), format(date, '>3s'))

def saveBdaysToFile(bDayDict, fileName):
    outFile = open(fileName, "w")                                               #file opened in write mode
    for date in bDayDict:                                                       #for each key value pair
        outLine = bDayDict[date] + ":" + date                                   #add them and their seperator
        outFile.write(outLine + "\n")                                           #make sure new line for each entry
    outFile.close()

def main():
    option = showMenu()                                                         #main menu
    while option != 5:                                                          #if not exit condition
        if option == 1:                                                         #read file function
            print("Enter file name, with file extention")
            fileName = input()
            bDayDict = getBdaysFromFile(fileName)
            print()
        elif option == 2:                                                       #add birthday function
            addBday(bDayDict)
            print()
        elif option == 3:                                                       #search function
            dateSearch(bDayDict)
            print()
        elif option == 4:                                                       #print all birthdays function
            print()
            printBdays(bDayDict)
            print()
            back = input("Press enter to return to main menu ")                 #return to main condition
            while back != '':                                                   #so printout stays as long as desired
                back = input()    
        option = showMenu()
    saveBdaysToFile(bDayDict, fileName)                                         #save changes to file
        
main()                                                                          #run