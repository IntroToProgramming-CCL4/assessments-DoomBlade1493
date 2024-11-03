#A dictionary is created that holds all 12 months and their respective amount of days, using an integer value
m = { 1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
#An integer variable is created that will allow the user to input a month(in numerical value)
n = int(input("Enter the month number (1-12): "))
#If the number inputted is equal to two, the if statement will be in effect
if n in m:
    if n == 2:
        #Because February has two different amount of days depending on the year, the user will be prompted to specify the year of their choosing
        y = int(input("Please specify the year for February: "))
        #If the remainder of the variable is equal to zero, then the if statement is in effect
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            print(f"February has 29 days in the year of {y}.")
        #If the year is less than 0, then the else-if statement will be in effect
        elif y<=0:
            print("This  year is impossible.")
        #If the variable doesnt meet any of the requirements, then the else statement below will be in effect
        else:
            print(f"February has {m[n]} days in the year of {y}.")
    #If the number inputted is not equal to two but is in the range of 1-12, the else statement will be in effect
    else:
        print(f"The month has {m[n]} days.")
#If the number inputted exceeds or is below the number 1-12, then the else statement below, will be in effect    
else:
    print("There are only 12 months in a year, either you're from a different planet or you just typed it wrong.")