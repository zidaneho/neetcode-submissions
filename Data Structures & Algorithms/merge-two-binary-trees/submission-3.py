# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
       
        def traverse(root1,root2):
            if root1 == None and root2 == None:
                return None
            total = 0
            if root1:
                total += root1.val
            if root2:
                total += root2.val
            res_root = TreeNode(total)
            res_root.left = traverse(root1.left if root1 else None, root2.left if root2 else None)
            res_root.right = traverse(root1.right if root1 else None, root2.right if root2 else None)
            return res_root
        res_root = traverse(root1,root2)
        return res_root