# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return "n"
        serialized = ""
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            node = queue.popleft()
            if node != None:
                serialized += " " + str(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                serialized += " n"
        return serialized.strip()
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split()
        if arr[0] == "n":
            return None
        root = TreeNode(arr[0])
        queue = deque()
        queue.append(root)
        index = 1
        while len(queue) > 0:
            node = queue.popleft()
            if arr[index] != "n":
                node.left = TreeNode(int(arr[index]))
                queue.append(node.left)
            index += 1
            if arr[index] != "n":
                node.right = TreeNode(int(arr[index]))
                queue.append(node.right)
            index += 1
                
        return root
            
