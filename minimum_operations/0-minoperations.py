#!/usr/bin/python3
""" calculates the fewest number of operations needed
to result in exactly n H characters in the file """


def minOperations(n):
    no_operations = 0
    divisor = 2

    # if n impossible to achieve
    if n <= 1:
        return 0

    while n > 1:
        # if n can be divisible by the divisor:
        if n % divisor == 0:
            # add divisor to number of operations
            no_operations += divisor
            # divide n by divisor
            n = n // divisor
        else:
            # if not, go to the next number to divide
            divisor += 1

    return no_operations
