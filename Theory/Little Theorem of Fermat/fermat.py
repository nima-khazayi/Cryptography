"""
Little Theorem of Fermat:
    we have 2 different inputs {p, a}
    p: an integer Prime number   
    a: an integer which is not multiple of P 

    'we are about to find the modular inverse of a.'
"""

import math

def prime_checker(n):
    # Function returns true if the number is prime.
    for i in range(0, round(math.sqrt(n))):
        if n % (i + 1) == 0:
            return False
        
    return True

def multiple_checker(a, p):
    # Function returns true if the numbers are not each others multiple.
    if a % p == 0:
        return False
    
    return True

def power(a, p, m):
    
    if p == 0:
        return 1

    q = power(a, p // 2, m) % m
    q = (q * q) % m

    return q if (p % 2 == 0) else (a * q) % m

if __name__ == "__main__":

    p = int(input("Enter your desired integer Prime number: "))
    a = int(input("Enter your desired integer number which you want to find its modular inverse: "))

    if not(prime_checker(p) or multiple_checker(a, p)):
        print("The modulo inverse doesn't exist")

    print("Modular multiplicative inverse is ",
              power(a, p - 2, p))