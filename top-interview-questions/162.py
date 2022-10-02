'''

Title: Find Peak Element
Source: https://leetcode.com/problems/find-peak-element/
Comment: Think of the characteristics of the peak. This is a binary search using the fact that after peak, there is either an increasing slope or decreasing slope. Think of some examples if you don't have any clue.

'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        while low < high:
            mid = low + ((high - low) // 2)
            if nums[mid] < nums[mid+1]:
                low = mid + 1
            else:
                high = mid
        return low