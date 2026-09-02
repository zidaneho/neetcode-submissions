class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        undiscovered = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    undiscovered.append((i,j))
        discovered = set()
       
        ccs = 0
        while len(undiscovered) > 0:
            node = undiscovered.pop()
            if node in discovered:
                continue
            q = [node]
            while len(q) > 0:
                point = q.pop(0)
                wPoint = (point[0],point[1]-1)
                tPoint = (point[0]-1,point[1])
                rPoint = (point[0],point[1]+1)
                bPoint = (point[0]+1,point[1])
                if self.isPointValid(grid,wPoint) and wPoint not in discovered:
                    discovered.add(wPoint)
                    q.append(wPoint)
                if self.isPointValid(grid,tPoint) and tPoint not in discovered:
                    discovered.add(tPoint)
                    q.append(tPoint)
                if self.isPointValid(grid,rPoint) and rPoint not in discovered:
                    discovered.add(rPoint)
                    q.append(rPoint)
                if self.isPointValid(grid,bPoint) and bPoint not in discovered:
                    discovered.add(bPoint)
                    q.append(bPoint)
            ccs += 1
        return ccs
    def isPointValid(self, grid, point):
        return point[0] >= 0 and point[0] < len(grid) and point[1] >= 0 and point[1] < len(grid[point[0]]) and grid[point[0]][point[1]] == "1"
   

   
