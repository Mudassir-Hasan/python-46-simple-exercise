# QUESTION :


# 18. A pangram is a sentence that contains all the letters of the English alphabet at least once,
# for example: The quick brown fox jumps over the lazy dog.
# Your task here is to write a function to check a sentence to see if itis a pangram or not

# Solution :
from string import punctuation
from string import ascii_lowercase

def pangram_or_not(sen) :

    for i in range(len(sen)):
        if sen[i] in str(punctuation) :
            sen = sen.replace(sen[i], '')

    sen = sen.lower() 
    
    set(sen) 

    eng_alph = set(ascii_lowercase)  

    if (len(sen) >= len(eng_alph)):
        return True
    else:
        return False 

# calling a function:

f = pangram_or_not('The quick brown fox jumps over the lazy dog.') 

print(f) 