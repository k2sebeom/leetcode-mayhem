'''

Title: Count and Say
Source: https://leetcode.com/problems/count-and-say/
Comment: Pretty straight forward

'''

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        prev = self.countAndSay(n - 1)
        
        last_seen = prev[0]
        count = 0
        result = ""

        for c in prev:
            if c == last_seen:
                count += 1
            else:
                result += f"{count}{last_seen}"
                last_seen = c
                count = 1
        result += f"{count}{last_seen}"
        return result