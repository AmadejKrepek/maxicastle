
from modules.crypto.utils.utils import preprocess_message, pad_message
from modules.crypto.constants import alphabet
# Hill cipher decryption function for Slovenian alphabet
def decrypt(ciphertext, key):
    ciphertext = preprocess_message(ciphertext)
    key = preprocess_message(key)
    n = int(len(key) ** 0.5)

    # Ensure that n is a valid square matrix size
    if n * n != len(key):
        return "Invalid key length. Key must be a square matrix."

    ciphertext = pad_message(ciphertext, n)
    matrix = [[alphabet.SLOVENIAN_ALPHABET.index(char) for char in key[i:i + n]] for i in range(0, len(key), n)]
    matrix_inverse = [[0] * n for _ in range(n)]

    # Calculate the determinant using the Laplace expansion
    det = 0
    if n == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        for i in range(n):
            sub_matrix = [row[:i] + row[i + 1:] for row in matrix[1:]]
            sub_matrix_key = ''.join([alphabet.SLOVENIAN_ALPHABET[i] for row in sub_matrix])
            det += matrix[0][i] * decrypt("a", sub_matrix_key)  # Recursive call with a placeholder key

    # Make sure the determinant is non-zero
    if det == 0:
        return "The matrix is not invertible. The determinant is zero."

    # Rest of the code for computing the inverse matrix

    decrypted_text = ""

    for i in range(0, len(ciphertext), n):
        block = [alphabet.SLOVENIAN_ALPHABET.index(char) for char in ciphertext[i:i + n]]
        result = [sum(matrix_inverse[i][j] * block[j] for j in range(n)) % len(alphabet.SLOVENIAN_ALPHABET) for i in range(n)]
        decrypted_text += ''.join(alphabet.SLOVENIAN_ALPHABET[char] for char in result)

    return decrypted_text