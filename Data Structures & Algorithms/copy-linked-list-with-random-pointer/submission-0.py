"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {}
        oldToCopy[id(None)] = None
        
        curr = head
        while curr != None:
            newNode = Node(curr.val)
            oldToCopy[id(curr)] = newNode
            curr = curr.next

        curr = head
        while curr != None:
            copy = oldToCopy[id(curr)]
            copy.next = oldToCopy[id(curr.next)]
            copy.random = oldToCopy[id(curr.random)]
            curr = curr.next
        return oldToCopy[id(head)]