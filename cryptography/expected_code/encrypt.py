#File description – this file will be our “encryptor” 
#Here we will go from a message in regular english - to a secret encrypted message
#Note: our 'key' is the number of spaces our letters will be shifted down


#define a function called “caesar_encrypt” with the parameters message and key 
def caesar_cypher(message, key):
    #define a string with the name “encrypted” that stores an empty string (this is where we will store our secure message) 
    encrypted = ""

    #start a for loop that goes through all the letters in the message (hint: the structure for this is ‘for _ in string’) 
    for letter in message:

        #check if the letter is lowercase using the .islower() function 
        if(letter.islower()):
            #get position of the current letter in the ASCII table by using the ‘ord()’ method and subtracting the position of the character ‘a’ (this will give us the position of the letter, as if we were just looking at the alphabet) 
            position = ord(letter) - ord('a')

            #shift the letters by adding the index that you got as a parameter to the position of the letter you just got above 
            position = position + key

            #get the remainder of this value divided by 26 (hint: use modulo - ‘%’) 
            position = position % 26

            #add back the position of ‘a’ within the ASCII table (hint: use ord(‘a’)) 
            position = position + ord('a')

            #add the shifted letter to the string variable you made up above
            encrypted = encrypted + chr(position)    

        #check if the letter is an upper-case letter by using the method .isupper()  
        elif(letter.isupper()):
            #repeat the shifting process that you did for lowercase letters, but replace ord(‘a’) with ord(‘A’), since the uppercase letters are at a different spot on the ASCII table 
            #get position of the current letter in the ASCII table by using the ‘ord()’ method and subtracting the position of the character ‘A’ (this will give us the position of the letter, as if we were just looking at the alphabet) 
            position = ord(letter) - ord('A')

            #shift the letters by adding the index that you got as a parameter to the position of the letter you just got above 
            position = position + key

            #get the remainder of this value divided by 26 (hint: use modulo - ‘%’) 
            position = position % 26

            #add back the position of ‘A’ within the ASCII table (hint: use ord(‘A’)) 
            position = position + ord('A')

            #add the shifted letter to the string variable you made up above
            encrypted = encrypted + chr(position)     

        #add one last case – if the letter is not uppercase or lowercase, this means that it is a special character (space, ‘-’, ‘:’) 
        #if this is the case – just add it to the string variable you made to store your secret message
        else:
            encrypted = encrypted + letter 

    #return the message
    return encrypted
