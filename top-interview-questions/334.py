'''

Title: Increasing Triplet Subsequence
Source: https://leetcode.com/problems/increasing-triplet-subsequence/
Comment: We can say it is a greedy algorithm

'''

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
