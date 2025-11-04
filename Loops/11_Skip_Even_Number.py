# Problem 2: Skip even numbers
# Loop from 1 to n and print only the odd numbers by skipping the even ones.

num=int(input("Enter the number"))
for i in range(1,num):
    if i %2 !=0:
        print(i,end=" ")
