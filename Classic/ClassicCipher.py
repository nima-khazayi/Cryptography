import sys
from pathlib import Path
from math import *

def ceasar(plain, c, crypt):

    cipher = open(c, "w")
    text = ""
    try:
        key = int(input("Enter your Key: "))
        key = key % 26

    except ValueError:
        ceasar(plain, c, crypt)

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
    text = ""
    try:
        a, b = input("Your key should be integer\nAs a(plain) + b; gcd(a, 26) must equal to 1\nEnter your desire key: ").split()
        a = int(a)
        b = int(b)
        if gcd(a, 26) != 1:
            raise ValueError
    
    except ValueError:
        affine(plain, c, crypt)

    A = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    a_prime = [1, 9, 21, 15, 3, 19, 7, 23, 11, 5, 17, 25]

    match crypt:

        case "-e":
            for i in plain:
                if i.isalpha():
                    if i.islower():
                        index = ord(i) - 96
                        index = a * index + b
                        index = index % 26
                        if index == 0:
                            string = chr(122)
                            text += string

                        else:
                            string = chr(index + 96)
                            text += string
                    
                    elif i.isupper():
                        index = ord(i) - 64
                        index = a * index + b
                        index = index % 26
                        if index == 0:
                            string = chr(90)
                            text += string

                        else:
                            string = chr(index + 64)
                            text += string
                else:
                    text += i

        case "-d":

            # Creating the decryption key as we need a^(-1) 
            # Which will calculate from A & a_prime lists by matching the index of the list
            for k in range(len(A)):
                if A[k] == a:
                    a = a_prime[k]

            for i in plain:
                if i.isalpha():
                    if i.islower():
                        index = ord(i) - 96
                        index = a * (index - b)
                        index = index % 26
                        if index == 0:
                            string = chr(122)
                            text += string

                        else:
                            string = chr(index + 96)
                            text += string
                    
                    elif i.isupper():
                        index = ord(i) - 64
                        index = a * (index - b)
                        index = index % 26
                        if index == 0:
                            string = chr(90)
                            text += string

                        else:
                            string = chr(index + 64)
                            text += string
                else:
                    text += i
            
    cipher.write(text)

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

