'''
Aloha! Bienvenue and welcome to Project 2
Program stores and tracks number of "sales"
Creates number of different items, able to
input individual item sales. Can return single
item sales, total sales, number of diffeent
items with sales, average number of items sold.
Can print list of all items and their recorded sales
Ciao for now!!!
by Kevin Jordan for CSCI160
kevin.jordan@und.edu ID: 1301006
'''

def createItems(size):
    '''Initializes array values to -1 for length of size'''
    salesList = []                                              #initialize list
    for item in range(size):                                    #loop 'size' times
        salesList.append(-1)                                    #initialize each val with -1
    return salesList

def setSales(salesList, itemNumber, numOfSales):
    '''Adds numOfSales to itemNumber's total sales value in salesList'''
    itemNumberIndex = itemNumber - 1                            #translates from human to computer counting
    if salesList[itemNumberIndex] == -1:                        #if unchanged value need to account for diff in -1 and 0 with +1
        salesList[itemNumberIndex] = salesList[itemNumberIndex] + numOfSales + 1
    else:                                                       #since val already added can just add to existing val
        salesList[itemNumberIndex] = salesList[itemNumberIndex] + numOfSales
    return

def getSales(salesList, itemNumber):
    '''Returns number of sales of itemNumber in salesList'''
    itemNumberIndex = itemNumber - 1                            #translates from human to computer counting
    if salesList[itemNumberIndex] == -1:                        #if -1 means actually 0 sales
        return 0
    else:
        return salesList[itemNumberIndex]                       #otherwise return value

def totalSales(salesList):
    '''Returns total number of sales from salesList excluding unchanged values'''
    total = 0
    for i in range(len(salesList)):                             #for each index
        if salesList[i] != -1:                                  #if it has a value other than default
            total += salesList[i]                               #add it to total
    return total

def numOfItemsWithSale(salesList):
    '''Returns the number of unique items with logged sales'''
    total = 0
    for i in range(len(salesList)):                             #for each index
        if salesList[i] != -1:                                  #if value contained is not -1
            total += 1                                          #increment counter
    return total

def getAverage(salesList):
    '''Returns the average calculaed from (total items sold / number of items with sales)'''
    if totalSales(salesList) == 0:                              #if totalSales is 0, so will be numOfItemsWithSale
        return None                                             #cant calc average
    else:                                                       #otherwise calc it
        avg = totalSales(salesList) / numOfItemsWithSale(salesList)
        return avg

def printSales(salesList):
    '''Prints to screen all items and number os sales for each'''
    print(" Item             Quantity")                         #print headers
    print("Number              Sold  ")
    for i in range(len(salesList)):                             #for each item
        if salesList[i] != -1:                                  #if there were sales print index and val
            print(format((i+1), '4d'), format(salesList[i], '18d'))
        else:                                                   #if no sales just print index
            print(format((i+1), '4d'))

def main():
    import time                                                 #needed to show messages and results before diverting back to menu
    print("Sales tracking appication")
    print("How many unique items in inventory?")
    salesList = createItems(int(input()))                       #call and create list
    print()
    print("Main menu:")
    print("Enter S to submit sales report")
    print("Enter R to check sales report for individual item")
    print("Enter T to view total items sold")
    print("Enter U to check how many unique items have recorded sales")
    print("Enter A to check average number of items sold")
    print("Enter P to view full sales report")
    print("Enter Q to quit")
    menuChoice = input()                                        #menu control variable
    while (menuChoice != 'Q') and (menuChoice != 'q'):          #while quit is not selected
        print()
        if (menuChoice == 'S') or (menuChoice == 's'):          #run program to add sales data
            print("Submit sales report selected")
            itemNumber = int(input("Enter item number: "))      #inputs needed
            numOfSales = int(input("Enter number of sales: "))
            setSales(salesList, itemNumber, numOfSales)
            print("Sales succesfully added!")
            time.sleep(3)                                       #pause so user can confirm changes made
        if (menuChoice == 'R') or (menuChoice == 'r'):          #run program to get sales data and reports it
            itemNumber = int(input("Enter item number to report times it was sold: "))
            print("Item ", itemNumber, " was sold ", getSales(salesList, itemNumber), " times", sep='')
            time.sleep(3)                                       #pause so user can confirm results
        if (menuChoice == 'T') or (menuChoice == 't'):          #runs program to get total and reports it
            print("Total items sold: ", totalSales(salesList))
            time.sleep(3)                                       #pause so user can confim results
        if (menuChoice == 'U') or (menuChoice == 'u'):          #runs program for num items with sales and reports it
            print("Number of unique items with recorded sales: ", numOfItemsWithSale(salesList))
            time.sleep(3)                                       #pause so user can confirm results  
        if (menuChoice == 'A') or (menuChoice == 'a'):          #runs program to get average and reports it
            print("Average number of items sold: ", getAverage(salesList))
            time.sleep(3)                                       #pause so user can confirm results
        if (menuChoice == 'P') or (menuChoice == 'p'):          #runs program to print whole list
            printSales(salesList)
            print("Press any key for main menu, Q to quit")     #makes user enter data so printed results can be examined
            menuReturn = input()                                #before reverting to menu or can quit directly and exit program
            if (menuReturn == 'Q') or (menuReturn == 'q'):
                break
                
        
        print()                                                 #reprint of menu items so user can choose
        print("Main menu:")
        print("Enter S to submit sales report")
        print("Enter R to check sales report for individual item")
        print("Enter T to view total items sold")
        print("Enter U to check how many unique items have recorded sales")
        print("Enter A to check average number of items sold")
        print("Enter P to view full sales report")
        print("Enter Q to quit")            
        menuChoice = input()
    print()    
    print("Exited")                                             #exit program confirmation

main()                                                          #call and run