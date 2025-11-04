#Problem 1: Print each item in a shopping list
#The problem is to take shopping items as input from the user and display them one by one in a structured format.
item_list=input("Enter the item list").split(" ")

#iterate using for loop
for i in item_list:
    print(i.strip())n #strip() method used to remove trailing and leading space.
else:
    print("exit with 0 value")
