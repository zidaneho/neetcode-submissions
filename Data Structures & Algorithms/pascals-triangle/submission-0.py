class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[1]]
        for row in range(2,numRows+1):
            arr.append([])
            for i in range(row):
                if i-1 < 0 or i >= len(arr[-2]):
                    arr[-1].append(1)
                else:
                    arr[-1].append(arr[-2][i-1] + arr[-2][i])
        return arr