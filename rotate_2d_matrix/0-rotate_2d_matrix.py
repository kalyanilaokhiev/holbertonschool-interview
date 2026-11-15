#!/usr/bin/python3
"""Rotate 2D Matrix"""

def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate it 90 degrees clockwise"""
    n = len(matrix)
    temp = 0

    for row in range(n):
        for col in range(row + 1, n):
            #transposing, swap rows and col diagonally 
            temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp   

    #reversing each row backwards
    for row in matrix:
        row.reverse()

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

