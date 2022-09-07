'''

Title: Longest Substring Without Repeating Characters
Source: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Comment: It is an O(n) algorithm with "sliding window" technique. Log the index of the character while sliding thru the string, and once you find a character that you have seen before, shrink the window so that you look into the longest window without repeating that character.

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        start = 0
        max_len = 0
        where = {}
        for i in range(len(s)):
            if s[i] in where and where[s[i]] >= start:
                start = where[s[i]] + 1
            where[s[i]] = i
            max_len = max(max_len, i - start + 1)
        return max_len
