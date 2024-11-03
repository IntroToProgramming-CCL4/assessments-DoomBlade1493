#A variable is created, that will allow the user to input any integer value
n=int(input("Let's Determine Whether The Number Is Odd Or Even\nPlease Input A Number: "))
#A function is created to determine wether the number is even or odd
def EO():
    #If the number has a remainder equal to zero, the if statement will be executed
    if n%2==0:
        print(f"{n} is an Even Number")
        #If the number has a remainder that isnt equal to zero, the else statement will be executed
    else:
        print(f"{n} is an Odd Number")
#Because the definition has already been given, the function below will be executed
EO()