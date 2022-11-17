'''

Title: Longest Increasing Subsequence
Source: https://leetcode.com/problems/longest-increasing-subsequence/
Comment: Take a look into bisect module

'''
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for n in nums:
            idx = bisect.bisect_left(tails, n)
            tails[idx:idx+1] = [n]
        return len(tails)
