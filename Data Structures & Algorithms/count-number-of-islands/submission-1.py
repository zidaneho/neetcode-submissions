class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                oldVisitedCount = len(visited)
                self.explore(grid,i,j,visited)
                if oldVisitedCount < len(visited):
                    islands += 1
        return islands

    def explore(self,grid,i,j,visited):
        if (i,j) in visited:
            return
        if i >= len(grid) or i < 0 or j >= len(grid[i]) or j < 0:
            return
        if grid[i][j] == "1":
            visited.add((i,j))
            self.explore(grid,i+1,j,visited)
            self.explore(grid,i-1,j,visited)
            self.explore(grid,i,j-1,visited)
            self.explore(grid,i,j+1,visited)
        
