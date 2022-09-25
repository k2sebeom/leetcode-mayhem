'''

Title: Subsets
Source: https://leetcode.com/problems/subsets/
Comment: To return all subsets, it is O(2^n) anyways. Simple recursion may work.

'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
    
        without = self.subsets(nums[1:])
        return without + [[nums[0]] + s for s in without]