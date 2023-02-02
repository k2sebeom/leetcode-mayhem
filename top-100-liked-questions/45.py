'''

Title: Jump Game II
Source: https://leetcode.com/problems/jump-game-ii/
Comment: Dynamic Programming Works

'''


class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        Dynamic Programming

        dp = [0, ...., len(nums) - 1]
        min jumps starting from index

        at each step at dp[i]:
            for all indices (i, i + nums[i]):
                find minimum jump
            #O(n)
            dp[i] = min jump + 1
        #O(n^2)
        '''

        dp = [0] * len(nums)

        for i in range(len(dp) - 2, -1, -1):
            min_jump = float('inf')
            for m in range(i + 1, min(len(dp), i + nums[i] + 1)):
                min_jump = min(dp[m], min_jump)
            dp[i] = min_jump + 1
        
        # print(dp)/
        return dp[0]