'''
Aloha! Bienvenue and welcome to Lab 9.2
Reads data file into list. Displays maxVal
minVal, avg. Propmt for range and displays
values within it.
by Kevin Jordan for CSCI160 
kevin.jordan@und.edu ID: 1301006
'''

def readFile(): #read data in
    import FileUtils
    inFile = FileUtils.selectOpenFile("Open File") #lookup file
    if inFile == None: #check if file exists or not selected
        print("No file selected or does not exist, later aligator!")
        exit()
    readFile = open(inFile, "r") #read file
    scoresList = [] #empty list to store scores
    for line in readFile: #add values from file to list
        scoresList.append(int(line.strip()))
    readFile.close() #close file
    return scoresList #make list usable

def maxVal(scoresList): #function for max
    maxVal = -9E100 #initialize
    for i in range(len(scoresList)): #for all indexes
        val = scoresList[i] #take value
        if val > maxVal: #see if its greater than previous max
            maxVal = val #assign updated max
    return maxVal

def minVal(scoresList): #funtion for mix
    minVal = 9E100 #initialize
    for i in range(len(scoresList)): #for all indexes
        val = scoresList[i] #take value
        if val < minVal: #see if its smaller than previous min
            minVal = val #assign updated min
    return minVal

def avgScore(scoresList): #funtion for avg
    total = 0 #initialize
    for i in range(len(scoresList)): #for all indexes
        total = total + scoresList[i] #add their values
    avg = total / len(scoresList) #divide by number of values
    return avg

def matchingRangeValues(scoresList, lower, upper): #function prints values in specified range
    for i in range(len(scoresList)): #for all indexes
        val = scoresList[i] #take their value
        if (val >= lower) and (val <= upper): #and see if its in range
            print(val) #print if yes

def main(): #main program
    readFileScoreList = readFile() #reads in data file
    print("Largest score: ", format(maxVal(readFileScoreList), '5d')) #prints info from data
    print("Smallest score: ", format(minVal(readFileScoreList), '4d'))
    print("Average score: ", format(avgScore(readFileScoreList), '5.2f'))
    print()
    print("Enter range limits to search") #prompts for range values
    lower = int(input("Lower: "))
    upper = int(input("Upper: "))
    print()
    print("Values within specified range:")
    matchingRangeValues(readFileScoreList, lower, upper) #calls function to print in range values from file
    
main() #run