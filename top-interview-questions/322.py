'''

Title: Coin Change
Source: https://leetcode.com/problems/coin-change/
Comment: Think of DP solution. Backtracking is rarely an optimized solution

'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            min_amount = amount + 10
            for c in coins:
                if a - c >= 0 and dp[a-c] >= 0:
                    min_amount = min(dp[a - c] + 1, min_amount)
            dp[a] = min_amount if min_amount <= amount else -1
        return dp[-1]