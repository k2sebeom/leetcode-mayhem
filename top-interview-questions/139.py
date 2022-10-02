'''

Title: Word Break
Source: https://leetcode.com/problems/word-break/
Comment: Dynamic Programming works like a charm

'''

class Solution:    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        wordDict = set(wordDict)
        
        dp[0] = s[0] in wordDict
        
        for i in range(len(dp)):
            if s[:i+1] in wordDict:
                dp[i] = True
                continue
            for j in range(1, i+1):
                if s[j:i+1] in wordDict and dp[j - 1]:
                    dp[i] = True
                    break
        return dp[-1]
