'''

Title: Search a 2D Matrix II
Source: https://leetcode.com/problems/search-a-2d-matrix-ii/
Comment: Start from top right and moves down searching. Start with intuition but think logically.

'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1

        while row < rows and col >= 0:
            val = matrix[row][col]
            if val > target:
                col -= 1
            elif val < target:
                row += 1
            else:
                return True
        return False