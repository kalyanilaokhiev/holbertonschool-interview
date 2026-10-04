#!/usr/bin/python3

def pascal_triangle(n):
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

pascal_triange = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))