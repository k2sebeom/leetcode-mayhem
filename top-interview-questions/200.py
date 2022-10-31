'''

Title: Number of Islands
Source: https://leetcode.com/problems/number-of-islands/
Comment: Think of the known algorithms (in this case DFS) and apply it to the context

'''

class Solution:
    def explore(self, i, j, grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 0
        
        if grid[i][j] in "02": # Either sea or already explored
            return 0
        
        grid[i][j] = "2" # Mark explored tile
        
        self.explore(i-1, j, grid)
        self.explore(i+1, j, grid)
        self.explore(i, j-1, grid)
        self.explore(i, j+1, grid)
        
        return 1
    
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                counter += self.explore(i, j, grid)
        return counter