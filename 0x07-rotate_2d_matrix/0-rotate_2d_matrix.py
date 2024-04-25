#!/usr/bin/python3
""" Defining function to rotate 2D matrix """


def rotate_2d_matrix(matrix):
    """ Rotate 2D matrix by 90 degree """
    new_list = []
    row = len(matrix)
    col = len(matrix[0])
    for i in range(0, row):
        tmp_list = []
        for k in range(0, col):
            tmp_list.append(matrix[k][i])
        new_list.append(tmp_list)
    rot_2d = [[i[j] for j in range(len(i) - 1, -1, -1)] for i in new_list]
    return rot_2d
