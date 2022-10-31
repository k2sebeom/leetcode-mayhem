'''

Title: Kth Largest Element in an Array
Source: https://leetcode.com/problems/kth-largest-element-in-an-array/
Comment: Take a look at heap algorithms.

'''

from heapq import nlargest

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return nlargest(k, nums)[-1]