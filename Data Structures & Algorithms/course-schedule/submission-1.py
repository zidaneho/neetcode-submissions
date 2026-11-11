class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        #O(E)
        for course, preReq in prerequisites:
            adjList.setdefault(preReq, []).append(course)
        
        done = set()
        path = set()

        def dfs(node):
            if node in path:
                return False
            if node in done:
                return True
            path.add(node)
            for n in adjList.get(node,[]):
                if not dfs(n):
                    return False
            path.remove(node)
            done.add(node)
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return False
        return True
        

