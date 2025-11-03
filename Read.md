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
- Python Strings are arrays of bytes representing Unicode characters.
- String can be represent as single quotes `'` or  double quotes `"` or triple quotes `'''`.
- ```python
  str="I"
  str2='Love'
  str1='''Python'''
  print(type(str))
  print(type(str1))
  print(type(str2))

  OUTPUT
  <class 'str'>
  <class 'str'>
  <class 'str'>
  ```  
- ```python
  print(len(str1)) #this function return the length of an string
  #We can access string value by index as well.
  #p y t h o n
  #0 1 2 3 4 5 -- index value
  print(str1[0]) #return `p`
  #print(str1[9]) #Will return an exception because the actual length is less than accessing length
  print(str1[-1]) #return `n`
  ```
# List Data Type
- This is an ordered and mutable list 
- Can be stored mixed value.
- Values can be accessed by index value.
- ```python
  list=[] #creating empty list
  
  list1=['Parwez', "Pwskills", 121, 1022.2, 4+9j]
  print(type(list))  #<class 'list'>
  print(list1[0]) #Parwez
  print(list1[2]) #121
  print(list1[-1]) #(4+9j)
  print(list1[-1].real) #Accessing real part
  print(list1[-1].imag) #Accessing imaginary part
 ```
# Tuples
-```python
  # Tuples are created in `()` paranthesis. It is an ordered and immutable object in python.
  tup =() # Empty tuples () are created.
  print(type(tup)) #<class 'tuple'>
  # assign multiple value separated by comma called Tuple Packing.
  tup_packing=1,2,3,4, "Hello"
  print(tup_packing)
  print(type(tup_packing))
  ```
