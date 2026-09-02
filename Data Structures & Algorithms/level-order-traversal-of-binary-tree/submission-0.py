from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    class NodeStruct:
        def __init__(self, node, depthLevel):
            self.node = node
            self.depthLevel = depthLevel
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = deque()
        queue.append(self.NodeStruct(root,0))
        mapping = {}
        while len(queue) > 0:
            nodeStruct = queue.popleft()
            node = nodeStruct.node
            depthLevel = nodeStruct.depthLevel
    
            if depthLevel in mapping:
                mapping[depthLevel].append(node.val)
            else:
                mapping[depthLevel] = [node.val]

            if node.left:
                queue.append(self.NodeStruct(node.left,depthLevel + 1))
            if node.right:
                queue.append(self.NodeStruct(node.right,depthLevel + 1))
        result = []
        for val in mapping.values():
            result.append(val)
        return result
        
            