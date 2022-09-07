'''

Title: Longest Palindromic Substring
Source: https://leetcode.com/problems/longest-palindromic-substring/
Comment: It is an O(n^2) algorithm. When it comes to a palindrome, expanding from middle to left right index is useful. I am not sure how to optimize it to O(n). REMEMBER get_pal method. It may come handy.

'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        
        def get_pal(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1; r += 1
            return s[l+1:r]

        result = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = get_pal(s, i, i)
            if len(tmp) > len(result):
                result = tmp
            # even case, like "abba"
            tmp = get_pal(s, i, i+1)
            if len(tmp) > len(result):
                result = tmp
        return result