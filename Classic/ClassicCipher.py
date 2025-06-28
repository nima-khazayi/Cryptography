import sys
from pathlib import Path

def ceasar(plain, c, crypt):

    cipher = open(c, "w")
    text = ""
    key = int(input("Enter your Key: "))
    key = key % 26
    match crypt:

        case "-e":
            for i in plain:
                if i.isalpha():
                    if i.islower():
                        index = ord(i) + key
                        if index <= 122:
                            text += chr(index)

                        else:
                            text += chr(96 + (index % 122))

                    elif i.isupper():
                        index = ord(i) + key
                        if index <= 90:
                            text += chr(index)

                        else:
                            text += chr(64 + (index % 90))
                
                else:
                    text += i
        
        case "-d":
            for i in plain:
                if i.isalpha():
                    if i.islower():
                        index = ord(i) - key
                        if index >= 97:
                            text += chr(index)

                        else:
                            text += chr(122 - (96 % index))

                    elif i.isupper():
                        index = ord(i) - key
                        if index >= 65:
                            text += chr(index)

                        else:
                            text += chr(90 - (64 % index))
                
                else:
                    text += i

    cipher.write(text)

def affine(plain, c, crypt):
    
    cipher = open(c, "w")
    cipher.write(plain)

def main(p, c, crypt):

    plain = open(p, "r")
    plain = plain.read()
    print("Choose your method:")
    print("1.Ceasar Cipher")
    print("2.Affine Cipher")
    method = int(input("Your choice is: "))
    match method:

        case 1:
            ceasar(plain, c, crypt)

        case 2:
            affine(plain, c, crypt)

try:
    if sys.argv[1] == "--help":

        print("\nUsage of this Cryptography program is like:\n    -e/-d InputFile.txt OutputFile.txt\n    -e for encryption\n    -d for decryption\n")
        sys.exit()

    elif Path(sys.argv[2]).suffix.lower() != ".txt" or Path(sys.argv[3]).suffix.lower() != ".txt":
        
        print("I/O files should be in *.txt format!")
        sys.exit()

    elif sys.argv[1] != "-e" and sys.argv[1] != "-d":

        print("Use --help to get help")
        sys.exit()

except IndexError:
    print("There are not enough arguments! (use --help)")
    sys.exit()

except FileNotFoundError:
    print("Input file does not exist in this directory! (use -help)")
    sys.exit()

except EOFError:
    print("Program has been halted as you wished")
    sys.exit()

main(sys.argv[2], sys.argv[3], sys.argv[1])
