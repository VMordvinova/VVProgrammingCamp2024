import ceaser_cypher as c

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

        #printing their encrypted message
        print("\nHere is your encrypted message: " + c.caesar_encrypt(message, key))

        #asking if they would like to encrypt something else
        print("\nWould you like to encrypt something else? (y/n)", end = " ")
        if(input() != 'y'):
            print("\n~~~ Thank you for using our program! ~~~~")
            break
        else:
            print(('-' * 25) + "\n")


main()
    