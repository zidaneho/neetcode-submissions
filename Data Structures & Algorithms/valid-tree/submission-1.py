class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {}
        for n1,n2 in edges:
            if n1 not in adjList:
                adjList[n1] = []
            if n2 not in adjList:
                adjList[n2] = []
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        visited = set()
        def dfs(node,parent):
            if node in visited:
                return False
            visited.add(node)
            for num in adjList.get(node,[]):
                if num == parent:
                    continue
                if not dfs(num,node):
                    return False
            return True
        if not dfs(0,-1):
            return False
        if len(visited) != n:
            return False
        
        return True