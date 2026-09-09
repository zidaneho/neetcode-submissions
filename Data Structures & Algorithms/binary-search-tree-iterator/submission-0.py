# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.curr = None
        self.has_next = True

    def next(self) -> int:
        res = []
        def traverse(node):
            if node.left:
                traverse(node.left)
            res.append(node)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        i = 0
        while i < len(res):
            if self.curr == None:
                self.curr = res[i]
                break
            elif res[i].val == self.curr.val:
                self.curr = res[i+1]
                i+=1
                break 
            i +=1
        if i+1 >= len(res):
            self.has_next = False
        return self.curr.val

    def hasNext(self) -> bool:
        return self.has_next


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()