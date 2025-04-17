import numpy as np


def find_position(matrix, char):
    row = 0
    for r in matrix:
        col = 0
        for elem in r:
            if elem == char:
                return (row, col)
            elif char in elem:
                return row, col
            col += 1
        row += 1


def playfair_encrypt(message, key):
    key_matrix = generate_key_matrix(key)
    message = message.replace(" ", '')
    message = list(message)
    cipher_text = ''
    for i in range(int(np.ceil(len(message)/2))):
        digraph = message[0:2]
        if len(digraph) == 2:
            if digraph[0] != digraph[1]:
                message.pop(0)
                message.pop(0)
            elif digraph[0] != 'X':
                digraph[1] = 'X'
                message.pop(0)
            else:
                digraph[1] = 'Q'
                message.pop(0)
        elif digraph[0] != 'X':
            digraph.append('X')
            message.pop(0)
        else:
            digraph.append('Q')
            message.pop(0)
        r1, c1 = find_position(key_matrix, digraph[0])
        r2, c2 = find_position(key_matrix, digraph[1])
        if r1 == r2:
            if c1 != 4 and c2 != 4:
                cipher_text += key_matrix[r1][c1 + 1]
                cipher_text += key_matrix[r1][c2 + 1]
            elif c1 != 4:
                cipher_text += key_matrix[r1][c1 + 1]
                cipher_text += key_matrix[r1][0]
            else:
                cipher_text += key_matrix[r1][0]
                cipher_text += key_matrix[r1][c2 + 1]
        elif c1 == c2:
            if r1 != 4 and r2 != 4:
                cipher_text += key_matrix[r1 + 1][c1]
                cipher_text += key_matrix[r2 + 1][c1]
            elif r1 != 4:
                cipher_text += key_matrix[r1 + 1][c1]
                cipher_text += key_matrix[0][c2]
            else:
                cipher_text += key_matrix[0][c1]
                cipher_text += key_matrix[r2 + 1][c1]
        else:
            cipher_text += key_matrix[r1][c2]
            cipher_text += key_matrix[r2][c1]
    return cipher_text


def generate_key_matrix(key):
    matrix = []
    key_matrix = [[None for _ in range(5)] for _ in range(5)]
    for i in range(len(key)):
        if key[i] not in matrix:
            if key[i] not in ['I', 'J']:
                matrix.append(key[i])
            else:
                matrix.append('I')
    for j in range(26):
        if letters[j] not in matrix:
            if letters[j] not in ('I', 'J'):
                matrix.append(letters[j])
            elif 'I' not in matrix:
                matrix.append('I')
            else:
                continue
    count = 0
    for rows in range(5):
        for cols in range(5):
            key_matrix[rows][cols] = matrix[count]
            count += 1
    return key_matrix


letters = []
for i in range(65, 91):
    letters.append(chr(i))


def main():
    message = input("Enter the message you want to encrypt: ").upper()
    key = input("Enter the key: ").upper()
    print("Encrypted message:", playfair_encrypt(message, key))


main()
