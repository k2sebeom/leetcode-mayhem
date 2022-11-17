'''

Title: Top K Frequent Elements
Source: https://leetcode.com/problems/top-k-frequent-elements/
Comment: Easy

'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = dict()
        for n in nums:
            if n in seen:
                seen[n] += 1
            else:
                seen[n] = 1
        L = [(k, seen[k]) for k in seen]
        L.sort(key=lambda d: d[1])
        return [d[0] for d in L[-k:]]