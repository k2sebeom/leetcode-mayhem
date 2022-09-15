'''

Title: Merge Intervals
Source: https://leetcode.com/problems/merge-intervals/
Comment: Sort the array if that seems easier. Also, think of known problems like interval scheduling.

'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key =lambda x: x[0])

        result = []
        s, e = intervals[0]
        for interval in intervals[1:]:
            if interval[0] > e:
                result.append([s, e])
                s = interval[0]
            e = max(interval[1], e)

        result.append([s, e])
        return result