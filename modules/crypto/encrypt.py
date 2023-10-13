from modules.crypto.utils.utils import preprocess_message, pad_message

slovenian_alphabet = "abcčdefghijklmnoprsštuvzž"


# Hill cipher encryption function for Slovenian alphabet
def encrypt(plaintext, key):
    plaintext = preprocess_message(plaintext)
    key = preprocess_message(key)
    n = int(len(key) ** 0.5)
    plaintext = pad_message(plaintext, n)
    while len(key) < n * n:
        key += "a"

    matrix = [[slovenian_alphabet.index(char) for char in key[i:i + n]] for i in range(0, len(key), n)]
    encrypted_text = ""

    for i in range(0, len(plaintext), n):
        block = [slovenian_alphabet.index(char) for char in plaintext[i:i + n]]
        result = [sum(matrix[i][j] * block[j] for j in range(n)) % len(slovenian_alphabet) for i in range(n)]
        encrypted_text += ''.join(slovenian_alphabet[char] for char in result)

    return encrypted_text