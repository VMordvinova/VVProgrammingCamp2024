import encrypt
import decrypt

def main():
    #welcome message
    print("Welcome to the Caesar Cypher Encryptor! Press enter to start!")
    input()


    #looping until user would like to exit the program
    while True:

        #asking the user for 
        print("Please enter the message you would like to encrypt:", end = " ")
        message = input()

        print("Please enter the key that you would like to use:", end = " ")
        key = int(input())

        #variable to hold the encrypted message
        encrypted_message = encrypt.caesar_encrypt(message, key)

        #printing their encrypted message
        print("\nHere is your encrypted message: " + encrypted_message)

        #printing a version of their encrypted message, put through their decryptor
        print("\nHere is your message, as decrypted by your decryptor (the message should match your original message): " +decrypt.caesar_decrypt(encrypted_message, key))

        #asking if they would like to encrypt something else
        print("\nWould you like to encrypt something else? (y/n)", end = " ")
        if(input() != 'y'):
            print("\n~~~ Thank you for using our program! ~~~~")
            break
        else:
            print(('-' * 25) + "\n")
        
main()