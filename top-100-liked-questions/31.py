'''

Title: Next Permutation
Source: https://leetcode.com/problems/next-permutation/
Comment: Think of few examples and find the pattern.

'''


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prev = nums[-1]
        idx = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < prev:
                idx = i
                break
            prev = nums[i]
        if idx < 0:
            nums.sort()
            return
        
        min_idx = idx + 1
        for i in range(idx + 1, len(nums)):
            if nums[i] > nums[idx] and nums[min_idx] > nums[i]:
                min_idx = i

        nums[idx], nums[min_idx] = nums[min_idx], nums[idx]
        trailing = nums[idx+1:]
        trailing.sort()
        for i in range(len(trailing)):
            nums[idx + 1 + i] = trailing[i]
