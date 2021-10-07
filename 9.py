# QUESTION :

# 9. Write a function is_member()that takes a value (i.e. a number, string, etc) xand a list of values a, and
# returns True if x is a member of a, False otherwise. 
# (Note that this is exactly what the inoperator does,
# but for the sake of the exercise you should pretend Python did not have this operator.)

# Solution :

def is_member(x , a) :

    for item in a :
        
        if (x == item):

            return True

    return False 

x = 3

a = [1,2,3,4,5]

f = is_member(x, a) 

print(f) 