# QUESTION : 

# 20. Represent a small bilingual lexicon as a Python dictionary in the following fashion 
# {"merry":"god","christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"}
# and use it to translate your Christmas cards from English into Swedish. That is, 
# write a function translate()that takes a list of English words and returns a list of Swedish words.

# Solution :

dictionary = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}

def translate(lst) :
    list_of_swedish_words = [] 
    for words in lst :
        if words.lower() in dictionary :
            list_of_swedish_words.append(dictionary[words.lower()]) 

    return list_of_swedish_words  

# calling a function:

f = translate(['Merry', 'christmas', 'and', 'happy', 'new', 'year'])

print(f) 