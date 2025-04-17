import random
from math import gcd

class RSA:
    def __init__(self, bit_length=16):
        self.p = self.generate_prime(bit_length)
        self.q = self.generate_prime(bit_length)
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = self.choose_e()
        self.d = self.mod_inverse(self.e, self.phi)
    
    def generate_prime(self, bit_length):
        while True:
            num = random.getrandbits(bit_length)
            if self.is_prime(num):
                return num
    
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def choose_e(self):
        e = 3
        while gcd(e, self.phi) != 1:
            e += 2
        return e
    
    def mod_inverse(self, a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1
    
    def encrypt(self, message):
        return [pow(ord(char), self.e, self.n) for char in message]
    
    def decrypt(self, encrypted_message):
        return ''.join(chr(pow(char, self.d, self.n)) for char in encrypted_message)
    
    def display_keys(self):
        print(f"Public Key: (e={self.e}, n={self.n})")
        print(f"Private Key: (d={self.d}, n={self.n})")

if __name__ == '__main__':
    rsa = RSA()
    rsa.display_keys()
    
    message = "IamIronMan"
    print("Original Message:", message)
    
    encrypted_msg = rsa.encrypt(message)
    print("Encrypted Message:", encrypted_msg)
    
    decrypted_msg = rsa.decrypt(encrypted_msg)
    print("Decrypted Message:", decrypted_msg)
