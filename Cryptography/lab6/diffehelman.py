from random import randint

class User:
    def __init__(self, p, g) -> None:
        self.p = p  # Store p as an instance variable
        self.private = randint(1, p)
        self.public = pow(g, self.private, p)

    def get_public_key(self):
        return self.public

    def get_shared_key(self, public_key):
        return pow(public_key, self.private, self.p)  # Use self.p instead of p

def main():
    p = 23  # Prime modulus
    g = 5   # Primitive root

    alice = User(p, g)
    bob = User(p, g)

    Ya = alice.get_public_key()  # Alice's public key
    Yb = bob.get_public_key()    # Bob's public key

    Ska = alice.get_shared_key(Yb)  # Alice computes shared key
    Skb = bob.get_shared_key(Ya)    # Bob computes shared key

    print("Alice's public key:", Ya)
    print("Bob's public key:", Yb)
    print("Alice's shared key:", Ska)
    print("Bob's shared key:", Skb)

main()
