'''
Welcome to Preject 1 program
Takes a month worth of daily high temperature data
Outputs table of #days, avgTemp, month High temp, month
Low temp, #days+32F, %days+32F, #days-32F, %days-32F
by Kevin Jordan kevin.jordan@und.edu
for CSCI 160 (Online section)
'''

print("Wlecome to the Month Temprature Analysis Program")
print()
numDays = int(input("Please enter number of days in month to analyze: ")) #input number of days to be used
while (numDays < 28) or (numDays > 31): #error check month length value and loop until valid
    numDays = int(input("Sorry, not valid length of month. Enter number of days 28-31: "))

dayCounter = 0 #initialize counters and sentinels
monthHigh = -60
monthLow = 120
freezePlus = 0
freezeLess = 0
totalDegs = 0
dailyHigh = int(input("Please enter daily High temperature in degrees F: ")) #input temp 
while (dailyHigh < -50) or (dailyHigh > 110): #error check temp value and loop till valid
    dailyHigh = int(input("Sorry enter daily High temp, range -50 to 110 (F): "))
totalDegs = totalDegs + dailyHigh #catch total if loop is not entered (numDays is commented out for use of program in other range)
while dayCounter < (numDays-1): #loop temp input until num days is reached
    dayCounter += 1
    if dailyHigh > monthHigh: #running update to monthly high
        monthHigh = dailyHigh
    if dailyHigh < monthLow: #running update to monthly low
        monthLow = dailyHigh
    if dailyHigh > 32: #num days +freezing or -freezing decision and counter
        freezePlus += 1
    else:
        freezeLess += 1
    dailyHigh = int(input("Enter next daily High temp (F): ")) #next value prompt
    while (dailyHigh < -50) or (dailyHigh > 110): #error check temp value and loop till valid
        dailyHigh = int(input("Sorry enter daily High temp, range -50 to 110 (F): "))
    totalDegs = totalDegs + dailyHigh #running total of degrees
if dailyHigh > monthHigh: #month high if loop is bypassed (numDays is commented out for use of program in other range)
    monthHigh = dailyHigh
if dailyHigh < monthLow: #month low if loop is bypassed (numDays is commented out for use of program in other range)
    monthLow = dailyHigh
if dailyHigh > 32: #num days +freezing or -freezing counter (numDays is commented out for use of program in other range)
    freezePlus += 1
else:
    freezeLess += 1

print() #output of formatted table with all values
print("Month Stats")
print("Total Days in Month:", format(numDays, '27d'))
print("Average Daily High Temp:", format((totalDegs/numDays), '23.2f'), 'F', sep='')
print("Month High Temp:", format(monthHigh, '31d'), 'F', sep='')
print("Lowest Daily High Temp:", format(monthLow, '24d'), 'F', sep='')
print("Number of Days Above Freezing:", format(freezePlus, '17d'))
print("Percentage of Days Above Freezing:", format(((freezePlus/numDays)*100), '13.2f'), '%', sep='')
print("Number of Days Freezing or Below:", format(freezeLess, '14d'))
print("Percentage of Days Freezing or Below:", format(((freezeLess/numDays)*100), '10.2f'), '%', sep='')