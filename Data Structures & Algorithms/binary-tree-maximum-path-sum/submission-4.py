# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        order = []
        self.globalMax = -float('inf')
        def postOrderDfs(node):
            if node == None:
                return
            postOrderDfs(node.left)
            postOrderDfs(node.right)
            order.append(node)
        postOrderDfs(root)

        result = {}
        def explore(node, isCenter=False):
            if node == None:
                return 0
            if node in result:
                return result[node]

            left = max(explore(node.left),0) 
            right = max(explore(node.right),0)
            self.globalMax = max(self.globalMax,left + right + node.val)
            result[node] = max(left,right,0) + node.val

            return result[node]
            
        explore(root)
        # for key,val in result.items():
        #     print(key.val,"maxpathsum:",val)
        return self.globalMax
