#!/usr/bin/python3
"""2D matrix rotation module
"""
def rotate_2d_matrix(matrix):
    """Rotates an n by n matrix and rotates it 90 degrees clockwise.

    Args:
        matrix (array): array of arrays of integers or characters

    Returns:
        matrix: rotated matrix argument
    """
    n = len(matrix)
    
    # Transpose the matrix in-place
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        matrix[i].reverse()

# Example usage:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rotate_2d_matrix(matrix)
print(matrix)
