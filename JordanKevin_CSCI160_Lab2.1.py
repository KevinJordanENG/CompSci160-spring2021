'''
Welcome to the conversion program
enter: hours, minutes, seconds, to convert all to seconds
by Kevin Jordan for CSCI 160
'''

hours = int(input("Please enter a whole number of hours: "))
minutes = int(input("Please enter a whole number of minutes in the range 0-59: "))
seconds = int(input("Please enter a whole number of seconds in the range 0-59: "))
totalSeconds = (hours*3600) + (minutes*60) + seconds
print("Total time entered in seconds: ", totalSeconds)