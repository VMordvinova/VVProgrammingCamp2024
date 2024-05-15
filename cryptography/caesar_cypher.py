# creating a program that will encrypt/decrypt data using the ceaser cypher
# encryption alg  -> encrypted = (character + shift) % 26
# modeled after the example 

def caesar_encrypt(message, key):
    encrypted = ""

    for c in message:

        if c.islower():
            getting_index = ord(c) - ord('a') 
            shifting = (getting_index + key) % 26 + ord('a')
            encrypted += chr(shifting)

        elif c.isupper():
            getting_index = ord(c) - ord('A') 
            shifting = (getting_index + key) % 26 + ord('A')
            encrypted += chr(shifting)

        else:
            encrypted += c

    
    return encrypted

def caesar_decrypt(encrypted, key):
    message = ""

    for c in encrypted:

        if c.islower():
            getting_index = ord(c) - ord('a') 
            og_position = (getting_index - key) % 26 + ord('a')
            message += chr(og_position)

        elif c.isupper():
            getting_index = ord(c) - ord('A') 
            og_position = (getting_index - key) % 26 + ord('A')
            message += chr(og_position)

        else:
            message += c


    return message


#testing that the program works as intended
def main():
    print(caesar_decrypt(caesar_encrypt("slay", 2), 2))
    print(caesar_decrypt(caesar_encrypt("to be, or not to be - that is the question", 7), 7))
    print(caesar_decrypt(caesar_encrypt("VIRTUAL VENTURES", 3), 3))
    print(caesar_decrypt(caesar_encrypt("The year is currently... 2024", 4), 4))

main()
