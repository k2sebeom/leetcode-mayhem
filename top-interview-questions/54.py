'''

Title: Spiral Matrix
Source: https://leetcode.com/problems/spiral-matrix/
Comment: Think of basic matrix operation like rotate and transpose

'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def rotate(matrix: List[List[int]]) -> List[List[int]]:
            return [[row[::-1][i] for row in matrix] for i in range(len(matrix[0]))]
    
        curr = matrix
        result = []
        while curr:
            row = curr[0]
            result += row
            curr.pop(0)
            if curr:
                curr = rotate(curr)
        return result
