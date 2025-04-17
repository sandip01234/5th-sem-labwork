import hashlib
def sha256_hash(text):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(text.encode('utf-8'))
    return sha256_hash.hexdigest()

if __name__ == '__main__':
    input_text = input('Enter the text to hash using SHA256: ')
    hashed_value = sha256_hash(input_text)
    print(f'The SHA256 hash of {input_text} is {hashed_value}')
    