# QUESTION :

# 1. Define a function max()that takes two numbers as arguments and returns the largest of them. 
# Use the ifthen­else construct available in Python.
# (It is true that Python has the max()function built in, but writing it
# yourself is nevertheless a good exercise.)


# Solution :

def max(arg1 , arg2):
    if arg1>arg2 :
        return arg1
    else:
        return arg2

f = max(7, 5) 
print(f) 