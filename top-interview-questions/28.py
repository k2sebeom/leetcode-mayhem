'''

Title: Find the Index of the First Occurrence in a String
Source: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
Comment: This is difficult?

'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i in range(len(haystack)-len(needle)+1):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle)-1:
                    return i
        return -1