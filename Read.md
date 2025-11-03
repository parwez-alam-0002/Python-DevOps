# Introduction 

- Python is one of the most popular programming languages. It’s simple to use, packed with features and supported by a wide range of libraries and frameworks. Its clean syntax makes it beginner-friendly.

```python
  print("Hello World!)
```

# Comments:
- Used for human understanding, Interpreter always ignore that.
- Single line comment `#`
- Multi-line comment `'''` or `"""`.

# Indentation : 
- Used to define the block of code.

# Input and output
```python
  #Taking multiple input and spliting this
  x,y,z=input("Enter the value :").split()
  print("Value of X :",x)
  print("Value of Y :",y)
  print("Value of Z :",z)
```

# Find DataType of Input in Python
 ```python
  x=int(input())
  print(type(x))
 ```

# Keywords 
- These are the reserve keywords that we cannot use in variable names, function names, identifiers in python.
- for check the list of keywords
- ```python
  import keyword
  print(keyword.kwlist) #It will list all the keywords present in the python.
  for = 10 # this is not accepted in python because for is a reserve keyword.
  ```
# Data types
- Decide what are the operation can be perform with that data.
- ```python
  no=100 
  print(type(no)) #<class 'int'>
  flt=2.20
  print(type(flt)) #<class 'float'>
  imj=2+4j
  print(type(imj)) #<class 'complex'>
  ```
  
