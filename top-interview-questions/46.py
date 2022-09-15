'''

Title: Permutations
Source: https://leetcode.com/problems/permutations/
Comment: A simple recursion with memoization may work like a charm.

'''

class Solution:
    MEMO = dict()
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        
        if str(nums) in self.MEMO:
            print(f"{nums} in memo!")
            return self.MEMO[str(nums)]
        
        result = []
        for i, n in enumerate(nums):
            rest = nums[:i] + nums[i+1:]
            prev = self.permute(rest)
            for p in prev:
                result.append([n] + p)
        self.MEMO[str(nums)] = result
        return result
            