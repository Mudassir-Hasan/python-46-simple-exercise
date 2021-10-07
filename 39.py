# QUESTION :

# 39. Write a program able to play the "Guess the number"­game, 
# where the number to be guessed is randomlychosen between 1 and 20. 
# (Source: http://inventwithpython.com) This is how it should work when run in aterminal:
# >>> import guess_number
# Hello! What is your name?
# Torbjörn
# Well, Torbjörn, I am thinking of a number between 1 and 20.
# Take a guess.
# 10 
# Your guess is too low.
# Take a guess.
# 15
# Your guess is too low.
# Take a guess.
# 18
# Good job, Torbjörn! You guessed my number in 3 guesses

# Solution :


# random numbers
import random 
num1 = random.randint(1,20) 
 
print('\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~\n\t\t\t\tGuess the number, game\n\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~') 


# getting the name of user 
name = input('Hello! What is your name? ')
print(f'Well, {name}, I am thinking of a number between 1 and 20.' )

# loop for continuouety
while(True) :

    try:

       # taking the number from the user :

       num2 = int(input('''\t\t\t____________
       \t\t\tTake a guess :
       \t\t\t____________\n\t\t\t    ''')) 
       

       # conditions for checking and result 

        
       if (num2<num1 and num2>=1) :
           print('_________________________________')
          
           print('Your guess is too lower')
          
           print('_________________________________')

       elif (num2>num1 and num2>20) :
           print('__________________________________')
          
           print('Your guess is too higher')
          
           print('__________________________________') 
       
       elif (num1 == num1) :
           print(f'Good job, {name}! You guessed my number in {num1} guesses\n')     
          
           print('_____Thanks for playing this game_____ \n')
          
           break


    except Exception as e :
        print(f'you got the {e} Error')


 