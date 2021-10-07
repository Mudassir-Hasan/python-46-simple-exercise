# QUESTION :

# 38. Write a program that will calculate the average word length of a text stored in a file 
# (i.e the sum of all thelengths of the word tokens in the text, divided by the number of word tokens).

# Solution :

def calculator (fileName) :
    with open(fileName , 'r') as f :
        content = f.read() 
    l = []
    lst = content.split() 
    for item in lst :
        l.append(len(item))

    avg = sum(l) / len(l) 

    return f'The average of length of words in given file is {int(avg)}'
 


print(calculator('38.text') )