import math
#Problem 2: Print squares of numbers from 1 to n
no=int(input("Enter max value:"))

for i in range(1,no+1):
   # print(int(math.pow(i,2)),end="\t")
   print(i*i,end="\t")
else:
    print("Exit with 0")
