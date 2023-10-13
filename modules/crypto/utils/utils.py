from modules.crypto.constants import alphabet

# Function to convert a message to uppercase and remove characters not in the alphabet
def preprocess_message(message):
    message = message.lower()
    message = ''.join(char for char in message if char in alphabet.SLOVENIAN_ALPHABET)
    return message

# Function to pad the message to match the matrix size
def pad_message(message, matrix_size):
    while len(message) % matrix_size != 0:
        message += 'a'  # You can use any character for padding
    return message