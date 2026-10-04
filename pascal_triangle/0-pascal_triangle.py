#!/usr/bin/python3
"""pascals triangle"""

def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal's triangle of n"""
    if n <= 0:
        list = []
        return list

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            sum = row[j - 1] + row[j - 1]
            row.append(sum)

        # every row ends with a 1
        end = 1
        row.append(end)
        triangle.append(row)

    return triangle