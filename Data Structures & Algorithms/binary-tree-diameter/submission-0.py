# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.recurseTree(root,0)
    def recurseTree(self,root,maxDepth):
        if root is None:
            return maxDepth
        sumDepths = self.getMaxHeight(root.left,0) + self.getMaxHeight(root.right,0)
        if sumDepths > maxDepth:
            maxDepth = sumDepths
        return max(self.recurseTree(root.left,maxDepth),self.recurseTree(root.right,maxDepth))
    def getMaxHeight(self,root,depth):
        if root is None:
            return depth
        return max(self.getMaxHeight(root.left,depth+1),self.getMaxHeight(root.right,depth+1))

