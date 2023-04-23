'''
Aloha! Bienvenue and welcome to Lab 10
Whole suite of functions that are called
from the main program to show functionlity.
by Kevin Jordan for CSCI160 
kevin.jordan@und.edu ID: 1301006
'''

def fillListFromFile(fileName):
    '''Takes input file name, reads data, returns a list'''
    import os
    if os.path.isfile(fileName) == False:
        print(fileName, "not found. Be sure to include file extention and try again!")
        exit()
    readFile = open(fileName, 'r')
    theList = []
    for line in readFile:
        theList.append(int(line.strip()))
    readFile.close()
    return theList

def findMaxValue(theList):
    '''Finds max value of a list'''
    maxVal = theList[0]
    for i in range(len(theList)):
        if theList[i] > maxVal:
            maxVal = theList[i]
    return maxVal

def findMinValue(theList):
    '''Finds min value of a list'''
    minVal = theList[0]
    for i in range(len(theList)):
        if theList[i] < minVal:
            minVal = theList[i]
    return minVal

def calcRange(theList):
    '''Finds range of a list'''
    Max = findMaxValue(theList)
    Min = findMinValue(theList)
    Range = Max - Min
    return Range

def calcAverage(theList):
    '''Finds average of a list'''
    total = 0
    for values in theList:
        total += values
    average = total/len(theList)
    return average

def findNumberAbove(theList, testValue):
    '''Returns the number of values greater than testValue'''
    counter = 0
    for values in theList:
        if values > testValue:
            counter += 1
    return counter

def findFirstOccurrence(theList, valueToFind):
    '''Returns index of first occurence of valueToFind'''
    index = -1
    for i in range(len(theList)):
        if theList[i] == valueToFind:
            index = i
            break
    return index

def findLastOccurrence(theList, valueToFind):
    '''Returns index of last occurence of valueToFind'''
    index = -1
    for i in range(len(theList)):
        if theList[i] == valueToFind:
            index = i
    return index

def calcCount(theList, valueToFind):
    '''Returns the number of times valueToFind is in theList'''
    counter = 0
    for value in theList:
        if value == valueToFind:
            counter += 1
    return counter

def isInList(theList, valueToFind):
    '''Returns True/False if valueToFind is in list'''
    if calcCount(theList, valueToFind) != 0:
        return True
    else:
        return False

def isInAscOrder(theList):
    '''Returns True/False if list is in ascending order'''
    previousLow = theList[0]
    for i in range(len(theList)):
        if theList[i] < previousLow:
            return False
        else:
            previousLow = theList[i]
    return True

def isInDescOrder(theList):
    '''Returns True/False if list is in descending order'''
    previousHigh = theList[0]
    for i in range(len(theList)):
        if theList[i] > previousHigh:
            return False
        else:
            previousHigh = theList[i]
    return True

def main():
    theList = fillListFromFile(input("Enter the file name to import: "))
    testValue = int(input("Please enter a value to test: "))
    valueToFind = int(input("Please enter a value to find: "))
    print()
    print("Here is the imported list of values:")
    print(theList)
    print()
    print("Max value found in list: ", findMaxValue(theList))
    print("Min value found in list: ", findMinValue(theList))
    print("Range of values found in list: ", calcRange(theList))
    print("Average of values found in list: ", calcAverage(theList))
    print("Number of values greater than ", testValue, ': ', findNumberAbove(theList, testValue), sep='')
    print("Index of first occurrence of ", valueToFind, ': ', findFirstOccurrence(theList, valueToFind), sep='')
    print("Index of last occurrence of ", valueToFind, ': ', findLastOccurrence(theList, valueToFind), sep='')
    print("Number of occurrences of ", valueToFind, ': ', calcCount(theList, valueToFind), sep='')
    print(valueToFind, "is in the list: ", isInList(theList, valueToFind))
    print("List in ascending order: ", isInAscOrder(theList))
    print("List in descending order: ", isInDescOrder(theList))
    
main()