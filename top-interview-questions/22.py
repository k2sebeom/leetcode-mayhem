'''

Title: Generate Parentheses 
Source: https://leetcode.com/problems/generate-parentheses/
Comment: Considering all possible cases is important. Study recursive algorithms like backtracking and DFS

'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        if n == 1:
            return ["()"]
        
        prev = self.generateParenthesis(n - 1)
        result = set()
        
        for p in prev:
            stack = 0
            indices = [0]
            print(p)
            for i, c in enumerate(p):
                if c == '(':
                    stack += 1
                else:
                    stack -= 1
                if stack == 0:
                    indices.append(i)
            print(indices)
            for i in indices:
                for j in indices:
                    if i <= j:
                        result.add(p[:i] + '(' + p[i:j] + ')' + p[j:])
        return list(result)