'''
Aloha! Bienvenue and welcome to Lab 12 Part 2
Parts inventory program that reads from file
and can dispaly number of parts, parts >limit,
lowest price, largest price, average price,
and prints whole parts list
by Kevin Jordan for CSCI160
kevin.jordan@und.edu ID: 1301006
'''

def getInventoryFromFile():
    import FileUtils                                                    #import needed file handling
    inFile = FileUtils.selectOpenFile("Open File")
    if inFile == None:                                                  #check if file exists/selected
        print("No file selected or does not exist, later aligator!")
        exit()
    inventory = {}                                                      #empty dict
    readFile = open(inFile, "r")
    for line in readFile:                                               #for each line in file
        line = line.strip()                                             #get rid of blank spacees
        (partName, price) = line.split(":")                             #create tuple of key/value pairs
        inventory[partName] = price                                     #add to dict
    readFile.close()
    return inventory

def inventoryMenu():
    print("Main Menu:")                                                 #menu display function
    print("1. Number of Parts")
    print("2. Parts Greater than Value Search")
    print("3. Lowest Cost Part")
    print("4. Highest Cost Part")
    print("5. Average of Part Prices")
    print("6. Display all Parts")
    print("0. To Quit")
    print()
    choice = int(input("Choice: "))
    while (choice < 0) or (choice > 6):                                 #checks for valid menu choice
        choice = int(input("Choose Valid Choice: "))
    return choice

def enterToReturnToMain():                                              #return to main menu fuction
    back = input("Press Enter to Return to Main")                       #so displayed output stays on screen
    while back != '':                                                   #as long as needed
        back = input()

def totalParts(inventory):
    counter = 0                                                         #initialize counter
    for partName in inventory:                                          #count each part in dict
        counter += 1
    return counter

def partsGreaterThan(inventory, upperLimit):
    greaterThanList = []                                                #empty list
    for partName in inventory:                                          #for each key
        if float(inventory[partName]) >= upperLimit:                    #check if matching val is above limit
            greaterThanList.append(partName)                            #if so add it to the list
    return greaterThanList

def leastExpensivePart(inventory):
    if inventory == {}:                                                 #error handling for empty dict
        return None    
    minPrice = 9E100                                                    #initialize
    for partName in inventory:                                          #for each item
        if float(inventory[partName]) < minPrice:                       #if the price is less than previous min val
            minPrice = float(inventory[partName])                       #update min val
            minPriceName = partName                                     #record key associated with min val
    return minPriceName

def mostExpensivePart(inventory):
    if inventory == {}:                                                 #error handling for empty dict
        return None
    maxPrice = -9E100                                                   #initialize
    for partName in inventory:                                          #for each item
        if float(inventory[partName]) > maxPrice:                       #if the price is more than previous max val
            maxPrice = float(inventory[partName])                       #update max val
            maxPriceName = partName                                     #record key associated with max val
    return maxPriceName

def averagePrice(inventory):
    if inventory == {}:                                                 #error handling for empty dict
        return None    
    total = 0                                                           #initialize
    counter = 0
    for partName in inventory:
        total += float(inventory[partName])                             #running total
        counter += 1                                                    #incement counter
    avg = total/counter                                                 #calc avg
    return avg

def printParts(inventory):
    print("Part                          Price")                        #print formatted output table
    for partName in inventory:
        print(format(partName, '27s'), format('$', '>s'), format(float(inventory[partName]), '7.2f'), sep='')

def main():
    inventory = getInventoryFromFile()                                  #fuction to read in dict
    choice = inventoryMenu()                                            #main menu
    while choice != 0:
        if choice == 1:                                                 #call function for total parts
            numParts = totalParts(inventory)
            print("Total Parts in Inventory:", numParts)
            print()
            enterToReturnToMain()                                       #leave output on screen until back to main is entered
            print()
        elif choice == 2:                                               #call function for parts above price limit
            upperLimit = float(input("Enter Upper Limit on Price: "))   #get upper limit input
            greaterThanList = partsGreaterThan(inventory, upperLimit)
            print("List of Parts Greater Than $", format(upperLimit, '.2f'), sep='')
            print(greaterThanList)
            print()
            enterToReturnToMain()                                       #leave output on screen until back to main is entered
            print()
        elif choice == 3:                                               #call fuction for min price
            print("Lowest Cost Part:", leastExpensivePart(inventory))
            print()
            enterToReturnToMain()                                       #leave output on screen until back to main is entered
            print()
        elif choice == 4:                                               #call fuction for max price
            print("Highest Cost Part:", mostExpensivePart(inventory))
            print()
            enterToReturnToMain()                                       #leave output on screen until back to main is entered
            print()
        elif choice == 5:                                               #call function for avg price
            avg = averagePrice(inventory)
            if avg == None:                                             #error handling if None returned from averagePrice
                print("Average of Parts Prices: ", avg)
            else:
                print("Average of Parts Prices: $", format(avg, '6.2f'), sep='')
            print()
            enterToReturnToMain()                                       #leave output on screen until back to main is entered
            print()
        elif choice == 6:                                               #call function to print dict
            print()
            printParts(inventory)
            print()
            enterToReturnToMain()                                       #leave output on screen until back to main is entered
            print()            
        choice = inventoryMenu()

main()                                                                  #run baby!