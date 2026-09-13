# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = deque()
        curr = head
        while curr != None:
            stack.append(curr.val)
            curr = curr.next
        curr = head
        is_left = True
        print(stack)
        while curr != None:
            curr.val = stack[0] if is_left else stack[-1]
            if is_left:
                stack.popleft()
                is_left = False
            else:
                stack.pop()
                is_left = True
            curr = curr.next