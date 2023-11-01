# Hill cipher encryption function for Slovenian alphabet
from modules.exercise_1.crypto.utils.utils import preprocess_message, pad_message
from modules.exercise_1.crypto.constants import alphabet


# Hill cipher encryption function for Slovenian alphabet
def encrypt(plaintext, key, modulus=25):
    def is_square_matrix(matrix):
        for row in matrix:
            if len(row) != len(matrix):
                return False
        return True

    def determinant(matrix):
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        elif len(matrix) == 3:
            a, b, c = matrix[0]
            d, e, f = matrix[1]
            g, h, i = matrix[2]
            return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
        return None

    def has_inverse(matrix, modulus):
        if not is_square_matrix(matrix):
            return False

        det = determinant(matrix)
        # Singular matrix
        if det == 0:
            return False

        for x in range(1, modulus):
            if (det * x) % modulus == 1:
                return True

        return False

    # Greatest common divisor
    # Euclidean algorythm, till b is 0
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    plaintext = preprocess_message(plaintext)
    key = preprocess_message(key)
    n = int(len(key) ** 0.5)

    if n < 2:
        return False, "Error: The key is too short to create a square matrix."

    if len(plaintext) % n != 0:
        # If not, pad the plaintext to make it a whole number of blocks
        plaintext = pad_message(plaintext, n)

    matrix = [[alphabet.SLOVENIAN_ALPHABET.index(char) for char in key[i:i + n]] for i in range(0, len(key), n)]

    if not is_square_matrix(matrix):
        return False, "Error: The key matrix is not square."

    if not has_inverse(matrix, modulus):
        return False, "Error: The key matrix does not have an inverse."

    if gcd(determinant(matrix), modulus) != 1:
        return False, "Error: The determinant of the key matrix and the modulus have a common divisor."

    encrypted_text = ""

    for i in range(0, len(plaintext), n):
        block = [alphabet.SLOVENIAN_ALPHABET.index(char) for char in plaintext[i:i + n]]
        result = [sum(matrix[i][j] * block[j] for j in range(n)) % modulus for i in range(n)]
        for char in result:
            if 0 <= char < len(alphabet.SLOVENIAN_ALPHABET):
                encrypted_text += alphabet.SLOVENIAN_ALPHABET[char]
            else:
                print(f"Invalid character index: {char}")

    return True, encrypted_text


