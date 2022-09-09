'''

Title: Divide Two Integers
Source: https://leetcode.com/problems/divide-two-integers/
Comment: The idea is the same. We are finding the number of times dividend can contain divisor, but since step by step move is too slow, we go in powers of 2 multiple times.

'''

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)