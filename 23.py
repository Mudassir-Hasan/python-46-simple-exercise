# QUESTION :

# 23. Define a simple "spelling correction" function correct() that takes a string and sees to it that 1) 
# two ormore occurrences of the space character is compressed into one, and 2) 
# inserts an extra space after aperiod if the period is directly followed by a letter.
# E.g. correct("This   is  very funny  and   cool.Indeed!") 
# should return "This is very funny and cool. Indeed!" 
# Tip: Use regularexpressions!

# Solution :

def spell_correction(String) :
    String = String.replace("   " , " ")

    String = String.replace("  " , " ") 

    return String

f = spell_correction("This   is  very funny  and   cool.Indeed!") 

print(f)   