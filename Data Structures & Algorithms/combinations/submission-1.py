class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        def dfs(idx,arr):
            if len(arr) == k:
                combinations.append(arr[:])
                return
            for i in range(idx, n+1):
                arr.append(i)
                dfs(i+1, arr)
                arr.pop()
        dfs(1,[])
        return combinations
            
            
