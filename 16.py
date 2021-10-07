# QUESTOIN :

# 16. Write a function filter_long_words() that takes a list of words and an integer n
# and returns the list of words that are longer than n.

# Solution :

def filter_long_words(lst_of_words , n):
    lst_of_words_longer_than_n = [] 

    for item in lst_of_words:
        if (len(item) > n) :
            lst_of_words_longer_than_n.append(item) 

    return lst_of_words_longer_than_n

lst_of_words = ['hi' , 'hello' , 'how are u' , 'good'] 

# calling a function

f = filter_long_words(lst_of_words , 4) 

print(f) 