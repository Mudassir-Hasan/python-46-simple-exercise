# QUESTION :

# 2. Define a function max_of_three()that takes three numbers as arguments and returns the largest of
# them.

# Solution :

def max_of_three(arg1 , arg2 , arg3) :
    
    if (arg1 > (arg2 and arg3)) :
        return arg1 
    
    elif (arg2 > (arg1 and arg3)):
        return arg2 

    elif (arg3 > (arg1 and arg2)) :
        return arg3 

f = max_of_three(3, 2, 5) 

print(f) 