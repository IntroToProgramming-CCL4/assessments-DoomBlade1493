#A list is created with six set names
list=["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
#A variable is created to allow the user to search a name
n=input("Please Input Name(Please Use Proper Capitalization): ")
#If the name inputted is in the list, the if statenemt will be executed
if n in list:
    print(f"The name, {n}, has been found in the database")
#If the name inputted is not in the list, the else statement will be executed
else:
    print(f"the name, {n}, does not exist in the database")