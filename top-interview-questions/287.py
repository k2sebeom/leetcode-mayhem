'''

Title: Find the Duplicate Number
Source: https://leetcode.com/problems/find-the-duplicate-number/
Comment: Use the constraint that nums are in [1, n]

'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        idx = 0
        curr = nums[0]
        nums[0] = 0
        for _ in range(len(nums)):
            if nums[curr] == 0:
                return curr
            nums[curr], curr = 0, nums[curr]

            
        