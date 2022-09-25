'''

Title: Longest Consecutive Sequence
Source: https://leetcode.com/problems/longest-consecutive-sequence/
Comment: Even though there exists a nested loop, we only think of incidents that we count. Think of how human would do.

'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in seen:
                i = n + 1
                j = 1
                while i in seen:
                    i += 1
                    j += 1
                longest = max(longest, j)

        return longest