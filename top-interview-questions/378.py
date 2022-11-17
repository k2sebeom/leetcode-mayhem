'''

Title: Kth Smallest Element in a Sorted Matrix
Source: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
Comment: This is fake

'''


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        L = []
        add = L.append
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                add(matrix[i][j])
        L.sort()
        return L[k - 1]