#The given variable is the password that will be used
PW=("12345")
#The "A" variable is the amount of recorded tries that are available
A=5
#The for loop will be used in the range of 5
for r in range(5):
    #A variable is created that will allow the user to input the password
    pw=input("Government Computer Online\nPlease Enter Password: ")
    #If the inputted password is the same as the given password, the for loop will be broken
    if pw==PW:
        print("\nIdentification Verified\nWelcome Back User_1")
        break
    #If the inputted password is different from the given password, the "A" variable will be subtracted by 1, and the loop will continue
    else:
        A=A-1
        print(f"\nIncorrect Password Has Been Inputted\n{A} Tries Remaining")
#If the given password is still incorrect after 5 tries, the loop will stop, and it will print a warning instead
else:
    print("There's No Where To Run, The Authorities Have Been Informed.\n If You Just Forgot Your Password, It's Not My Problem.")