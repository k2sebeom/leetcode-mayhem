'''

Title: Game of Life
Source: https://leetcode.com/problems/game-of-life/
Comment: This is CS150 level of problem

'''


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def count_neighbors(i, j):
            count = 0
            for x in (-1, 0, 1):
                for y in (-1, 0, 1):
                    if x == 0 and y == 0:
                        continue
                    if i + x >= 0 and i + x < len(board) and j + y >= 0 and j + y < len(board[0]):
                        count += board[i + x][j + y]
                    
            return count
        next_board = [[d for d in row] for row in board]
        for i in range(len(board)):
            for j in range(len(board[i])):
                count = count_neighbors(i, j)
                if count < 2 or count > 3:
                    next_board[i][j] = 0
                if count == 3:
                    next_board[i][j] = 1
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = next_board[i][j]
                    