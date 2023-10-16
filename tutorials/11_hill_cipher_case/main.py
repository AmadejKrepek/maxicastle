# Define the Slovenian alphabet
slovenian_alphabet = 'abcčdefghijklmnoprstuvzž'

# Function for converting the number matrix to their respective alphabet matrix
def matrix_to_letter(n):
    encry_string = ''
    for i in n:
        for j in i:
            encry_string += slovenian_alphabet[j]
    return encry_string  # final value

# Function for encryption
def encryption(a, b):
    encry_l = []
    for i in range(0, len(b), 2):
        l = []
        try:
            l += [slovenian_alphabet.index(b[i]), slovenian_alphabet.index(b[i + 1])]
        except:
            l += [slovenian_alphabet.index(b[i]), 0]

        # Multiplying the matrix to have the resultant encrypted matrix
        c = [[0, 0]]
        for j in range(2):
            for k in range(2):
                c[0][j] += a[j][k] * l[k]

        # Taking the modulo of the alphabet length
        c[0][0] %= len(slovenian_alphabet)
        c[0][1] %= len(slovenian_alphabet)

        encry_l.append(c[0])

    return matrix_to_letter(encry_l)  # returns the encrypted string

# Function for decryption
def decryption(a, b):
    decry_l = []
    for i in range(0, len(b), 2):
        l = []
        try:
            l += [slovenian_alphabet.index(b[i]), slovenian_alphabet.index(b[i + 1])]
        except:
            l += [slovenian_alphabet.index(b[i]), 0]

        # Calculate the determinant of the matrix 'a'
        det = a[0][0] * a[1][1] - a[0][1] * a[1][0]

        # Find the multiplicative inverse of the determinant modulo the alphabet length
        inv_det = None
        for d in range(1, len(slovenian_alphabet)):
            if (det * d) % len(slovenian_alphabet) == 1:
                inv_det = d
                break

        if inv_det is None:
            raise ValueError("The provided key matrix is not invertible.")

        # Calculate the inverse matrix
        a_inv = [[0, 0], [0, 0]]
        a_inv[0][0] = (a[1][1] * inv_det) % len(slovenian_alphabet)
        a_inv[0][1] = (-a[0][1] * inv_det) % len(slovenian_alphabet)
        a_inv[1][0] = (-a[1][0] * inv_det) % len(slovenian_alphabet)
        a_inv[1][1] = (a[0][0] * inv_det) % len(slovenian_alphabet)

        # Multiply the inverse matrix and the encrypted text
        c = [[0, 0]]
        for j in range(2):
            for k in range(2):
                c[0][j] += a_inv[j][k] * l[k]

        # Take the modulo of the alphabet length for each element
        c[0][0] = c[0][0] % len(slovenian_alphabet)
        c[0][1] = c[0][1] % len(slovenian_alphabet)

        decry_l.append(c[0])

    return matrix_to_letter(decry_l)  # returns the decrypted string

# Function to convert a string key into a 2x2 numeric key matrix
def string_to_key_matrix(key_string):
    key_matrix = [[slovenian_alphabet.index(key_string[0]), slovenian_alphabet.index(key_string[1])],
                  [slovenian_alphabet.index(key_string[2]), slovenian_alphabet.index(key_string[3])]]
    return key_matrix

# Function to add padding to the message
def add_padding(msg):
    while len(msg) % 2 != 0:
        msg += 'a'  # Add 'a' as padding
    return msg

# Main program starts here
msg = input("Enter the message for encryption: ").lower().replace(" ", "")

# Get the encryption key from the user as a 4-character string
key_string = input("Enter a 4-character string key: ").lower().replace(" ", "")

# Add padding to the message if needed
msg = add_padding(msg)

# Check if the key and message are of the correct length
if len(key_string) != 4:
    print("Key length should be 4 characters.")
else:
    # Convert the string key to a key matrix
    randmat = string_to_key_matrix(key_string)

    # Split the sentence for encrypting and decrypting each word
    word_list = [msg[i:i+2] for i in range(0, len(msg), 2)]

    encrypted_message = ''
    decrypted_message = ''

    for word in word_list:
        # Encryption
        encrypted_message += encryption(randmat, word)

        # Decryption
        decrypted_message += decryption(randmat, encrypted_message)

    print("Encrypted message is:", encrypted_message)
    print("Decrypted message is:", decrypted_message)
