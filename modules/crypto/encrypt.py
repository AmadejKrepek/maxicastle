# Hill cipher encryption function for Slovenian alphabet
from modules.crypto.utils.utils import preprocess_message, pad_message
from modules.crypto.constants import alphabet


# Hill cipher encryption function for Slovenian alphabet
def encrypt(plaintext, key):
    plaintext = preprocess_message(plaintext)
    key = preprocess_message(key)
    n = int(len(key) ** 0.5)

    # Check if the length of the plaintext is a multiple of 'n'
    if len(plaintext) % n != 0:
        # If not, pad the plaintext to make it a whole number of blocks
        plaintext = pad_message(plaintext, n)

    while len(key) < n * n:
        key += "a"

    matrix = [[alphabet.SLOVENIAN_ALPHABET.index(char) for char in key[i:i + n]] for i in range(0, len(key), n)]
    encrypted_text = ""

    for i in range(0, len(plaintext), n):
        block = [alphabet.SLOVENIAN_ALPHABET.index(char) for char in plaintext[i:i + n]]
        result = [sum(matrix[i][j] * block[j] for j in range(n)) % len(alphabet.SLOVENIAN_ALPHABET) for i in range(n)]
        encrypted_text += ''.join(alphabet.SLOVENIAN_ALPHABET[char] for char in result)

    return encrypted_text
