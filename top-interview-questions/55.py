'''

Title: Jump Game
Source: https://leetcode.com/problems/jump-game/
Comment: Define dynamic programming table thoughtfully

'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        db = [False] * len(nums)
        db[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            db[i] = i + nums[i] >= last
            if db[i]:
                last = i
        return db[0]
