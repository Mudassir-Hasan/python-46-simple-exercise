# QUESTION :

# 25. In English, the present participle is formed by adding the suffix ­ing to the infinite form: go ­> going. 
# A simpleset of heuristic rules can be given as follows:
# 1. If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
# 2. If the verb ends in ie, change ie to y and add ing
# 3. For words consisting of consonant-­vowel-­consonant, double the final letter before adding ing
# 4. By default just add ing
# Your task in this exercise is to define a function make_ing_form() 
# which given a verb in infinitive form returns its present participle form. 
# Test your function with words such as lie, see, move and hug.
# However,you must not expect such simple rules to work for all cases

# Solution :

def make_ing_form(form) :

    if (form.endswith('ie')) :
        form = form.replace(form[-2:: ] ,'y') 
        form += 'ing' 


    elif (form.endswith('e')) :
        if (form.endswith('ee')):
            form += 'ing' 
        else:
            form = form.replace(form[-1] ,'') 
            form += 'ing'  

    else:
        form += 'ing' 

    return form

# checking :

print(make_ing_form('be')) 
print(make_ing_form('flee')) 
print(make_ing_form('see')) 
print(make_ing_form('knee')) 



    