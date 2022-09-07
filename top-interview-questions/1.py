'''

Title: Two Sum
Source: https://leetcode.com/problems/two-sum/
Comment: Hello

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = dict()
        for i, value in enumerate(nums):
            indices[value] = i
        for i, value in enumerate(nums):
            remaining = target - value
            if remaining in indices and indices[remaining] != i:
                return [i, indices[remaining]]
        return [-1, -1]
