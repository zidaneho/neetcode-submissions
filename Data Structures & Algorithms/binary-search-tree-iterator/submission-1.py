# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.i = -1
        self.res = []
        def traverse(node):
            if node.left:
                traverse(node.left)
            self.res.append(node)
            if node.right:
                traverse(node.right)
        traverse(self.root)

    def next(self) -> int:
        self.i+= 1
        return self.res[self.i].val

    def hasNext(self) -> bool:
        return self.i < len(self.res)-1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()