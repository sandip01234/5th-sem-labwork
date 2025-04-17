from random import randint
import math

def miller_rabin(n, a):
    if n % 2 == 0:  # Directly check for even numbers
        return n == 2  # Only 2 is prime, all other even numbers are composite

    k = 0
    m = n - 1
    while m % 2 == 0:
        m //= 2
        k += 1

    T = pow(a, m, n)  # Compute (a^m) % n
    if T == 1 or T == n - 1:
        return True

    for _ in range(k - 1):
        T = pow(T, 2, n)  # Compute (T^2) % n
        if T == 1:
            return False
        if T == n - 1:
            return True

    return False

def main():
    n = 4  
    a = 2  
    
    if n < 2:
        print(n, "is neither prime nor composite")
        return

    if miller_rabin(n, a):
        print(n, "is a prime number")
    else:
        print(n, "is a composite number")

main()
