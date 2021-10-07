# QUESTION :

# Write a function that takes a character (i.e. a string of length 1) and returns True
# if it is a vowel, False otherwise.

# Solution : 

def fun(char) :

    vowels = ['a' , 'e' , 'i' , 'o' , 'u' ] 

    if char in vowels:
        return True
    
    else:
        return False 

# inputing a character
char = input('Enter a Character : ')  

f = fun(char)

print(f) 