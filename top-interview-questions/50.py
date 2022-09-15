'''

Title: Pow(x, n)
Source: https://leetcode.com/problems/powx-n/
Comment: If step by step is too exhaustive, think of dividing by two, as well as recursion.

'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def posPow(x: float, n: int) -> float:
            if n == 0:
                return 1
            if n == 1:
                return x
            prev = posPow(x, n // 2)
            if n % 2 == 0:
                return prev * prev
            else:
                return prev * prev * x
        
        result = posPow(x, abs(n))
        return result if n > 0 else 1 / result