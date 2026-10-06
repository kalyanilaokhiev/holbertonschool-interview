#!/usr/bin/python3
"""pascals triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
        the Pascal's triangle of n"""
    if n <= 0:
        list = []
        return list

    triangle = [[1]]

    for i in range(n - 1):
        # previous row
        prev = triangle[-1]
        # new row starts with 1
        row = [1]

        # calc row numbers by getting prev indexes
        for j in range(len(prev) - 1):
            # slide with 2 numbers and add them, keep going until len(prev) - 1
            number = prev[j] + prev[j + 1]
            row.append(number)

        # append 1 at the end
        row.append(1)
        triangle.append(row)

    return triangle
