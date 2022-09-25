'''

Title: Best Time to Buy and Sell Stock II
Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
Comment: Think of greedy algorithm: Think of myopic decision making at see if it works for global setting

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Greedy
        bought = -1
        profit = 0
        
        for i in range(len(prices) - 1):
            if bought < 0 and prices[i + 1] > prices[i]: # If you have not bought yet and price increases
                bought = prices[i] # Buy now
            elif bought >= 0 and prices[i + 1] < prices[i]: # bought and price decreases
                profit += prices[i] - bought
                bought = -1
        if bought >= 0 and prices[-1] > bought:
            profit += prices[-1] - bought
        return profit
            
            