# Jumping through While - Python
import math
def printIncreasingPower(x):
    #code here
    # Loop to jump in powers of 2
    itr=1
    count=1
    while(itr<=x):
        #code here
       itr=int(math.pow(count,2))
       count=count+1
       if itr<=x:
           print(itr,end=" ")
       else:
            break
        
