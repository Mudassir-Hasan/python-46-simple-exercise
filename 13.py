# QUESTION :

# 13. The function max()from exercise 1) and the function max_of_three()from exercise 2) will only work for
# two and three numbers, respectively. But suppose we have a much larger number of numbers, or suppose
# we cannot tell in advance how many they are? Write a function max_in_list()that takes a list of
# numbers and returns the largest one.

# Solution :

from functools import reduce

def max_in_list(lst) :

    lst.sort()

    return lst[-1] 

lst = [1,2,3,4,6,7,43,54,67,46346,78,0,8]

# calling a function

f = max_in_list(lst) 

print(f) 

#--> by using the higher built in map function:
 
def max_in_lst(new_lst) :

    def max_in_two(a,b) :

        if (a>b):
            return a 
        
        else:
            return b

    return reduce(max_in_two , new_lst) 

#calling a function:

print(max_in_lst([1,2,3,4,6,7,43,54,67,46346,78,0,8]))

# --> 3 by using simply for loop 

def max_in_lis(List) :

    max_number = 0

    for item in List:
        
        if (item > max_number) :
            max_number = item 

    return max_number 

#calling a function :

f = max_in_lis([1,2,3,4,6,7,43,54,67,46346,78,0,8])

print(f)  



# to check the greater number in two lists:

def max_in_two_lists(lst1, lst2) :
    max_num = 0 
    lst2.extend(lst1) 
    print(lst2) 

    for items in lst2:

        if (items > max_num ) : 
            max_num = items 

    return max_num 


list1 = [1,2,3,4,5] 
list2 = [6,7,8,9,10] 

print(max_in_two_lists(list1 , list2)) 
