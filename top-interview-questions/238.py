'''

Title: Product of Array Except Self
Source: https://leetcode.com/problems/product-of-array-except-self/
Comment: Different direction

'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        acc = 1
        for n in nums:
            result.append(acc)
            acc *= n
        acc = 1
        for i, n in enumerate(nums[::-1]):
            result[~i] *= acc
            acc *= n
        return result