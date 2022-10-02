'''

Title: Fraction to Recurring Decimal
Source: https://leetcode.com/problems/fraction-to-recurring-decimal/
Comment: Mimic the process as if human is doing it

'''


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        is_negative = numerator * denominator < 0
        numerator, denominator = abs(numerator), abs(denominator)
        whole = numerator // denominator
        decimal = []
        recurring = True
        seen = dict()
        remainder = numerator % denominator
        
        if remainder == 0:
            return f'{"-" if is_negative else ""}{whole}'
        
        i = 0
        
        while True:
            carry = remainder * 10
            point = carry // denominator
            decimal.append(point)
            
            seen[remainder] = i
            remainder = carry % denominator           
            
            if remainder == 0:
                recurring = False
                break
            if remainder in seen:
                break
            i += 1
    
        if recurring:
            idx = seen[remainder]
            decimal = ''.join(map(str, decimal[:idx])) +  "(" + ''.join(map(str, decimal[idx:])) + ")"
        else:
            decimal = ''.join(map(str, decimal))
        return f'{"-" if is_negative else ""}{whole}.{decimal}'