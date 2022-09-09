'''

Title: Valid Parentheses
Source: https://leetcode.com/problems/valid-parentheses/
Comment: We use stack as a data structure. The point is to understand that a left parentheses should not close until all the previous parentheses are closed.

'''

class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')', '{':'}','[':']'}
        stack = []
        for c in s:
            if c in d:
                stack.append(c)
            elif not stack or d[stack.pop()] != c:
                return False
        return len(stack) == 0