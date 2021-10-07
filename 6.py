# QUESTION :

# 6. Define a function sum()and a function multiply()that sums and multiplies (respectively) all the
# numbers in a list of numbers. For example, sum([1, 2, 3, 4])should return 10, and multiply([1,
# 2, 3, 4])should return 24.

# Solution : 

# function defination for sum

def Sum(lst):
    sum_of_items_in_lst = 0

    for item in lst:
        sum_of_items_in_lst += item

    return sum_of_items_in_lst

# function defination for multiplicatin

def Multiply(lst):
    mult_of_items_in_lst = 1

    for item in lst:
        mult_of_items_in_lst *= item

    return mult_of_items_in_lst    

# list
lst = [1,2,3,4] 

# 1st function call
f1 = Sum(lst) 

# 2nd function call
f2 = Multiply(lst) 

print(f1)  
print(f2)
