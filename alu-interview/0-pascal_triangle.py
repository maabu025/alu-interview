#!/usr/bin/python3

"""
0-pascal_triangle
Module that defines a function to generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the given level.

    Args:
        n (int): The level of Pascal's Triangle to generate.

    Returns:
        list: A list of lists representing Pascal's Triangle.

    Raises:
        ValueError: If n is less than or equal to 0.

    Examples:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(1, i):
            element = prev_row[j - 1] + prev_row[j]
            row.append(element)

        row.append(1)
        triangle.append(row)

    return triangle


def print_triangle(triangle):
    """
    Prints the Pascal's Triangle.

    Args:
        triangle (list): A list of lists representing Pascal's Triangle.

    Returns:
        None

    Examples:
        >>> triangle = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
        >>> print_triangle(triangle)
        [1]
        [1, 1]
        [1, 2, 1]
        [1, 3, 3, 1]
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    triangle = pascal_triangle(5)
    print_triangle(triangle)
