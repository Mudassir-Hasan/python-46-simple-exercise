# QUESTION :

# 34. Write a procedure char_freq_table() that, when run in a terminal,
#  accepts a file name from the user,
#  builds a frequency listing of the characters contained in the file,
#  and prints a sorted and nicely formattedcharacter frequency table to the screen.

# Solution :

def char_freq_table(fileName): 
    
    frequency = {}
    with open (f'{fileName}.text' , 'r') as f :
        content = f.read() 
        # changing the file type:
        str(content) 
        # converting the contents into list:
        content = content.split() 
        # sorting the elements of lists :
        content.sort() 

        # checking the frequency of alphabets :

    
    for i in content:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return frequency



file = input('enter the file name : ') 

f = char_freq_table(file) 
print(f) 

