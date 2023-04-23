'''
Aloha! Bienvenue and welcome to Project 3
Program fills dict from file for book data, allows 
book addition, search by text in title, prints
table of dict, takes 'order' of books, displays
books in specified price range, saves final dict
by Kevin Jordan for CSCI160
kevin.jordan@und.edu ID: 1301006
'''

def getBooksFromFile():
    library = {}                                                        #empty dict
    readFile = open('books.txt', "r")
    for line in readFile:                                               #for each line in file
        line = line.strip()                                             #get rid of blank spacees
        (bookName, price) = line.split(":")                             #create tuple of key/value pairs
        library[bookName] = price                                       #add to dict
    readFile.close()
    return library

def mainMenu():
    print("Main Menu")                                                  #main menu choices
    print("1. Add Book to Library")
    print("2. Dispaly All Books")
    print("3. Search for a Book")
    print("4. Take a Book Order")
    print("5. Search by Price")
    print("0. To Quit")
    print()
    choice = int(input("Enter Menu Choice: "))
    while (choice < 0) or (choice > 5):                                 #checks for valid menu choice
        choice = int(input("Choose Valid Option: "))
    return choice    

def enterToReturnToMain():                                              #return to main menu fuction
    back = input("Press Enter to Return to Main")                       #so displayed output stays on screen
    while back != '':                                                   #as long as needed
        back = input()

def addBookToDict(library, bookName, price):                            #add key value pair to dict
    library[bookName] = price

def displayLibrary(library):                                            #print dict contents
    print("Book Title                           Price")                 #in formatted table
    for bookName in library:
        print(format(bookName, '35s'), '$'+format(float(library[bookName]), '6.2f'), sep='')

def searchForBook(library):
    strToSearch = input("Search Text (Hit Enter to Return to Main Menu): ").lower()
    while strToSearch != '':                                            #check for exit condition
        notFoundFlag = True                                             #set flag if str is contained in dict keys
        print()
        for bookName in library:
            if strToSearch in bookName.lower():                         #if str exists in any dict keys print it
                print(format(bookName, '35s'), '$'+format(float(library[bookName]), '6.2f'), sep='')
                notFoundFlag = False                                    #and change flag to show match was found
        if notFoundFlag == True:                                        #if str was not found in dict keys
            print("No Book Title Found Containing", strToSearch)        #print it wasn't found
        print()
        strToSearch = input("Search Text (Hit Enter to Return to Main Menu): ").lower()
    print()

def bookOrder(library):
    bookName = input("Book Title to Add to Cart: ")                     #needs to be precisely key value in dict
    numBooks = 0                                                        #initialize counters
    totalPrice = 0
    while bookName != '':                                               #while not exit condition
        if bookName in library:                                         #if key exists in dict
            quantity = int(input("Quantity: "))                         #ask for quantity
            numBooks += quantity                                        #add quantity to running total
            totalPrice += float(library[bookName])*quantity             #calc price for entered key/quantity
        bookName = input("Book Title to Add to Cart: ")
    print()
    print("Book Order")                                                 #print order totals when done
    print("Total Books: ", numBooks)
    print("Total Price: ", '$'+format(totalPrice, '.2f'))

def searchBooksByPrice(library):
    lower = float(input("Enter Lower Price Limit: "))                   #limits
    upper = float(input("Enter Upper Price Limit: "))
    print()
    print("Books in Price Range")                                       #print table of matching key/value pairs
    print("Book Title                           Price")
    for bookName in library:                                            #check if matches and print if so for each entry
        if (float(library[bookName]) >= lower) and (float(library[bookName]) <= upper):
            print(format(bookName, '35s'), '$'+format(float(library[bookName]), '6.2f'), sep='')

def writeLibraryToFile(library):
    outFile = open('books.txt', "w")                                    #write mode
    for bookName in library:                                            #for each item
        outLine = bookName + ':' + library[bookName]                    #add key value pair as string
        outFile.write(outLine + "\n")                                   #write each key/value pair to new line
    outFile.close()

def main():
    import time                                                         #need sleep function for choice 1
    library = getBooksFromFile()                                        #read in dict data from txt file
    choice = mainMenu()                                                 #menu loop
    while choice != 0:
        if choice == 1:
            bookName = input("Book Title: ")                            #user input for key/value pair to add to dict
            price = input("Price: ")
            addBookToDict(library, bookName, price)                     #call function to add to dict
            print()
            print(bookName, "added!")                                   #dispaly success before retuning to main menu
            time.sleep(2)
        if choice == 2:
            displayLibrary(library)                                     #call function to display library
            print()
            enterToReturnToMain()                                       #leave output on screen until back to main is entered
            print()
        if choice == 3:
            searchForBook(library)                                      #call function to search by text
        if choice == 4:
            bookOrder(library)                                          #call function to create book order
            print()
            enterToReturnToMain()                                       #leave output on screen until back to main is entered
            print()
        if choice == 5:
            searchBooksByPrice(library)                                 #call function to search in min/max price range
            print()
            enterToReturnToMain()                                       #leave output on screen until back to main is entered
            print()            
        choice = mainMenu()
    writeLibraryToFile(library)                                         #save to same file when done

main()                                                                  #LETS GOOOOO!!!