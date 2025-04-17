def rail_fence_encrypt(message, key):
    cipher_text = ""
    c = 0
    r = 0
    i = 0
    down = True
    matrix = [[None for _ in range(len(message))] for _ in range(key)]
    
    while c < len(message):
        matrix[r][c] = message[i]
        r = r + 1 if down else r - 1

        down = True if r == 0 else False

        c += 1
        i += 1

    print("Encryption Table:")
    for row in matrix:
        print(row)

    for row in matrix:
        for item in row:
            if item is not None:
                cipher_text += item
    return cipher_text


def rail_fence_decrypt(cipher_text, key):
    decrypted_message = ['' for _ in range(len(cipher_text))]
    c = 0
    r = 0
    i = 0
    down = True
    matrix = [['' for _ in range(len(cipher_text))] for _ in range(key)]

    while c < len(cipher_text):
        matrix[r][c] = '*'
        r = r + 1 if down else r - 1

        down = True if r == 0 else False

        c += 1
        i += 1

    print("\nDecryption Table (after placement of characters):")
    idx = 0
    for row in range(key):
        for col in range(len(cipher_text)):
            if matrix[row][col] == '*' and idx < len(cipher_text):
                matrix[row][col] = cipher_text[idx]
                idx += 1

    for row in matrix:
        print(row)

    r = 0
    c = 0
    down = True
    for i in range(len(cipher_text)):
        decrypted_message[i] = matrix[r][c]
        r = r + 1 if down else r - 1

        down = True if r == 0 else False
        c += 1

    return ''.join(decrypted_message)


def main():
    message = input("Enter the message to encrypt: ")
    key = int(input("Enter the number of rails (key): "))
    
    encrypted_message = rail_fence_encrypt(message, key)
    print(f"\nEncrypted Message: {encrypted_message}")
    
    decrypted_message = rail_fence_decrypt(encrypted_message, key)
    print(f"\nDecrypted Message: {decrypted_message}")


# Run main function
main()
