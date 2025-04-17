import numpy as np

# Function to compute modular inverse of a matrix
def get_mod_inverse(matrix, mod):
    determinant = int(np.round(np.linalg.det(matrix))) % mod
    determinant_inverse = pow(determinant, -1, mod)  # Compute modular inverse
    adjugate_matrix = np.round(determinant * np.linalg.inv(matrix)).astype(int) % mod
    return (determinant_inverse * adjugate_matrix) % mod

# Function for Hill Cipher encryption
def encrypt_message(text, key_matrix):
    mod_val = 26
    size = len(key_matrix)

    # Padding the text to match key matrix size
    while len(text) % size != 0:
        text += 'Z'  # Using 'Z' as padding instead of 'X'

    # Convert text to numerical values (A=0, B=1, ..., Z=25)
    text_numbers = [ord(letter) - ord('A') for letter in text.upper()]
    encrypted_numbers = []

    # Encrypt in blocks
    for i in range(0, len(text_numbers), size):
        block = np.array(text_numbers[i:i+size])
        encrypted_block = np.dot(key_matrix, block) % mod_val
        encrypted_numbers.extend(encrypted_block)

    # Convert encrypted numbers back to letters
    encrypted_text = ''.join(chr(num + ord('A')) for num in encrypted_numbers)
    return encrypted_text

# Function for Hill Cipher decryption
def decrypt_message(cipher_text, key_matrix):
    mod_val = 26
    size = len(key_matrix)

    # Compute modular inverse of key matrix
    try:
        key_inverse = get_mod_inverse(key_matrix, mod_val)
    except ValueError:
        return "Error: Key matrix is not invertible modulo 26."

    # Convert ciphertext to numerical values
    cipher_numbers = [ord(letter) - ord('A') for letter in cipher_text.upper()]
    decrypted_numbers = []

    # Decrypt in blocks
    for i in range(0, len(cipher_numbers), size):
        block = np.array(cipher_numbers[i:i+size])
        decrypted_block = np.dot(key_inverse, block) % mod_val
        decrypted_numbers.extend(decrypted_block)

    # Convert decrypted numbers back to letters
    decrypted_text = ''.join(chr(num + ord('A')) for num in decrypted_numbers)
    return decrypted_text

# Example Usage
if __name__ == "__main__":
    # Changed key matrix
    key_matrix = np.array([[3, 10, 20], [11, 9, 4], [20, 17, 15]])  # New 3x3 key
    message = "SECRET"

    encrypted_text = encrypt_message(message, key_matrix)
    print(f"Encrypted Message: {encrypted_text}")

    decrypted_text = decrypt_message(encrypted_text, key_matrix)
    print(f"Decrypted Message: {decrypted_text}")
