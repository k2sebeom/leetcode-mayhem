'''

Title: Min Stack
Source: https://leetcode.com/problems/min-stack/
Comment: Remember that stacks are FILO, so it keeps the memory. Keep the minimum value so far within the stack.

'''


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))

    def pop(self) -> None:
        self.stack.pop(-1)        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]