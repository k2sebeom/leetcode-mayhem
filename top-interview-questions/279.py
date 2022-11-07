'''

Title: Perfect Squares
Source: https://leetcode.com/problems/perfect-squares/
Comment: This is slow but DP works

'''


from math import sqrt

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0, 1, 2, 3, 1, 2]
        add = dp.append
        
        if n < len(dp):
            return dp[n]
        
        for i in range(6, n + 1): 
            if int(sqrt(i))**2 == i:
                add(1)
                continue
            best = i
            for j in range(1, int(sqrt(i)) + 1):
                best = min(best, dp[i - j**2] + 1)
            add(best)
        return dp[-1]
        
        