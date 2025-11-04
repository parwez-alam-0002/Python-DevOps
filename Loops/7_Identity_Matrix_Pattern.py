# Problem 2: Print Identity Matrix Pattern
# Construct a square matrix of 1s and 0s where only diagonal elements are 1, mimicking an identity matrix.

num=int(input("Enter Numberm : "))

for i in range(num):
    for j in range(num):
        if(i is j):
            print('1',end=" ")
        else:
            print("0", end=" ")
    else:
        print()
