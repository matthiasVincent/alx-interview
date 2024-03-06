#!/usr/bin/python3

"""Module implements a function that returns pascal Triangle"""


def pascal_triangle(n):
    """returns pascal list of lists containing pascal triangle
    for a given value of n"""
    pascal_list = []
    if n <= 0:
        return pascal_list
    pascal_list.append([1])
    for i in range(1, n):
        temp_list = [1]
        for j in range(1, i):
            current = pascal_list[i - 1][j - 1]
            adjacent = pascal_list[i - 1][j]
            sum_of_adjacent_elements = current + adjacent
            temp_list.append(sum_of_adjacent_elements)
        temp_list.append(1)
        pascal_list.append(temp_list)
    return pascal_list
