'''

Title: Zigzag Conversion
Source: https://leetcode.com/problems/zigzag-conversion/
Comment: O(n) algorithm. Handle the edge case and build some rows

'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): # Edge case
            return s

        rows = [''] * numRows
        curr, direction = 0, 1
        for x in s:
            rows[curr] += x
            if curr == numRows - 1:
                direction = -1
            elif curr == 0:
                direction = 1
            curr += direction
        
        return ''.join(rows)