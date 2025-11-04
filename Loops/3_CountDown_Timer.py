# Problem 1: Countdown timer
# Implement a countdown that starts from a user-given number and decreases to 1, displaying the remaining time at each step.

no=int(input("Enter the number"))
while(no):
    print(no)
    no=no-1
else:
    print("Exit with 0")
