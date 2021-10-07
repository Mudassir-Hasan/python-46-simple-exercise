# QUESTION :

# 24. The third person singular verb form in English is distinguished by the suffix ­s, 
# which is added to the stem ofthe infinitive form: run ­> runs.
# A simple set of rules can be given as follows:1. If the verb ends in y, remove it and add ies2. 
# If the verb ends in o, ch, s, sh, x or z, add es3. By default just add s
# 
# Your task in this exercise is to define a function make_3sg_form() 
# which given a verb in infinitive formreturns its third person singular form. 
# Test your function with words like try, brush, run and fix. 
# Note however that the rules must be regarded as heuristic, 
# in the sense that you must not expect them to work for allcases.
# Tip: Check out the string method endswith()

# Solution :

def make_3sg_form(verb) :

    if (verb.endswith('y')) :
        verb = verb.replace(verb[-1] , 'ies') 

    elif(verb.endswith('o') or verb.endswith('s')) :
        verb += 'es'

    elif(verb.endswith('ch') or verb.endswith('sh')) :
        verb += 'es'

    elif(verb.endswith('x') or verb.endswith('z')) :
        verb += 'es'

    else:
        verb +='s'

    return verb 

# checking:

print(make_3sg_form('try')) 
print(make_3sg_form('brush'))
print(make_3sg_form('run'))
print(make_3sg_form('fix'))
 