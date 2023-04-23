'''
Aloha! Bienvenue and welcome to Lab 9.1
Takes input test scores and writes them
to file. Will ask to create another file
after finishing creating previous file
by Kevin Jordan for CSCI160 
kevin.jordan@und.edu ID: 1301006
'''

def testScoreGet(): #funtion to get scores
    print("Enter scores. Enter -1 to end list and save to file.")
    scores = input("Scores: ")
    scoresList = [] #empty list to store scores
    while scores != '-1': #append scores till sentinel is entered
        scoresList.append(scores)
        scores = input()
    return scoresList
    
def writeFile(scoresList): #funtion to write to file
    import FileUtils
    fileName = FileUtils.selectSaveFile ("Save File")
    if fileName == None: #makes sure user selected a file
        print("Oh alright, don't save it then!")
        exit() #if not exits program
    outFile = open(fileName, "w") #write mode
    for i in range(len(scoresList)): #for each index
        outFile.write(scoresList[i] + '\n') #write its value on a new line
    outFile.close() 
        
def main(): #main program
    scores = testScoreGet() #get scores
    writeFile(scores) #write file
    nextFile = input("Create another file? Enter Y/N: ") #prompt to write another file
    while (nextFile == 'Y') or (nextFile == 'y'): #keep getting scores and writing files while yes
        scores = testScoreGet()
        writeFile(scores)
        nextFile = input("Create another file? Enter Y/N: ")
        
main() #run