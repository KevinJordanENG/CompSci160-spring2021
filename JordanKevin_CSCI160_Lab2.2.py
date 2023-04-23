'''
Welcome to the conversion program
enter seconds: converts to hours, minutes, seconds
by Kevin Jordan for CSCI 160
'''

secondsTotal = int(input("Please enter a whole number of seconds: "))
hours = int(secondsTotal/3600)
minutes = int((secondsTotal - hours*3600) / 60)
seconds = int((secondsTotal - hours*3600) % 60)
print("Hours: ", hours, "Minutes: ", minutes, "Seconds: ", seconds)