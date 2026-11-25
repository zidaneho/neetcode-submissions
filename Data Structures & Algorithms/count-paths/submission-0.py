class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(len(dp[-1])):
            dp[-1][i] = 1
        for i in range(len(dp)):
            dp[i][-1] = 1
        for r in range(len(dp)-2,-1,-1):
            for c in range(len(dp[r])-2,-1,-1):
                if dp[r][c] != 0:
                    continue
                dp[r][c] = dp[r+1][c] + dp[r][c+1]
        return dp[0][0]