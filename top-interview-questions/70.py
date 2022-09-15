'''

Title: Climbing Stairs
Source: https://leetcode.com/problems/climbing-stairs/
Comment: Dynamic Programming works like a charm

'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]