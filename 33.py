# QUESTION :

# 33. According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase backwards.
# ("Semordnilap" is itself "palindromes" spelled backwards.) 
# Write a semordnilap recogniser that accepts a filename (pointing to a list of words) 
# from the user and finds and prints all pairs of words that are semordnilaps
# to the screen. For example, if "stressed" and "desserts" is part of the word list, 
# then the output should include the pair "stressed desserts".
# Note, by the way, that each pair by itself forms a palindrome!

# Solution :

lst = [] 
with open('semordnilap.text' , 'r') as f :
    contents = f.readlines() 

for line in contents :
    line = line.strip() 
    lst.append(line) 

for word in lst:
    reverse = word[ ::-1] 
    
    if reverse in lst:
        print(f'{word} and {reverse} ')  