#!/usr/bin/python3
"""
    Method that calculate the fewest number of operations.
"""


def minOperations(n):
    """
        calculate fewest number of operation

        Args:
             n: repetition of H

        Returns:
            number of operations(copy all & paste)
    """

    if n <= 1:
        return 0

    operations = 0
    factors = 2

    while factors <= n:
        if n % factors == 0:
            operations += factors
            n //= factors
        else:
            factors += 1
    return operations
