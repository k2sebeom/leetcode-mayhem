'''

Title: Gas Station
Source: https://leetcode.com/problems/gas-station/
Comment: Greedy algorithm. When there exists only one solution, thinking of optimization as greedy algorithm.

'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        trip_tank, curr_tank, start, n = 0, 0, 0, len(gas)
        for i in range(n):
            trip_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            if curr_tank < 0:
                start = i + 1
                curr_tank = 0 
        return start if trip_tank >= 0 else -1