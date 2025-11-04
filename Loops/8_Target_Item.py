# Problem 1: Stop printing at a target item
# Loop through a list of items and stop printing when a specific keyword like "stop" is encountered.

list_item=tuple(input("Enter list -- ").split(" "))

for item in list_item:
    if item.upper().equals('STOP'):
        break 
    print(item.upper(),end=" ")
