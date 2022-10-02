'''

Title: Factorial Trailing Zeroes
Source: https://leetcode.com/problems/factorial-trailing-zeroes/
Comment: Think of the number of iterations done

'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
        fives = 0
        
        for i in range(1, n + 1):
            q = i
            while q % 5 == 0:
                fives += 1
                q = q // 5

        return fives