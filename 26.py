# QUESTION :

# Using the higher order function reduce(), 
# write a function max_in_list() that takes a list of numbersand returns the largest one. 
# Then ask yourself: 
# why define and call a new function, when I can just as wellcall the reduce() function directly?

# Solution :

from functools import reduce

def max_in_list(lst) :
    def max_in_two(a,b) :
        if a>b :
            return a 
        else:
            return b  

    return reduce(max_in_two , lst) 

lst = [1,2,3,4,5 , 9 ,7] 

f = max_in_list(lst)

print(f) 