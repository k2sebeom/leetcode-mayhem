'''

Title: Search in Rotated Sorted Array
Source: https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/
Comment: Focus on the basic. Check if the known algorithms work

'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1