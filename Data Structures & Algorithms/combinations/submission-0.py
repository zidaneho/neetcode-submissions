class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        def dfs(arr,num):
            if len(arr) == k:
                combinations.append(arr)
                return
            if num > n:
                return
            arr.append(num)
            dfs(arr[:],num+1)
            arr.pop()
            dfs(arr[:],num+1)
        dfs([],1)
        return combinations
            
