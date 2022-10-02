'''

Title: Maximum Product Subarray
Source: https://leetcode.com/problems/maximum-product-subarray/
Comment: Kadane's algorithm, but we keep track of min prod because it may turn positive when meeting negative number

'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = prev_max = prev_min = nums[0]
        for num in nums[1:]:
            curr_min = min(prev_max*num, prev_min*num, num)
            curr_max = max(prev_max*num, prev_min*num, num)
            global_max= max(global_max, curr_max)
            prev_max = curr_max
            prev_min = curr_min
        return global_max