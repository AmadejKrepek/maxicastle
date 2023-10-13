def encrypt(msg):
    # Replace spaces with nothing
    msg = msg.replace(" ", "")
    # Ask for keyword and get encryption matrix
    C = make_key(msg)
    # Ensure the message length is even
    len_check = len(msg) % 2 == 0
    if not len_check:
        msg += "0"
    # Populate message matrix
    P = create_matrix_of_integers_from_string(msg)
    # Calculate length of the message
    msg_len = int(len(msg) / 2)
    # Calculate P * C
    encrypted_msg = ""
    for i in range(msg_len):
        # Dot product
        row_0 = P[0][i] * C[0][0] + P[1][i] * C[0][1]
        # Modulate and add 26 to get back to the Slovenian alphabet range
        integer = int(row_0 % 30 + ord('A'))
        # Change back to chr type and add to text
        encrypted_msg += chr(integer)
        # Repeat for the second column
        row_1 = P[0][i] * C[1][0] + P[1][i] * C[1][1]
        integer = int(row_1 % 30 + ord('A'))
        encrypted_msg += chr(integer)
    return encrypted_msg

def decrypt(encrypted_msg):
    # Ask for keyword and get encryption matrix
    C = make_key(encrypted_msg)
    # Inverse matrix
    determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
    determinant = determinant % 30
    multiplicative_inverse = find_multiplicative_inverse(determinant, 30)
    C_inverse = [
        [C[1][1], -C[0][1]],
        [-C[1][0], C[0][0]
    ]]
    for row in range(2):
        for column in range(2):
            C_inverse[row][column] *= multiplicative_inverse
            C_inverse[row][column] = C_inverse[row][column] % 30

    P = create_matrix_of_integers_from_string(encrypted_msg)
    msg_len = int(len(encrypted_msg) / 2)
    decrypted_msg = ""
    for i in range(msg_len):
        # Dot product
        column_0 = P[0][i] * C_inverse[0][0] + P[1][i] * C_inverse[0][1]
        # Modulate and add 26 to get back to the Slovenian alphabet range
        integer = int(column_0 % 30 + ord('A'))
        # Change back to chr type and add to text
        decrypted_msg += chr(integer)
        # Repeat for the second column
        column_1 = P[0][i] * C_inverse[1][0] + P[1][i] * C_inverse[1][1]
        integer = int(column_1 % 30 + ord('A'))
        decrypted_msg += chr(integer)
    if decrypted_msg[-1] == "0":
        decrypted_msg = decrypted_msg[:-1]
    return decrypted_msg

def find_multiplicative_inverse(determinant, mod):
    multiplicative_inverse = -1
    for i in range(mod):
        inverse = determinant * i
        if inverse % mod == 1:
            multiplicative_inverse = i
            break
    return multiplicative_inverse

def make_key(message):
    while True:
        cipher = input("Input the encryption key: ")
        if len(cipher) < len(message):
            # Pad the key with 'A' characters to match the message length
            padding_length = len(message) - len(cipher)
            cipher += 'A' * padding_length
        C = create_matrix_of_integers_from_string(cipher)
        determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
        determinant = determinant % 30
        inverse_element = find_multiplicative_inverse(determinant, 30)
        if inverse_element == -1:
            print("Determinant is not relatively prime to 30, uninvertible key")
        else:
            break
    return C

def create_matrix_of_integers_from_string(string):
    # Map string to a list of integers a/A <-> 0, b/B <-> 1 ... ž/Ž <-> 29
    integers = [chr_to_int(c) for c in string]
    length = len(integers)
    M = [[0, 0] for _ in range(length // 2)]
    iterator = 0
    for column in range(length // 2):
        for row in range(2):
            M[column][row] = integers[iterator]
            iterator += 1
    return M

def chr_to_int(char):
    # Cast char to int and subtract ord('A') to get 0-29
    integer = ord(char) - ord('A')
    return integer

if __name__ == "__main__":
    msg = input("Message: ")
    encrypted_msg = encrypt(msg)
    print("Encrypted Message:", encrypted_msg)
    decrypted_msg = decrypt(encrypted_msg)
    print("Decrypted Message:", decrypted_msg)
