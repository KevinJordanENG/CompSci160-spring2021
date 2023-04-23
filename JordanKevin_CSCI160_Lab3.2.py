'''
Welcome to the credits to graduate program
asks user for credits completed to date and current semester credits
outputs current class year, anticipated year after current semester
and minimum credits left to graduate (120 based)
by Kevin Jordan for CSCI 160
'''

totalCredits = int(input("Please enter your total number of credits earned to date: "))
semesterCredits = int(input("Please enter your current semester credits: "))

# current class
if totalCredits >= 90:
    print("You are currently a Senior. You're almost done!")
elif totalCredits >= 60:
    print("You are currently a Junior. Don't forget to look at taking the FE exam.")
elif totalCredits >= 24:
    print("You are currently a Sophomore. Good job working through the general ed courses.")
else:
    print("You are currently a Freshman. Welcome to the jungle!")

# anticipated class
totalCredits = totalCredits + semesterCredits
if totalCredits >=120:
    print("Con-graduations! After this semester you're done your Bachelor's!")
elif totalCredits >= 90:
    print("After this semester you will be considered a Senior.")
elif totalCredits >= 60:
    print("After this semester you will be considered a Junior.")
elif totalCredits >= 24:
    print("After this semester you will be considered a Sophomore.")
else:
    print("After this semester you will be considered a Freshman.")

# graduation status
creditsLeft = 120 - totalCredits
if creditsLeft > 0:
    print("You will have a total of", creditsLeft, "credits left before you graduate.")
else:
    print("You will have a total of", abs(creditsLeft), "credits more than you need to graduate.")