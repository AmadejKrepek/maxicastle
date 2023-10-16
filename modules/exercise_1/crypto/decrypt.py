from modules.exercise_1.crypto.utils.utils import preprocess_message, pad_message
from modules.exercise_1.crypto.constants import alphabet


def calculate_determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]

    det = 0
    for j in range(n):
        sub_matrix = [row[:j] + row[j + 1:] for row in matrix[1:]]
        sub_matrix_det = calculate_determinant(sub_matrix)
        det += matrix[0][j] * sub_matrix_det * (-1) ** j

    return det


def calculate_inverse_matrix(matrix, det):
    n = len(matrix)
    adjugate_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            sub_matrix = [row[:j] + row[j + 1:] for row in matrix[:i] + matrix[i + 1:]]
            sub_matrix_det = calculate_determinant(sub_matrix)
            cofactor = (-1) ** (i + j) * sub_matrix_det
            adjugate_matrix[j][i] = cofactor

    n_mod = len(alphabet.SLOVENIAN_ALPHABET)  # Modulus based on the size of the alphabet
    inverse_matrix = [[(adjugate_matrix[i][j] * pow(det, -1, n_mod)) % n_mod for j in range(n)] for i in range(n)]

    return inverse_matrix


# Hill cipher decryption function for Slovenian alphabet
def decrypt(ciphertext, key):
    ciphertext = preprocess_message(ciphertext)
    key = preprocess_message(key)
    n = int(len(key) ** 0.5)

    if n * n != len(key):
        return "Invalid key length. Key must be a square matrix."

    ciphertext = pad_message(ciphertext, n)
    matrix = [[alphabet.SLOVENIAN_ALPHABET.index(char) for char in key[i:i + n]] for i in range(0, len(key), n)]

    det = calculate_determinant(matrix)

    if det == 0:
        return "The matrix is not invertible. The determinant is zero."

    inverse_matrix = calculate_inverse_matrix(matrix, det)

    decrypted_text = ""

    for i in range(0, len(ciphertext), n):
        block = [alphabet.SLOVENIAN_ALPHABET.index(char) for char in ciphertext[i:i + n]]
        result = [sum(inverse_matrix[i][j] * block[j] for j in range(n)) % len(alphabet.SLOVENIAN_ALPHABET) for i in
                  range(n)]
        decrypted_text += ''.join(alphabet.SLOVENIAN_ALPHABET[char] for char in result)

    return decrypted_text
