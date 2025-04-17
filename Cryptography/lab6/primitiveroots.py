def primitive_roots(p):
    roots = []  # List to store primitive roots

    for item in range(1, p):  # Check numbers from 1 to p-1
        gen_num = set()  # Use a set to store unique values
        for i in range(1, p):  # Exponents from 1 to p-1
            gen_num.add((item ** i) % p)  # Compute (item^i) % p
        
        # If the set contains all numbers from 1 to p-1, it's a primitive root
        if len(gen_num) == p - 1:
            roots.append(item)

    return roots

# Example usage:
p = int(input("Enter a number "))  # Prime number
print(f"Primitive roots of {p}:", primitive_roots(p))
