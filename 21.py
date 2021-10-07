# QUESTION :

# 21. Write a function char_freq() that takes a string and 
# builds a frequency listing of the characters containedin it. 
# Represent the frequency listing as a Python dictionary.
# Try it with something likechar_freq("abbabcbdbabdbdbabababcbcbab")

# Solution : 
    
def char_freq(Str):
  frequency = {}
  for i in Str:
    if i in frequency:
      frequency[i] += 1
    else:
      frequency[i] = 1
  return frequency

f = char_freq("abbabcbdbabdbdbabababcbcbab")

print(f) 
