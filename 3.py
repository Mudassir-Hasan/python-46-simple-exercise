# QUESTION :

# 3. Define a function that computes the length of a given list or string. (It is true that Python has the len()
# function built in, but writing it yourself is nevertheless a good exercise.)


# Solution : 

def Len(lst) :
    len_of_lst = 0 

    for items in lst:
        len_of_lst += 1

    return len_of_lst

lst = 'stri'

f = Len(lst) 

print(f) 