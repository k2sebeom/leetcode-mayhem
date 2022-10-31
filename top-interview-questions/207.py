'''

Title: Course Schedule
Source: https://leetcode.com/problems/course-schedule/
Comment: Topological Sorting

'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inNodes = dict()
        for p in prerequisites:
            if p[0] in inNodes:
                inNodes[p[0]].append(p[1])
            else:
                inNodes[p[0]] = [p[1]]
        
        q = []
        result = []

        for i in range(numCourses):
            if i not in inNodes:
                q.append(i)
        
        while q:
            n = q.pop(0)
            for i in inNodes:
                if n in inNodes[i]:
                    inNodes[i].remove(n)
                    if len(inNodes[i]) == 0:
                        q.append(i)
            result.append(n)

        return len(result) == numCourses