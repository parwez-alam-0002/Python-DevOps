# Problem 1: Skip out-of-stock items
# Iterate through a shopping list and skip any item marked as unavailable or out of stock.

items = ["milk", "bread", "out of stock", "eggs"]

for i in items:
    if i=="out of stock":
        continue
    print(i.strip())
