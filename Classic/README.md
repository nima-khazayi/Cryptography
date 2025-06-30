# README for Cryptography programs
This repository contains two Python scripts that implement classical
cryptography algorithms: the Vigenere cipher and the Caesar/Affine cipher.
Each script allows for the encryption and decryption of text files.

## Vigenere Cipher ('Vigenere.py')

### Description
The Vigenere cipher is a method of encrypting alphabetic text using
a simple form of polyalphabetic substitution. A keyword is used to 
determine the shift for each letter in the plaintext.
Note that empty spaces in the plaintext are ignored, but empty spaces
in the key are important.

### Usage
To run the Vigenere cipher, use the following command in your terminal:

```bash
python Vigenere.py InputFile.txt OutputFile.txt
```
- Replace ```InputFile.txt``` with the path to your plaintext file.
- Replace ```OutputFile.txt``` with the desired output file for the ciphertext.

### Features
- Accepts a keyword for encryption/decryption.
- Handles both uppercase and lowercase letters.
- Ignores non-alphabetic characters.

### Example
1. Input: ```HELLO WORLD```
2. Key: ```KEY```
3. Output: ```RIJVS UYVJN```

### Error Handling
- The program checks for valid input files and ensures the keyword only contains alphabetic characters.

## Caesar/Affine Cipher ('Classic.py')

### Description
This script implements two classical ciphers:
the Caesar cipher and the Affine cipher.
The Caesar cipher shifts letters by a fixed number,
while the Affine cipher uses a linear transformation.

### Usage
To run the Caesar/Affine cipher, use the following command in your terminal:

```bash
python Classic.py -e/-d InputFile.txt OutputFile.txt
```
- Use ```-e``` for encryption or ```-d``` for decryption.
- Replace ```InputFile.txt``` with the path to your plaintext file.
- Replace ```OutputFile.txt``` with the desired output file for the ciphertext.

### Features
- Supports both encryption and decryption.
- The Affine cipher requires a pair of integer keys(a,b) where ```gcd(a, 26) = 1```.

### Example
1. Input: ```HELLO```
2. Key: ```3```
3. Output: ```KHOOR```

### Error Handling
- Checks for valid input and key values.
- Provides usage instruction when requested.

## Requirements
- Python 3.x
- Access to the terminal/command line

## Contributions
Feel free to contribute by submitting issues or pull requests.
