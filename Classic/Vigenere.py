import sys
from pathlib import Path

def main(p, c):

    plain = open(p, "r")
    plain = plain.read()
    try:
        # Take the key as input
        # Key must be all alphabetic string but could include empty spaces
        key = str(input("Assume that this algorithm uses string as key\nIt also should use only alphabets(upper or lower cases)\nEnter your desire key: "))
        for i in key:
            if not i.isalpha() and i != " ":
                raise ValueError # Check if the entered key satisfy needs

    except ValueError:
        main(p, c) # Otherwise call main function once again

    print("In what term you desire to use this program: (choose number)")
    print("1.Encryption")
    print("2.Decryption")
    crypt = int(input()) # What are we doing?

    text = ""
    length = len(key)
    counter = 0
    """
     There could be two different policies
     That if in our plain text is not alphabetic characters and numbers
     Should our key effects them or not?
     And if not :
           Should our key characters get over them, or assign to them?
    """
    # I decided to go on only with alphabetic characters
    # And not assigning key characters to non-alphabetic characters
    match crypt:

        case 1:

            for i in plain:
                if i.isalpha():
                    if i.islower():
                        index = ord(i) - 96 # Take each character ascii 
                                            # Re-order it in 26 alphabetic places
                        
                        # Giving the same places to the key characters
                        if key[counter].islower():
                            tmp = ord(key[counter]) - 96

                        elif key[counter].isupper():
                            tmp = ord(key[counter]) - 64

                        elif key[counter] == " ":
                            tmp = 0

                        index = (index + tmp) % 26
                        if index == 0:
                            string = chr(122)

                        else:
                            string = chr(index + 96)

                        print(string, i, tmp)
                        text += string
                        counter = (counter + 1) % length

                    elif i.isupper():
                        index = ord(i) - 64 # Take each character ascii 
                                            # Re-order it in 26 alphabetic places
                        
                        # Giving the same places to the key characters
                        if key[counter].islower():
                            tmp = ord(key[counter]) - 96

                        elif key[counter].isupper():
                            tmp = ord(key[counter]) - 64

                        elif key[counter] == " ":
                            tmp = 0

                        index = (index + tmp) % 26
                        if index == 0:
                            string = chr(90)
                            
                        else:
                            string = chr(index + 64)

                        text += string
                        counter = (counter + 1) % length

                else:
                    text += i

        case 2:

            for i in plain:
                if i.isalpha():
                    if i.islower():
                        index = ord(i) - 96 # Take each character ascii 
                                            # Re-order it in 26 alphabetic places
                        
                        # Giving the same places to the key characters
                        if key[counter].islower():
                            tmp = ord(key[counter]) - 96

                        elif key[counter].isupper():
                            tmp = ord(key[counter]) - 64

                        elif key[counter] == " ":
                            tmp = 0

                        index = (index - tmp) % 26
                        if index == 0:
                            string = chr(122)
                            
                        else:
                            string = chr(index + 96)

                        text += string
                        counter = (counter + 1) % length

                    elif i.isupper():
                        index = ord(i) - 64 # Take each character ascii 
                                            # Re-order it in 26 alphabetic places
                        
                        # Giving the same places to the key characters
                        if key[counter].islower():
                            tmp = ord(key[counter]) - 96

                        elif key[counter].isupper():
                            tmp = ord(key[counter]) - 64

                        elif key[counter] == " ":
                            tmp = 0

                        index = (index - tmp) % 26
                        if index == 0:
                            string = chr(90)
                            
                        else:
                            string = chr(index + 64)

                        text += string
                        counter = (counter + 1) % length

                else:
                    text += i
        
    cipher = open(c, "w")
    cipher.write(text)
    
try:
    if sys.argv[1] == "--help":

        # Here is how to use the system arguments for this program
        print("\nUsage of this Cryptography program is like:\n    InputFile.txt OutputFile.txt")
        sys.exit()

    elif Path(sys.argv[1]).suffix.lower() != ".txt" or Path(sys.argv[2]).suffix.lower() != ".txt":
        
        print("I/O files should be in *.txt format!")
        sys.exit()

except IndexError: # Check if the argument values are passing correctly
    print("There are not enough arguments! (use --help)")
    sys.exit()

except FileNotFoundError: # Check if the input text file even exists
    print("Input file does not exist in this directory! (use -help)")
    sys.exit()

except EOFError:
    print("Program has been halted as you wished")
    sys.exit()

main(sys.argv[1], sys.argv[2]) # Pass two input and output text files to the main function
