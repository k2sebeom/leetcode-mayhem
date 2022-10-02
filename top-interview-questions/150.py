'''

Title: Evaluate Reverse Polish Notation
Source: https://leetcode.com/problems/evaluate-reverse-polish-notation/
Comment: Think of valid parenthesis problem. Use Stack

'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)
        }
        
        for t in tokens:
            if t in operations:
                y = stack.pop(-1)
                x = stack.pop(-1)
                op = operations[t]
                stack.append(op(x, y))
            else:
                stack.append(int(t))
        return stack[0]