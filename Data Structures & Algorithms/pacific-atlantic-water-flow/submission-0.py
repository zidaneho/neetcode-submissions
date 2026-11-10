class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 0 will represent if the tile is reachable to the ocean, 1 will represent it is not reachable to the ocean (so far)
        # we will precompute the matrix such that the corners are reachable to the ocean
        canReachPacific = [[0 for _ in range(len(heights[0]))] for _ in range(len(heights))]
        canReachAtlantic = [[0 for _ in range(len(heights[0]))] for _ in range(len(heights))]
        def dfsHelperCheck(newI,newJ, i,j):
            return newI >= 0 and newJ >= 0 and newI < len(heights) and newJ < len(heights[i]) and heights[newI][newJ] >= heights[i][j]
        def dfs(i,j,matrix):
            if i < 0 or i >= len(heights) or j < 0 or j >= len(heights[i]) or matrix[i][j] == 1:
                return
            matrix[i][j] = 1
            if dfsHelperCheck(i,j+1, i,j):
                dfs(i,j+1,matrix)
            if dfsHelperCheck(i,j-1, i,j):
                dfs(i,j-1,matrix)
            if dfsHelperCheck(i+1,j, i,j):
                dfs(i+1,j,matrix)
            if dfsHelperCheck(i-1,j, i,j):
                dfs(i-1,j,matrix)
        res = []
        
        # pacific
        for j in range(len(heights[0])):
            dfs(0,j,canReachPacific)
        for i in range(1,len(heights)):
            dfs(i,0,canReachPacific)

        # atlantic

        for j in range(len(heights[0])):
            dfs(len(heights)-1,j,canReachAtlantic)
        for i in range(len(heights)-1):
            dfs(i,len(heights[0])-1,canReachAtlantic)

        for i,r in enumerate(heights):
            for j,c in enumerate(r):
                if canReachPacific[i][j] == 1 and canReachAtlantic[i][j] == 1:
                    res.append([i,j])
        return res
        