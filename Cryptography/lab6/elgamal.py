import random
from math import pow

class ElGamal:
    def __init__(self):
        self.q = random.randint(pow(10, 20), pow(10, 50))
        self.g = random.randint(2, self.q)
        self.private_key = self.generate_key()
        self.public_key = self.power(self.g, self.private_key, self.q)

    def gcd(self, a, b):
        if a < b:
            return self.gcd(b, a)
        elif a % b == 0:
            return b
        else:
            return self.gcd(b, a % b)

    def generate_key(self):
        key = random.randint(pow(10, 20), self.q)
        while self.gcd(self.q, key) != 1:
            key = random.randint(pow(10, 20), self.q)
        return key

    def power(self, a, b, c):
        x = 1
        y = a
        while b > 0:
            if b % 2 != 0:
                x = (x * y) % c
            y = (y * y) % c
            b = b // 2
        return x % c

    def encrypt(self, msg):
        k = self.generate_key()  # Private key for sender
        s = self.power(self.public_key, k, self.q)
        p = self.power(self.g, k, self.q)
        
        encrypted_msg = [s * ord(char) for char in msg]
        return encrypted_msg, p

    def decrypt(self, encrypted_msg, p):
        h = self.power(p, self.private_key, self.q)
        decrypted_msg = ''.join(chr(int(char / h)) for char in encrypted_msg)
        return decrypted_msg

    def display_keys(self):
        print(f"Public Key (g^a mod q): {self.public_key}")
        print(f"Private Key: {self.private_key}")

if __name__ == '__main__':
    elgamal = ElGamal()
    elgamal.display_keys()
    
    message = "iamironman"
    print("Original Message:", message)
    
    encrypted_msg, p = elgamal.encrypt(message)
    print("Encrypted Message:", encrypted_msg)
    
    decrypted_msg = elgamal.decrypt(encrypted_msg, p)
    print("Decrypted Message:", decrypted_msg)
