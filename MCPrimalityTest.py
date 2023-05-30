"""
Monte Carlo Miller-Rabin Primality Test

Author: Mattia Cacciatore <cacciatore1995@hotmail.it>
"""
import math
import numpy as np
import random as rd
# ------------------------------ FUNCTIONS ---------------------------------
def mygcd(m,n):
    return math.gcd(m,n)

def make_multiplicative_group(n):
    # Quotient set
    Z_n = np.array([])
    # 'a' is a base
    for a in range(n):
        if(mygcd(a,n) == 1):
            Z_n = np.append(Z_n, a);
    return Z_n

def modular_exponentiation(b, e, m):
    # Result
    r = 1
    # Calculate (b^e) mod m
    while(e > 0):
        if((e % 2) == 1):
            r = ((r * b) % m)
        e = e // 2
        b = ((b * b) % m)
    return r

def primality_test(n, a):
    # 'a' is the base
    if(n < 3 or (n % 2) == 0):
        return "n not valid"
    
    s = 0
    q = n - 1

    while((q % 2) == 0):
        s = s + 1
        q = q / 2
    # Modular_exponentation so your device can handle big numbers.
    x = modular_exponentiation(a,q,n)

    if(x == 1 or x == -1):
        return "probably prime"
    
    while((s-1) >= 0):
        # Checking square roots, better than Fermat test.
        # Carmichael numbers aren't a problem.
        x = ((x**2)%n)
        if((x%n) == -1):
            return "probably prime"
        s = (s - 1)

    return "composite" # else

def MC_Miller_Rabin_test(n):
    # random choice of the base 'a' between 2 and n-1
    a = rd.randint(2, n-1)
    return primality_test(n,a)

def main():
    no_tests = input("Enter the number of attempts: ")
    n = input("Enter the number: ")
    # Upper bound error : 1/(4^no_tests) < (n-1)/2
    for i in range(int(no_tests)):
        print(str(n) + " is " + MC_Miller_Rabin_test(int(n)))


if __name__ == "__main__":
    main()
