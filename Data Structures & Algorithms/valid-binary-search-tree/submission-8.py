# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isValidBSTHelper(self, root, low, high):
        if root is None: return True

        left = root.left
        right = root.right

        # check left
        if low >= root.val: return False

        # check right:
        if high <= root.val: return False

        # base case - no children
        if not left and not right: return True

        # normal case
        return self.isValidBSTHelper(left, low, root.val) and self.isValidBSTHelper(right, root.val, high)
        

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, float('-inf'), float('inf'))
        
  