# QUESTION :

# 14. Write a program that maps a list of words into a list of integers representing the lengths of the 
# correponding words.

# Solution :

def words_to_integar(lst) :
    new_lst = []

    for i in range(len(lst)) :
        new_lst.append(len(lst[i])) 

    return new_lst

lst = ['hi' , 'hello'] 

# calling a function :

f = words_to_integar(lst) 

print(f) 