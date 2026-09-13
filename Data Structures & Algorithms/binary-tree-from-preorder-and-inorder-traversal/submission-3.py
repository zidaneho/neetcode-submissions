# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        self.pre_idx = 0
        indices = {}
        for i, val in enumerate(inorder):
            indices[val] = i
        def build(low, high):
            if low >= high:
                return None
            val = preorder[self.pre_idx]
            self.pre_idx += 1
            node = TreeNode(val)
            mid = indices[val]
            node.left = build(low, mid)
            node.right = build(mid+1,high)
            return node
        return build(0,len(inorder))
            
