'''

Title: Count Primes
Source: https://leetcode.com/problems/count-primes/
Comment: Sieve of Eratosthenes

'''

class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [1] * n
        if n < 2:
            return 0
        
        sieve[0], sieve[1] = 0, 0
        
        for i in range(2, int(sqrt(n)) + 1):
            if sieve[i] == 0:
                continue
            for j in range(2*i, n, i):
                sieve[j] = 0
            
        return sum(sieve)