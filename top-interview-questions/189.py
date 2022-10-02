'''

Title: Rotate Array
Source: https://leetcode.com/problems/rotate-array/
Comment: This is not space O(1), but fast

'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        idx = -k % len(nums)
        left, right = nums[idx:], nums[:idx]
        nums[:] = left + right