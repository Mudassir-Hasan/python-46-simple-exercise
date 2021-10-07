# QUESTION :

# 29. Using the higher order function filter(), define a function filter_long_words() 
# that takes a list of words and an integer n and returns the list of words that are longer than n.

# Solution :

def filter_long_words(words , n) :

    filt = lambda words: len(words) > n

    return list(filter(filt , words)) 


list_of_words = ['hi' , 'hello'] 

# calling a function:

f = filter_long_words(list_of_words, 4) 

print(f) 


