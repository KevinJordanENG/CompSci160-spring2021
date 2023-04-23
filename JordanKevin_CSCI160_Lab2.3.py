'''
Welcome to the address program
formats entered address to US standard mail form
by Kevin Jordan for CSCI 160
'''

firstName = input("Enter First Name: ")
lastName = input("Enter Last Name: ")
address = input("Enter Address: ")
city = input("Enter City: ")
state = input("Enter State: ")
zipCode = input("Enter Zip Code: ")

# Method 1:
print()
print(firstName, lastName)
print(address)
print(city, ', ', state, ' ', zipCode, sep='')

# Mehtod 2:
print('\n', firstName, ' ', lastName, '\n', address, '\n', city, ', ', state, ' ', zipCode, sep='')

# Method 3:
print('\n', firstName, sep='', end=' ')
print(lastName)
print(address)
print(city, ',', sep='', end=' ')
print(state, end=' ')
print(zipCode)