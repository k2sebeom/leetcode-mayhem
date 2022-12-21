'''

Title: Combination Sum
Source: https://leetcode.com/problems/combination-sum/
Comment: Dynamic programming, but there still exists room for optimization

'''


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target)]
        # if ith all the combinations that can make i + 1
        # ith
        # 2 + dp[i - 2]
        # 3 + dp[i - 3]
        
        for c in candidates:
            if c - 1 < target:
                dp[c - 1].append([c])
        
        for i in range(target):
            for c in candidates:
                if i - c >= 0:
                    for comb in dp[i - c]:
                        dp[i].append(comb + [c])
        # print(dp)
        for i in range(len(dp[-1])):
            dp[-1][i].sort()
            dp[-1][i] = tuple(dp[-1][i])
        dp[-1] = list(set(dp[-1]))
        return dp[-1]
