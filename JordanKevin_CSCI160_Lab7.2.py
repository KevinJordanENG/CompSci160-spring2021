'''
Aloha! Bienvenue and welcome to Lab 7.2
Opens existing file and reads values contained.
Information from file then displayed such as min,
max, T/F>90, T/F<10, avg, #values, #values>=70,
#values<70, closestValTo70, closestValTo70orLess
by Kevin Jordan for CSCI160 
kevin.jordan@und.edu ID: 1301006
'''

import FileUtils
print("Lets find your File!")
print()
inFile = FileUtils.selectOpenFile("Open File") #lookup file

if inFile == None: #check if file exists or not selected
    print("No file selected or does not exist, later aligator!")
    exit()

total = 0 #initialize counters
numOvals = 0
moreOr70counter = 0
less70counter = 0
val70plus = 0
maxVal = -9E100 #ridicalus sentinels too
minVal = 9E100
closestTo70 = 9E100
closestOrLess70 = 9E100
all70plus = False #initialize flags
greater90 = False
less10 = False
readFile = open(inFile, "r") #read file
for line in readFile: #take each value
    nums = int(line.strip()) #make it a usable number
    if nums < minVal: #run all data tests
        minVal = nums
    if nums > maxVal:
        maxVal = nums
    if nums > 90:
        greater90 = True
    if nums < 10:
        less10 = True
    if nums >= 70:
        moreOr70counter += 1
    else:
        less70counter += 1
    if abs(nums-70) < abs(closestTo70-70):
        closestTo70 = nums
    if (70-nums) >= 0:
        if (70-nums) < abs(closestOrLess70-70):
            closestOrLess70 = nums
    else:
        val70plus += 1
    numOvals += 1
    total = total + nums
    
readFile.close() #close file
if numOvals == 0: #error handling for empty file
    print("Empty file...")
    exit()
avg = total/numOvals
if (numOvals - val70plus) == 0: #output of file data stats
    all70plus = True
print("FILE DATA STATS")
print("Minimum value found: ", minVal)
print("Maximum value found: ", maxVal)
if greater90 == True:
    print("Number(s) greater than 90 present")
if less10 == True:
    print("Number(s) less that 10 present")
print("Average: ", format(avg, '6.3f'))
print("Number of values found in file: ", numOvals)
print("Number of values >= 70: ", moreOr70counter)
print("Number of values < 70: ", less70counter)
print("Number closest to 70: ", closestTo70)
if all70plus == True:
    print("All numbers over 70")
else:
    print("Number closest to and < 70: ", closestOrLess70)