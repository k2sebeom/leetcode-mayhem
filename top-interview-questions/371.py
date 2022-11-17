'''

Title: Sum of Two Integers
Source: https://leetcode.com/problems/sum-of-two-integers/
Comment: Computer Architecture is oddly helpful

'''

class Solution:
    def twos_complement(self, b):
        s = ''
        for c in b:
            s += '0' if c == '1' else '1'
        s = self.add(s, '0' * 11 + '1', bound=True)
        return s

    def add(self, ba: str, bb: str, bound=False) -> str:
        result = ''
        carry = 0
        for (ia, ib) in zip(ba[::-1], bb[::-1]):
            ca, cb = int(ia), int(ib)
            temp = ca & cb
            s = ca ^ cb
            temp_carry = temp | (s & carry)
            s = s ^ carry
            carry = temp_carry
            result = f'{s}{result}'
        if carry > 0 and bound:
            result = '1' + result
        return result
    
    def getSum(self, a: int, b: int) -> int:
        s = ''
        ba = bin(abs(a))[2:]
        bb = bin(abs(b))[2:]
        ba = '0' + '0' * (11 - len(ba)) + ba
        bb = '0' + '0' * (11 - len(bb)) + bb
        if b < 0:
            bb = self.twos_complement(bb)
        if a < 0:
            ba = self.twos_complement(ba)

        result = self.add(ba, bb)

        is_neg = result[0] == '1'
        if is_neg:
            result = self.twos_complement(result)

        return int(result, 2) * (-1 if is_neg else 1)
            
            
            