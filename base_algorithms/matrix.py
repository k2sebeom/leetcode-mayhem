'''
Matrix Manipulation
'''
from typing import List

def rotate(matrix: List[List[int]]) -> List[List[int]]:
    return [[row[::-1][i] for row in matrix] for i in range(len(matrix[0]))]

def transpose(matrix: List[List[int]]) -> List[List[int]]:
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def mprint(matrix: List[List[int]]):
    for row in matrix:
        print(row)


if __name__ == '__main__':
    M = [[1, 2, 3], [4, 5, 6]]
    print("Matrix:")
    mprint(M)
    print('===')

    print("Rotate: ")
    mprint(rotate(M))
    print('===')

    print("Transpose: ")
    mprint(transpose(M))
    print('===')
