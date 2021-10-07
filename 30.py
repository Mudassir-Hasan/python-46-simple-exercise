# QUESTION :

# 30. Represent a small bilingual lexicon as a Python dictionary in the following fashion
#  {"merry":"god","christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"} and 
#  use it to translate your Christmas cards from English into Swedish. 
# Use the higher order function map() to write a function translate() 
# that takes a list of English words and returns a list of Swedish words.

# Solution : 

dictionary = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"} 

def translate(lst) :
    trans = lambda a: dictionary[a.lower()] 

    return list(map(trans , lst)) 

# calling a function:

f = translate(['Merry', 'christmas', 'and', 'happy', 'new', 'year'])

print(f) 
