class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        def flipRow(rowIndex):
            for i in range(len(grid[rowIndex])):
                grid[rowIndex][i] = (grid[rowIndex][i] + 1) % 2
        
        for i,row in enumerate(grid):
            if row[0] == 0:
                flipRow(i)
        
        def flipCol(colIndex):
            for i in range(len(grid)):
                grid[i][colIndex] = (grid[i][colIndex]+1)%2
        def colSum(colIndex):
            s = 0
            for i in range(len(grid)):
                s += grid[i][colIndex]
            return s
        for i in range(len(grid[0])):
            s = colSum(i)
            if s <= len(grid) // 2:
                flipCol(i)
        
        def getBinaryNum(row):
            multiplier = 1
            num = 0
            for i in range(len(row)-1,-1,-1):
                num += multiplier * row[i]
                multiplier *= 2
            return num
        
        total = 0
        for i,row in enumerate(grid):
            total += getBinaryNum(row)
       

        return total
            
