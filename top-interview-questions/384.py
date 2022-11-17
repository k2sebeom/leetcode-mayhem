'''

Title: Shuffle an Array
Source: https://leetcode.com/problems/shuffle-an-array/
Comment: E-Z

'''

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums.copy()
        self.data = nums

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        L = self.original.copy()
        self.data.clear()
        for _ in range(len(self.original)):
            idx = int(random.random() * len(L))
            self.data.append(L.pop(idx))
        return self.data
