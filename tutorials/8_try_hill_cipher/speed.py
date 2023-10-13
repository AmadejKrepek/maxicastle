# Define the Slovenian alphabet
slovenian_alphabet = "abcčdefghijklmnoprsštuvzž"

# Function to convert a message to numbers
def message_to_numbers(message):
    numbers = [slovenian_alphabet.index(char) for char in message]
    return numbers

# Function to convert numbers to a message
def numbers_to_message(numbers):
    message = ''.join([slovenian_alphabet[num] for num in numbers])
    return message

# Function to pad the message to match the matrix size
def pad_message(message, matrix_size):
    while len(message) % matrix_size != 0:
        message += 'a'  # You can change the padding character if needed
    return message

# Function to encrypt a message using the Hill cipher
def hill_cipher_encrypt(message, key_matrix):
    matrix_size = len(key_matrix)
    message = pad_message(message, matrix_size)
    numbers = message_to_numbers(message)

    encrypted_numbers = []
    for i in range(0, len(numbers), matrix_size):
        block = [numbers[i:i + matrix_size]]
        result_block = [0] * matrix_size
        for j in range(matrix_size):
            for k in range(matrix_size):
                result_block[j] += key_matrix[j][k] * block[0][k]
            result_block[j] %= len(slovenian_alphabet)
        encrypted_numbers.extend(result_block)

    encrypted_message = numbers_to_message(encrypted_numbers)
    return encrypted_message

# Example key matrix (3x3)
key_matrix = [
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
]

# Example message to encrypt
message = "kriptografija"

encrypted_message = hill_cipher_encrypt(message, key_matrix)
print("Encrypted Message:", encrypted_message)
