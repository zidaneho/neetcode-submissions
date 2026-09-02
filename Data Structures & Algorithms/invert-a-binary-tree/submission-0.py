# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.post_dfs(root)
        return root
    def post_dfs(self, root):
        if root == None:
            return
        if root.left:
            self.post_dfs(root.left)
        if root.right:
            self.post_dfs(root.right)
        tmp = root.left
        root.left = root.right
        root.right = tmp