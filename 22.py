# QUESTION :

# 22. In cryptography, a Caesar cipher is a very simple encryption techniques in which each letter
# in the plain textis replaced by a letter some fixed number of positions down the alphabet. 
# For example, with a shift of 3, Awould be replaced by D, B would become E, and so on.
# The method is named after Julius Caesar, whoused it to communicate with his generals.
# ROT­13 ("rotate by 13 places") is a widely used example of aCaesar cipher where the shift is 13.
# In Python, the key for ROT­13 may be represented by means of thefollowing dictionary:
# key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t','h':'u', 
# 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b','p':'c',
# 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j','x':'k', 
# 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R','F':'S',  
# 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z','N':'A', 
# 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H','V':'I', 
# 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
# Your task in this exercise is to implement an encoder/decoder of ROT­13. 
# Once you are done, you will beable to read the following secret message:   
# Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!Note that since English has 26 characters, 
# your ROT­13 program will be able to both encode and decodetexts written in English

# Solution :

from string import punctuation

while True:
    try:
    
        # function for encoding
        def encoder(sentence , enc) :
            str_sen = ''
            sentence = sentence.split() 

            for i in range(len(sentence)):
                str_sen +=  sentence[i]

                for j in sentence[i] :    
                    if j in str(punctuation):
                        str_sen = str_sen.replace(j, j)
                    
                    elif j in enc :
                        str_sen = str_sen.replace(j , enc[j]) 

            return str_sen 

        # function for decodng :
        def decoder(encryp_sentence , dec) :
            str_encryp_sentence = ''
            encryp_sentence = encryp_sentence.split()

            for m in range(len(encryp_sentence)) :
                str_encryp_sentence += encryp_sentence[m]

                for n in encryp_sentence[m] :
                    if n in str(punctuation):
                        str_encryp_sentence = str_encryp_sentence.replace(n, n)  
                    
                    elif n in dec :
                        str_encryp_sentence = str_encryp_sentence.replace(n, dec[n]) 


            return str_encryp_sentence


        # dictionary for encoding :

        rot13 = {' ':' ', 'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t','h':'u', 
        'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b','p':'c',
        'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j','x':'k', 
        'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R','F':'S',  
        'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z','N':'A', 
        'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H','V':'I', 
        'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

        # dictionary for decoding :
        rot13_decoding = {}

        for l , m in rot13.items() :
            rot13_decoding[m] = l 

        # asking the user for encode or decode :

        ques = input('''---> Type encode for encoding the sentence :\n
---> Type decode for decoding the sentence :\n
---> Type cancel to exit the program : \n''') 


        # conditions to continue the program according to the input of user:

        if (ques.lower()  == 'cancel') :
            exit() 

        elif(ques.lower() == 'encode') :
            user_input = input('Enter a sentece : \n')

            f = encoder(user_input , rot13)

            print(f) 

        elif(ques.lower() == 'decode') :
            user_input = input('Enter a sentece : \n')

            f = decoder(user_input , rot13_decoding)

            print(f) 

        else :
            print('*****Please enter the correct input*****') 


    except Exception as e :
        print(f'you got "{e}" Error!') 
        