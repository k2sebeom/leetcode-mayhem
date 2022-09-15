'''

Title: Rotate Image
Source: https://leetcode.com/problems/rotate-image/
Comment: i th row becomes jth column reversed.

'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = [[row[i] for row in matrix[::-1]] for i in range(len(matrix))]
