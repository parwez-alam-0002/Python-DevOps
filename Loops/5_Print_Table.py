#Problem 1: Print a multiplication table
table=int(input("Enter the table number: "))
for i in range(1,11):
    print(f'{table} * {i} = {table*i}')
