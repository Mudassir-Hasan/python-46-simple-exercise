# QUESTION :

# 15. Write a function find_longest_word()that takes a list of words and returns the length of the longest
# one.

# Solution :

def find_longest_word(lst) :
    new_lst = []

    for i in range(len(lst)) :
        new_lst.append(len(lst[i])) 

    new_lst.sort() 

    return new_lst[-1] 

lst = ['hi' , 'hello' , 'oh'] 

# calling a function :

f = find_longest_word(lst) 

print(f) 