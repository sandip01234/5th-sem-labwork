import math

def additive_inverse(a, m):
    """Returns the additive inverse of 'a' modulo 'm'."""
    return (m - a) % m

def extended_gcd(a, b):
    """Returns the greatest common divisor of 'a' and 'b', and coefficients (x, y) for ax + by = gcd(a, b)."""
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def multiplicative_inverse(a, m):
    """Returns the multiplicative inverse of 'a' modulo 'm' (if it exists)."""
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError(f"{a} has no multiplicative inverse modulo {m}")
    return x % m

def is_relatively_prime(a, b):
    """Checks if 'a' and 'b' are relatively prime (i.e., gcd(a, b) = 1)."""
    g, _, _ = extended_gcd(a, b)
    return g == 1

def main():
    """Main function for input and output."""
    a = int(input("Enter the first number (a): "))
    m = int(input("Enter the modulus (m): "))

    print(f"Additive inverse of {a} modulo {m}: {additive_inverse(a, m)}")

    try:
        print(f"Multiplicative inverse of {a} modulo {m}: {multiplicative_inverse(a, m)}")
    except ValueError as e:
        print(e)

    print(f"Are {a} and {m} relatively prime? {is_relatively_prime(a, m)}")

if __name__ == "__main__":
    main()
