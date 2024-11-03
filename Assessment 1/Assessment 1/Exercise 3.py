#A dictionary is created that will be used to store the given information("Name", "Hometown", and "Age")
user={'Names:':'1','Hometown:':'2','Age:':3}
#The strings used in the dictionary is separated into their own variables
k1=("Names:")
k2=("Hometown:")
k3=("Age:")
#The user will then input their Name, Hometown, and Age
user[k1]=input("Enter Name: ")
user[k2]=input("Enter Hometown: ")
#Depending on the inputted age, there will be two different outcomes
user[k3]=int(input("Enter Age(Please Use Integer Value): "))
#If the inputted number is less than or equal to zero, then the if statement will be shown
if user[k3]<=0:
    print(f"How are you {user[k3]} years old?\nThat is literally a negative number.")
#Else, it would separate the key, and the value of the dictionary and it will print the information given by the user
else:
    for key, value in user.items():
        print(f"\n{key}\n{value}")