# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False 
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def height(self, root : Optional[TreeNode]):
        if root == None:
            return -1
        height = 0
        if root.left != None:
            height = max(height, 1 + self.height(root.left))
        if root.right != None:
            height = max(height, 1 + self.height(root.right))
        print(root.val,height)
        return height
