'''

Title: Letter Combinations of a Phone Number
Source: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Comment: Sometimes, a brute force recursion might work

'''

class Solution:
    MEMO = {}
    
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        if digits in self.MEMO:
            print(f'{digits} in memo')
            return self.MEMO[digits]
        
        if not digits:
            return ""
        
        if len(digits) == 1:
            self.MEMO[digits] = [c for c in phone[digits[0]]]
            return [c for c in phone[digits[0]]]
            
        prev = self.letterCombinations(digits[1:])
        
        result = []
        
        for c in phone[digits[0]]:
            result += [c + comb for comb in prev]
        self.MEMO[digits] = result
        return result
