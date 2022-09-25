'''

Title: Palindrome Partitioning
Source: https://leetcode.com/problems/palindrome-partitioning/
Comment: O(n^2) is still good considering the worst case is all the partitions

'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[] for _ in s]
        dp[0] = [[s[0]]]
        for i in range(1, len(dp)):
            singleton = list(map(lambda x: x + [s[i]], dp[i - 1]))
            dp[i] = singleton
            if s[0:i+1] == s[0:i+1][::-1]:
                dp[i].append([s[:i + 1]])
            for j in range(1, i):
                if s[j:i+1] == s[j:i+1][::-1]:
                    dp[i] += list(map(lambda x: x + [s[j:i+1]], dp[j - 1]))

        return dp[-1]
