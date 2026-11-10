"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # node vals to actual Node object
        if node == None:
            return None
        nodeMapping = {}
        queue = deque()
        queue.append(node)
        while len(queue) > 0:
            n = queue.popleft()
            if n.val in nodeMapping:
                continue
            nodeMapping[n.val] = Node(n.val,None)
            for neighbor in n.neighbors:
                queue.append(neighbor)
        visited = set()
        queue = deque()
        queue.append(node)
        while len(queue) > 0:
            n = queue.popleft()
            if n.val in visited:
                continue
            visited.add(n.val)
            for neighbor in n.neighbors:
                nodeMapping[n.val].neighbors.append(nodeMapping[neighbor.val])
                queue.append(neighbor)
        print(nodeMapping)
        return nodeMapping[1]
