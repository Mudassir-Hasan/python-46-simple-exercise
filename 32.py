# QUESTION :

# 32. Write a version of a palindrome recogniser that accepts a file name from the user, reads each line, 
# and
# prints the line to the screen if it is a palindrome.

# Solution :

# here i created the file with the name of palindrome


file_name = input('enter the file name : ') 
try:
    with open(f'{file_name}.text', 'r') as f :
    
        lines = f.readlines() 

        for i in range(len(lines)) :
            l = str(lines[i]) 
            l = l.replace('\n', '') 
            l1 = l[ ::-1] 
            if (l==l1) :
                print(f'The line no {i+1} in {file_name} file which is {l} is "palindrome".' ) 
            else:
                print(f'The line no {i+1} in {file_name} file which is " {l} " is not a "palindrome".' ) 

 

except Exception as e:
    print(f'Here you got the "{e}".') 
