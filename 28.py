# QUESTION :

# 28. Write a function find_longest_word() that takes a list of words and returns the length of the longestone.
# Use only higher order functions.

# Solution :

# def fing_longest_word(lst_of_words): 
#     def longest_in_two(x,y) :
#         if  


def fing_longest_word(words) :
    l = list(map(len , words) )
    l.sort() 

    return l[-1] 

print(f" The length of the longest word is {fing_longest_word(['hi' , 'hello'])}.") 
 
