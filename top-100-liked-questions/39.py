'''

Title: Combination Sum
Source: https://leetcode.com/problems/combination-sum/
Comment: Dynamic programming, but there still exists room for optimization

'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''Approach
        - Backtracking
        2 -> 2 -> 3
        
        [0, 1, 2, 3, 4, 5, 6, 7]
         n  n. n

        dp = [0, 1, ....., 7]
             [[], [[]], [[2]], [[3]], [[2, 2]], [[2, 3], [3, 2]]], 

        at each step of dp
            iterate though candidates
                c = candidate[i]
                if dp[d - c] exists:
                    add all new combinations
        '''

        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]

        for i in range(1, target + 1):
            for c in candidates:
                if i - c >= 0:
                    for prev in dp[i - c]:
                        dp[i].append(prev + [c])
        # print(dp[-1])
        result = set()
        for comb in dp[-1]:
            comb.sort()
            result.add(tuple(comb))
        return list(result)