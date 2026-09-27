# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        def traverse(root,curr_depth):
            if root == None:
                return
            curr_depth += 1
            self.max_depth = max(self.max_depth, curr_depth)
            traverse(root.left,curr_depth)
            traverse(root.right,curr_depth)
        traverse(root,0)
        return self.max_depth