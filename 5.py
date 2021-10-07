# QUESTION :

# 5. Write a function translate()that will translate a text into "rövarspråket" (Swedish for "robber's
# language"). That is, double every consonant and place an occurrence of "o"in between. For example,
# translate("this is fun")should return the string "tothohisos isos fofunon".

# Solution :

def translate(text):
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    new_text = ''
    
    for i in text :
    
        if (i in vowels) or (i==' '):
            new_text =  new_text+i 
    
        else:
            new_text = new_text + (i + 'o' + i)  

    return new_text

print(translate('this is fun'))
