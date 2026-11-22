# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.globalMax = root.val

        def explore(node, isCenter=False):
            if node == None:
                return 0

            left = max(explore(node.left),0) 
            right = max(explore(node.right),0)
            self.globalMax = max(self.globalMax,left + right + node.val)

            return max(left,right,0) + node.val
            
        explore(root)
        return self.globalMax
