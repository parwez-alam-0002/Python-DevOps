# List Data Type.
```python
list1=[] #a new list creating 
print(type(list1))
```

# creating a list using constructor
```python
list2=list([1,2,3,4,5,6,7,8,9,10])
print(list2)
```

# convert tuples into list
```python
list3=list((10,20,30,40))
print(list3)
```

# convert set into a list
```python
list4=list({"GFG","Geeks"})
print(list4)`

# convert a string into a list
```python
list5=list("GeeksForGeeks")
print(type(list5)) 
print(list5) # ['G', 'e', 'e', 'k', 's', 'F', 'o', 'r', 'G', 'e', 'e', 'k', 's']
```

# Adding Elements into List
- We can add elements to a list using the following methods:
- append(): Adds an element at the end of the list.
- extend(): Adds multiple elements to the end of the list.
- insert(): Adds an element at a specific position.
- clear(): removes all items.

```python
list6 = [1,2,3,4,5,6,7]
list6.append(8) #insert at last
print(list6)
list6.extend([9,10]) # add multiple value at last
print(list6)
list6.insert(1,101) # add a value at a specific index
print(list6)
list6.clear() # clear all the value from the list
print(list6)
```

# Removing Elements from List
- remove(): Removes the first occurrence of an element.
- pop(): Removes the element at a specific index or the last element if no index is specified.
- del statement: Deletes an element at a specified index.
