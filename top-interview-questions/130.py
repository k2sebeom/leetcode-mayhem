'''

Title: Surrounded Regions
Source: https://leetcode.com/problems/surrounded-regions/
Comment: Why does it work....?

'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        marks = [[0] * len(board[0]) for _ in range(len(board))]

        def mark(i, j):
            marks[i][j] = -1
            if board[i][j] != 'O':
                return
            if j + 1 < len(board[0]) and marks[i][j+1]  >= 0 and board[i][j + 1] == 'O':
                mark(i, j + 1)
            if j - 1 > 0 and marks[i][j-1]  >= 0 and board[i][j - 1] == 'O':
                mark(i, j - 1)
            if i + 1 < len(board) and marks[i+1][j]  >= 0 and board[i + 1][j] == 'O':
                mark(i + 1, j)
            if i - 1 > 0 and marks[i - 1][j]  >= 0 and board[i - 1][j] == 'O':
                mark(i - 1, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
                    mark(i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if marks[i][j] >= 0:
                    board[i][j] = 'X'
        return board