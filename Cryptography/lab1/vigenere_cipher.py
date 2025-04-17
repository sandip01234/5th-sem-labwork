def adjust_key(text, key):
    key = key.upper()
    return (key * (len(text) // len(key) + 1))[:len(text)]


def vigenere_encrypt(text, key):
    result = ""
    text = text.upper()
    key = adjust_key(text, key)
    for i in range(len(text)):
        if text[i].isalpha():
            temp = chr(((ord(text[i]) - ord('A') + ord(key[i]) - ord('A')) % 26) + ord('A'))
            result += temp
        else:
            result += text[i]
    return result


def vigenere_decrypt(text, key):
    result = ""
    text = text.upper()
    key = adjust_key(text, key)
    for i in range(len(text)):
        if text[i].isalpha():
            temp = chr(((ord(text[i]) - ord('A') - (ord(key[i]) - ord('A')) + 26) % 26) + ord('A'))
            result += temp
        else:
            result += text[i]
    return result


def main():
    print("Vigenère Cipher:")
    text = input("Enter the text you want to encrypt: ")
    key = input("Enter the key: ")
    encrypted_text = vigenere_encrypt(text, key)
    print("The encrypted text is:", encrypted_text)
    decrypted_text = vigenere_decrypt(encrypted_text, key)
    print("The decrypted text is:", decrypted_text)


main()
