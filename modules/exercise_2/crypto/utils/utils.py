from modules.exercise_1.crypto.constants import alphabet


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


# Function to generate a key
def generate_key(key_var):
    # You can implement key generation logic here
    # For example, you can use a library like cryptography to generate a key
    # Replace the following line with your key generation logic
    generated_key = "YourGeneratedKeyHere"
    key_var.set(generated_key)
