'''

Title: Largest Number
Source: https://leetcode.com/problems/largest-number/
Comment: functools cmp_to_key may be a nice approach

'''

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x: str, y: str):
            if int(x + y) > int(y + x):
                return 1
            elif int(x + y) < int(y + x):
                return -1
            else:
                return 0
        
        snums = list(map(str, nums))
        snums.sort(key=cmp_to_key(compare), reverse=True)
        return str(int(''.join(snums)))