# QUESTION :

# 27. Write a program that maps a list of words into a list of integers representing the lengths of 
# the correpondingwords. Write it in three different ways:
# 1) using a for­loop, 2) using the higher order function map(), and 3)using list comprehensions.

# Solution :

# using for loop:

lst_of_words = ['hi' , 'hello' , 'how are u'] 
lst_of_lengths = [] 

for i in lst_of_words :
    lst_of_lengths.append(len(i)) 

print(f'The list of lengths of list of words by using for loop is {lst_of_lengths}') 

# using map() function : 

def length_of_words(list_of_words) :
    return list(map(len , list_of_words))  

F = length_of_words(['hi' , 'hello' , 'how are u']) 

print(f"The list of length of list of words by using the map() function is {F}" ) 

# using list comprehensions

list_of_word = ['hi' , 'hello' , 'how are u'] 

list_of_length = [len(i) for i in list_of_word ] 

print(f"The list of length of list of words by using the list comprehension is {list_of_length}") 