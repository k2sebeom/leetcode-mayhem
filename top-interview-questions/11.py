'''

Title: Container With Most Water
Source: https://leetcode.com/problems/container-with-most-water/
Comment: O(n) greedy algorithm with two pointers. This may work because greedy always stays ahead. For example, it you have checked idx 1 and 3, moving the pointer of the taller tale will be meaningless since the shorter tale determines the amount of water.

'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        result, i, j = 0, 0, len(height)-1
        while (i < j):
            res = min(height[i], height[j]) * (j - i)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
            if res > result: result = res
        return result