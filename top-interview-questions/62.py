'''

Title: Unique Paths
Source: https://leetcode.com/problems/unique-paths/
Comment: Standard DP problem

'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n - 1) + [1] for _ in range(m - 1)]
        dp.append([1] * n)

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]