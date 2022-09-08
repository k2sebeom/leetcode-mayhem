'''

Title: Longest Common Prefix
Source: https://leetcode.com/problems/longest-common-prefix/
Comment: Pretty straight forward

'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_len = len(strs[0])
        prefix = ""
        for s in strs:
            min_len = min(min_len, len(s))
        
        for i in range(min_len):
            c = strs[0][i]
            common = True
            for s in strs:
                if s[i] != c:
                    common = False
                    break
            if common:
                prefix += c
            else:
                break
        return prefix