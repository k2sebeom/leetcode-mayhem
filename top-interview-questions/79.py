'''

Title: Word Search
Source: https://leetcode.com/problems/word-search/
Comment: Backtracking or DFS

'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(board: List[List[str]], word: str, row: int, col: int) -> bool:
            if board[row][col] != word[0]:
                return False

            if len(word) == 1:
                return True
            
            result = False
            temp = board[row][col]
            board[row][col] = '0'
            if row - 1 >= 0:
                result = result or helper(board, word[1:], row - 1, col)
            if col + 1 < len(board[0]):
                result = result or helper(board, word[1:], row, col + 1)
            if row + 1 < len(board):
                result = result or helper(board, word[1:], row + 1, col)
            if col - 1 >= 0:
                result = result or helper(board, word[1:], row, col - 1)
            board[row][col] = temp
            return result

        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(board, word, i, j):
                    return True
        return False
