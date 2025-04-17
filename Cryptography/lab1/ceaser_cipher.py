def caesar_encrypt(text, key):
    result = ""
    uppertext = text.upper()
    for char in uppertext:
        if char.isalpha():
            temp = chr((ord(char) + key - 65) % 26 + 65)
            result += temp
        else:
            result += char
    return result


def caesar_decrypt(text, key):
    result = ""
    uppertext = text.upper()
    for char in uppertext:
        if char.isalpha():
            temp = chr((ord(char) - key - 65) % 26 + 65)
            result += temp
        else:
            result += char
    return result


def main():
    print("Caesar Cipher:")
    text = input("Enter the text you want to encrypt: ")
    key = int(input("Enter the key: "))
    encrypted_text = caesar_encrypt(text, key)
    print("The encrypted text is:", encrypted_text)
    decrypted_text = caesar_decrypt(encrypted_text, key)
    print("The decrypted text is:", decrypted_text)


main()
