#Five variables are created with an integer value
n1=0
n2=50
n3=30
n4=50
n5=100
#A for loop in the range of 51 is created, and for every loop, the data value of the variables "n1" and "n2" will be added and subtracted by 1 respectively, until the range limit has been reached
for r in range(51):
    print(f"{n1}\t{n2}")
    n1=n1+1
    n2=n2-1
#A for loop in the range of 21 is created, for every loop the data value of "n3" will be added by 1, "n4" will be subtracted by 2, and "n5" will be added by 5
for a in range(21):
    print(f"\t\t{n3}\t{n4}\t{n5}")
    n3=n3+1
    n4=n4-2
    n5=n5+5