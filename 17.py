# QUESTION :

# 17. Write a version of a palindrome recognizer that also accepts phrase palindromes 
# such as "Go hang asalami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", 
# "Sit on a potato pan, Otis", "Lisa Bonetate no basil", "Satan, oscillate my metallic sonatas", 
# "I roamed under it as a tired nude Maori", "Rise to votesir", or the exclamation "Dammit, I'm mad!". 
# Note that punctuation, capitalization, and spacing are usuallyignored.

# Solution :
import string

def palindrome(sen) :
  
    unwanted = list(string.punctuation + ' ') 
# loop for ignore punctuations:
    
    for i in sen:
        
        if i in unwanted:
            sen = sen.replace(i , '')  

# to chech whether it is palindrome or not:
    sen = sen.lower() 

    new_sen = sen[ ::-1] 

    if (sen == new_sen) :
        return True
    
    else:
        return False 

sen = input('enter a sentence : ') 

# calling a function:

f = palindrome(sen) 

print(f) 