# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.valid = True

        def postorderDfs(root):
            if root == None:
                #minimum, maximum
                return (float('inf'), -float('inf'))
            leftResult = postorderDfs(root.left)
            rightResult = postorderDfs(root.right)

            if leftResult[1] >= root.val or rightResult[0] <= root.val:
                self.valid = False

            min_result = min(leftResult[0],root.val)
            max_result = max(rightResult[1],root.val)

            return (min_result,max_result)
        postorderDfs(root)

        return self.valid
   
