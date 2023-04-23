'''
Aloha! Bienvenue and welcome to Activity 11
Translation program, reads in file data
of two language word pairs, and can output
the other language word when prompted
by Kevin Jordan for CSCI160
kevin.jordan@und.edu ID: 1301006
'''

def getDictFromFile():
    '''Reads key/value pairs from file'''
    import FileUtils
    translationDict = {}
    fileName = FileUtils.selectOpenFile("Open File")
    if fileName == None:
        print("No file selected or does not exist, later aligator!")
        exit()    
    inFile = open (fileName, "r")
    for line in inFile:
        line = line.strip()
        (english, spanish) = line.split(":")
        translationDict[english] = spanish
    inFile.close()
    return translationDict  

def translate(translationDict, wordToTranslate):
    '''Takes input word and if it is a key, returns translated word'''
    if wordToTranslate in translationDict:
        return translationDict[wordToTranslate]
    else:
        return "Word is not in translation dictionary"

def main():
    translationDict = getDictFromFile()
    print("Please enter an English word to see Spanish translation")
    print("Press Enter to quit")
    wordToTranslate = input("English: ")
    while wordToTranslate != '':
        print("Spanish:", translate(translationDict, wordToTranslate))
        print()
        print("Enter English word or Enter to quit")
        wordToTranslate = input("English: ")    

main()