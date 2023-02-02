'''

Title: Permutations
Source: https://leetcode.com/problems/permutations/
Comment: Basic Permutations

'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        
        result = []
        perms = self.permute(nums[1:])
        s = nums[0]
        for p in perms:
            for i in range(len(p) + 1):
                result.append(p[:i] + [s] + p[i:])
        return result