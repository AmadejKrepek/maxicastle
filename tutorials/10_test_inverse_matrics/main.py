def calculate_determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]

    det = 0
    for j in range(n):
        sub_matrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        sub_matrix_det = calculate_determinant(sub_matrix)
        det += matrix[0][j] * sub_matrix_det * (-1) ** j

    return det

def calculate_inverse_matrix(matrix, det, modulus):
    n = len(matrix)
    adjugate_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            sub_matrix = [row[:j] + row[j+1:] for row in matrix[:i] + matrix[i+1:]]
            sub_matrix_det = calculate_determinant(sub_matrix)
            cofactor = (-1) ** (i + j) * sub_matrix_det % modulus
            adjugate_matrix[i][j] = cofactor

    inverse_matrix = [[(adjugate_matrix[i][j] * pow(det, -1, modulus)) % modulus for j in range(n)] for i in range(n)]
    return inverse_matrix

# Example usage:
matrix = [[20, 5], [18, 20]]
modulus = 29

determinant = calculate_determinant(matrix)
if determinant % modulus == 0:
    print("The determinant is not invertible with the given modulus.")
else:
    inverse_matrix = calculate_inverse_matrix(matrix, determinant, modulus)
    for row in inverse_matrix:
        print(row)
