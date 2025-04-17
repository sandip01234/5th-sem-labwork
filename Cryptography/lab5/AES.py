from Crypto.Cipher import AES
import binascii
import os

# Padding function to align input
def align_text(text):
    while len(text) % 16 != 0:
        text += ' '  # Space padding
    return text

# Encrypt using AES CBC mode
def aes_encode(text, passcode):
    passcode = passcode.ljust(16, b'\0')[:16]  # Ensure key is 16 bytes
    random_iv = os.urandom(16)  # Generate IV
    aes_cipher = AES.new(passcode, AES.MODE_CBC, random_iv)  # Create AES instance
    aligned_data = align_text(text).encode()  # Align input
    encrypted_data = aes_cipher.encrypt(aligned_data)  # Encrypt
    return binascii.hexlify(random_iv + encrypted_data).decode()  # Convert to hex

# Decrypt using AES CBC mode
def aes_decode(encrypted_text, passcode):
    passcode = passcode.ljust(16, b'\0')[:16]  # Ensure key is 16 bytes
    encrypted_text = binascii.unhexlify(encrypted_text)  # Convert back to bytes
    iv_block, cipher_block = encrypted_text[:16], encrypted_text[16:]  # Extract IV
    aes_cipher = AES.new(passcode, AES.MODE_CBC, iv_block)  # Create AES instance
    decrypted_output = aes_cipher.decrypt(cipher_block).decode().strip()  # Decrypt
    return decrypted_output

# Implementation Example
passkey = b"MySecureKey12345"  # AES requires a 16-byte key
plaintext_message = "AES Encryption Example!"

encrypted_result = aes_encode(plaintext_message, passkey)
print(f"Encrypted Data: {encrypted_result}")

decrypted_result = aes_decode(encrypted_result, passkey)
print(f"Decrypted Output: {decrypted_result}")
