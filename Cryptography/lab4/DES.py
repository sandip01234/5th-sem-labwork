from Crypto.Cipher import DES
import binascii

def pad(text):
    while len(text) % 8 != 0:
        text += ' '  # Padding with spaces
    return text

def des_encrypt(plain_text, key):
    cipher = DES.new(key.encode(), DES.MODE_ECB)
    padded_text = pad(plain_text)
    encrypted_text = cipher.encrypt(padded_text.encode())
    return binascii.hexlify(encrypted_text).decode()

def des_decrypt(cipher_text, key):
    cipher = DES.new(key.encode(), DES.MODE_ECB)
    decrypted_text = cipher.decrypt(binascii.unhexlify(cipher_text))
    return decrypted_text.decode().strip()

# Example Usage
message = "hey!"
key = "8CHARKEY"  # Key must be 8 characters long

encrypted_message = des_encrypt(message, key)
decrypted_message = des_decrypt(encrypted_message, key)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
