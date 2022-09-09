'''

Title: Find First and Last Position of Element in Sorted Array
Source: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Comment: It is a modified binary search. Think of the known algorithms and think how you can apply those changes.

'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[start] == nums[end] == target:
                return [start, end]

            if nums[mid] < target:
                start = mid+1
            elif nums[mid] > target:
                end = mid-1
            else:
                if nums[start] != target: start += 1
                if nums[end] != target: end -= 1
        return [-1,-1]