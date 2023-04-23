'''
Welcome to the int to english program
asks the user for integer number input in range 20-99
outputs the number in english
by Kevin Jordan for CSCI 160
'''
i = int(input("Please enter an integer in the range of 20-99: "))
if i<20 or i>99:
    print("Sorry, number is out of range 20-99")
else:
    if (i//10) == 9:
        print("ninety ", end='')
    elif (i//10) == 8:
        print("eighty ", end='')
    elif (i//10) == 7:
        print("seventy ", end='')
    elif (i//10) == 6:
        print("sixty ", end='')
    elif (i//10) == 5:
        print("fifty ", end='')
    elif (i//10) == 4:
        print("fourty ", end='')
    elif (i//10) == 3:
        print("thirty ", end='')    
    elif (i//10) == 2:
        print("twenty ", end='')    
    if (i%10) == 9:
        print("nine")
    elif (i%10) == 8:
        print("eight")   
    elif (i%10) == 7:
        print("seven")
    elif (i%10) == 6:
        print("six")
    elif (i%10) == 5:
        print("five")    
    elif (i%10) == 4:
        print("four") 
    elif (i%10) == 3:
        print("three")   
    elif (i%10) == 2:
        print("two")
    elif (i%10) == 1:
        print("one")