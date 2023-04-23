'''
Aloha! Bienvenue and welcome to Activity 9
UPC Validation from file. Returns valid
and unvalid output descriptions of codes
and their matchning product from input file
by Kevin Jordan for CSCI160 
kevin.jordan@und.edu ID: 1301006
'''

def isValidUPC(upcString): #function with algorithm to check validity of UPC
    if len(upcString) == 12: #has to be 12 character length
        sumOfEvenIndex = 0 #initialize sum variables
        sumOfOddIndex = 0
        for i in range(0,12,2): #summation of even indexed values
            sumOfEvenIndex = sumOfEvenIndex + int(upcString[i])
        sumEven3x = sumOfEvenIndex*3 #times3 
        for j in range(1,10,2): #summation of odd indexed values
            sumOfOddIndex = sumOfOddIndex + int(upcString[j])
        if (sumEven3x + sumOfOddIndex) == 0: #check digit determination
            checkDigit = 0
        else:
            checkDigit = 10 - ((sumEven3x + sumOfOddIndex) % 10)
        if checkDigit == int(upcString[len(upcString)-1]): #use of check digit to see if valid UPC
            return True
        else:
            return False
    else:
        return False
        
def UPCfromFileValidation(): #program to open and use file data
    import FileUtils
    print("Lets find your File!")
    print()
    inFile = FileUtils.selectOpenFile("Open File") #lookup file
    
    if inFile == None: #check if file exists or not selected
        print("No file selected or does not exist, later aligator!")
        exit()
    
    readFile = open(inFile, "r") #read file
    for lines in readFile: #seperate each line/item
        upcList = lines.split(':') #seperate each item description and code
        upcItem = upcList[0].strip() 
        upcNumStr = upcList[1].strip()
        if isValidUPC(upcNumStr): #check validity and print results
            print(upcItem, ": Valid UPC", sep='')
        else:
            print(upcItem, ": Invalid UPC", sep='')
    readFile.close() #close file
    return

UPCfromFileValidation() #call of main program