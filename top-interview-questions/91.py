'''

Title: Decode Ways
Source: https://leetcode.com/problems/decode-ways/
Comment: Dynamic Programming works

'''

class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1:
            return 0 if s == '0' else 1
        
        dp = [0] * len(s)
        
        dp[-1] = 0 if s[-1] == '0' else 1
        
        if s[-2] == '0':
            dp[-2] = 0
        elif int(s[-2:]) <= 26:
            dp[-2] = 1 + dp[-1]
        else:
            dp[-2] = dp[-1]

        for i in range(len(s) - 3, -1, -1):
            result = 0
            if s[i] != '0':
                result += dp[i + 1]
            if s[i] != "0" and int(s[i:i+2]) <= 26:
                result += dp[i + 2]
            dp[i] = result
        return dp[0]
                