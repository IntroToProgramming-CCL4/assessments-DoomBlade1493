#Two variable are created, one to determine the score of the user after answering the questions, and another to hold the given answer
score=0
print("QUESTION 1")
ans=input("What is the capital of France? ")
#Regardless of capitalization, as long as the answer is correct, it will be counted
ans=ans.lower()
if ans=="paris":
    print("You are correct")
#The variable that is keeping the score will be modified by adding one
    score=score+1
    print("Your Score:",score)
#If the answer is wrong, it will state that the user has given an incorrect answer and it will not modify the score
else:
    print("That is incorrect, the correct answer is Paris")
    print("Your Score:",score)

print("\nQUESTION 2")
ans=input("What is the capital of Germany? ")
ans=ans.lower()
if ans=="berlin":
    print("You are correct")
    score=score+1
    print("Your Score:",score)
else:
    print("That is incorrect, the correct answer is Berlin")
    print("Your Score:",score)

print("\nQUESTION 3")
ans=input("What is the capital of Ireland? ")
ans=ans.lower()
if ans=="dublin":
    print("You are correct")
    score=score+1
    print("Your Score:",score)
else:
    print("That is incorrect, the correct answer is Dublin")
    print("Your Score:",score)

print("\nQUESTION 4")
ans=input("What is the capital of The United Kingdom? ")
ans=ans.lower()
if ans=="london":
    print("You are correct")
    score=score+1
    print("Your Score:",score)
else:
    print("That is incorrect, the correct answer is London")
    print("Your Score:",score)

print("\nQUESTION 5")
ans=input("What is the capital of Italy? ")
ans=ans.lower()
if ans=="rome":
    print("You are correct")
    score=score+1
    print("Your Score:",score)
else:
    print("That is incorrect, the correct answer is Rome")
    print("Your Score:",score)

print("\nQUESTION 6")
ans=input("What is the capital of Austria? ")
ans=ans.lower()
if ans=="vienna":
    print("You are correct")
    score=score+1
    print("Your Score:",score)
else:
    print("That is incorrect, the correct answer is Vienna")
    print("Your Score:",score)

print("\nQUESTION 7")
ans=input("What is the capital of Greece? ")
ans=ans.lower()
if ans=="athens":
    print("You are correct")
    score=score+1
    print("Your Score:",score)
else:
    print("That is incorrect, the correct answer is Athens")
    print("Your Score:",score)

print("\nQUESTION 8")
ans=input("What is the capital of Hungary? ")
ans=ans.lower()
if ans=="budapest":
    print("You are correct")
    score=score+1
    print("Your Score:",score)
else:
    print("That is incorrect, the correct answer is Budapest")
    print("Your Score:",score)

print("\nQUESTION 9")
ans=input("What is the capital of Portugal? ")
ans=ans.lower()
if ans=="lisbon":
    print("You are correct")
    score=score+1
    print("Your Score:",score)
else:
    print("That is incorrect, the correct answer is Lisbon")
    print("Your Score:",score)

print("\nQUESTION 10")
ans=input("What is the capital of Russia? ")
ans=ans.lower()
if ans=="moscow":
    print("You are correct")
    score=score+1
    print("\nYour Score:",score)
else:
    print("That is incorrect, the correct answer is Moscow")
    print("\nYour Score:",score)
#After all questions are answered, the "score" variable will be checked.
#If the score is equal to 0, the first if statement will be in effect
if score==0:
    print("\nNo Offence, But Did You Even Try To Answer The Questions?")
#If the score is less than 5 but is greater than 0, the second if statement will be in effect
if score<=5 and score>0:
    print("\nAt Least You Tried......")
#If the score is greater than 5 but is less that 9, the third if statement will be in effect
if score>=5 and score<=9:
    print("\nIm Impressed With Your Knowledge Of Europe, Even If You Made a Mistake Or Two")
#If the given score is a 10, the fourth if statement will be in effect
if score==10:
    print("\nCongratulations, You Got A 10/10. I Didn't Plan For This Outcome So Have This Smile =)")