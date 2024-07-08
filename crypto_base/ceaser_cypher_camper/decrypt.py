#File description – this file will be our “decryptor” 
#Here we will go from the secret encrypted message to regular english
#Note: use the same key to encrypt it, as you did you decrypt it


#define a function called “caesar_decrypt” with the parameters encrypted and key 

    #define a string with the name “encrypted” that stores an empty string (this is where we will store our secure message) 

    #start a for loop that goes through all the letters in the message (hint: the structure for this is ‘for _ in string’) 

        #check if the letter is lowercase using the .islower() function 

            #get position of the current letter in the ASCII table by using the ‘ord()’ method and subtracting the position of the character ‘a’ (this will give us the position of the letter, as if we were just looking at the alphabet) 

            #shift the letters by subtracting the index that you got as a parameter to the position of the letter you just got above 

            #get the remainder of this value divided by 26 (hint: use modulo - ‘%’) 

            #add back the position of ‘a’ within the ASCII table (hint: use ord(‘a’)) 

            #add the shifted letter to the string variable you made up above   

        #check if the letter is an upper-case letter by using the method .isupper()  

            #repeat the shifting process that you did for lowercase letters, but replace ord(‘a’) with ord(‘A’), since the uppercase letters are at a different spot on the ASCII table 

        #add one last case – if the letter is not uppercase or lowercase, this means that it is a special character (space, ‘-’, ‘:’) 
        #if this is the case – just add it to the string variable you made to store your original message

    #return the original message