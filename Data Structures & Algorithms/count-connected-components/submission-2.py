class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connectedComponents = 0
        visited = set()
        adjList = {}
        for edge in edges:
            a,b = edge
            if a not in adjList:
                adjList[a] = []
            if b not in adjList:
                adjList[b] = []
            adjList[a].append(b)
            adjList[b].append(a)
        def traverse(val):
            if val in visited:
                return

            
            visited.add(val)
            for num in adjList[val]:
                traverse(num)
        for i in range(n):
            old_size = len(visited)
            if i not in adjList:
                connectedComponents += 1
            else:
                traverse(i)
            if len(visited) != old_size:
                connectedComponents += 1
        return connectedComponents
        
