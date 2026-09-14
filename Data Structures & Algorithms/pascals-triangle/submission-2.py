class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        res = [[1]]
        for r in range(2,numRows+1):
            res.append([])
            for c in range(r):
                if c == 0 or c == len(res[-2]):
                    res[-1].append(1)
                else:
                    res[-1].append(res[-2][c] + res[-2][c-1])
        return res



