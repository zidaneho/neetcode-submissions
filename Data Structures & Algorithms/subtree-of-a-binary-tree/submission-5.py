# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot == None:
            return True
        if root == None or subRoot == None:
            return False
        
        if root.val == subRoot.val and self.isSameTree(root,subRoot):
            return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

        
        if root.val != subRoot.val:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        else:
            return self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right,subRoot.right)
    def isSameTree(self,root : TreeNode, other : TreeNode):
        if root == None and other == None:
            return True
        elif root == None and other != None or root != None and other == None:
            return False
        if root.val != other.val:
            return False
        return self.isSameTree(root.left,other.left) and self.isSameTree(root.right,other.right)
        