# Problem 2: Sum until user enters 0
# Keep reading numbers from the user and calculate the cumulative sum until the input is 0.
sum=0
while True:
    no=int(input("Enter Number: "))
    sum=sum+no 
    if not no:
        print("Exit with 0.")
        break
    else:
        print("Sum is",sum)

