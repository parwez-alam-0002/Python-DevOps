#Problem 1: Print a multiplication table
table=int(input("Enter the table number: "))
for i in range(2,table+1):
    for j in range(1,11):
        print(f'{i} * {j} = {i*j}')
    else:
        print("-------------------")
