'''

Title: Basic Calculator II
Source: https://leetcode.com/problems/basic-calculator-ii/
Comment: Use stack, and keep track of the last seen operation

'''


class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return "0"
        stack, num, op = [], 0, "+"
        for i in range(len(s)):
            if s[i] not in '+-*/ ':
                num = num * 10 + int(s[i])

            if s[i] in '+-*/' or i == len(s)-1:
                if op == "-":
                    stack.append(-num)
                elif op == "+":
                    stack.append(num)
                elif op == "*":
                    stack.append(stack.pop() * num)
                else:
                    if stack[-1] < 0:
                        stack.append(-((-stack.pop()) // num))
                    else:
                        stack.append(stack.pop() // num)
                op = s[i]
                num = 0
            # print(stack)

        return sum(stack)