'''
Aloha! Bienvenue and welcome to Lab 12 Part 1
Parts inventory program that creates a dict
with item/price value pairs and writes to file
by Kevin Jordan for CSCI160
kevin.jordan@und.edu ID: 1301006
'''

def buildInventory():
    inventory = {}                                      #create empty dict
    partName = input("Part Name: ")                     #part name
    while partName != '':                               #loop til exit condition
        price = str(float(input("Price: ")))            #price for part
        inventory[partName] = price                     #add to dict
        partName = input("Part Name: ")
    return inventory                                    #return dict

def writeInventoryToFile(inventory):
    import FileUtils                                    #import needed module
    fileName = FileUtils.selectSaveFile ("Save File")
    if fileName == None:                                #no file chosen error handling
        print("Oh alright, don't save it then!")
        exit() 
    outFile = open(fileName, "w")                       #write mode
    for partName in inventory:                          #for each item
        outLine = partName + ':' + inventory[partName]  #add key value pair as string
        outFile.write(outLine + "\n")                   #write each key/value pair to new line
    outFile.close()

def main():
    print("Parts Inventory Creator")
    print("Enter Part Description and Price")
    print("Press Enter to End and Write to File")
    inventory = buildInventory()                        #call function for data input
    writeInventoryToFile(inventory)                     #call function to write to file

main()