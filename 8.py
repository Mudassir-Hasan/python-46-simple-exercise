# QUESTION :

# 8. Define a function is_palindrome()that recognizes palindromes (i.e. words that look the same written
# backwards). For example, is_palindrome("radar")should return True.

# Solution : 

def is_palindrome(string):

    new_str = string[ ::-1] 

    if (new_str == string ) :
        return True

    else:
        return False 

# inputing a string

string = input('Enter a string to check is it palindrome or not : ')

# calling a function

f = is_palindrome(string)

print(f) 